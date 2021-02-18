import os
import pymysql
from urllib.parse import unquote
import traceback

password_decoded = unquote(os.environ.get('DB_PASSWORD'))

conn = pymysql.connect(host=os.environ.get('DB_HOST'),
            user=os.environ.get('DB_USER'),
            password=password_decoded,
            db=os.environ.get('DB_NAME'))

MESSAGE = os.environ.get('MESSAGE')



def update_banner():
    if not MESSAGE:
        return

    try:
        with conn.cursor() as cur:
            cur.execute('DELETE FROM messages WHERE 1=1')
            cur.execute('INSERT INTO messages (content) VALUES (%s)', (MESSAGE))

        conn.commit()
    except Exception as e:
        print("ERROR: Unable to change the banner")
        print(e)
        traceback.print_exc()
    finally:
        conn.close()


update_banner()
