import os
import pymysql
from urllib.parse import unquote
import traceback

password_decoded = unquote(os.environ.get('DB_PASSWORD'))

conn = pymysql.connect(host=os.environ.get('DB_HOST'),
            user=os.environ.get('DB_USER'),
            password=password_decoded,
            db=os.environ.get('DB_NAME'),
            cursorclass=pymysql.cursors.DictCursor)

MESSAGE = os.environ.get('MESSAGE')
SEVERITY = os.environ.get('SEVERITY', 'info')



def update_banner():
    try:
        with conn.cursor() as cur:
            cur.execute('DELETE FROM messages WHERE 1=1')
            if MESSAGE:
                cur.execute("SELECT id from mediatype WHERE name='text/markdown'")
                result = cur.fetchone()
                media_type_id = int(result['id'])

                cur.execute('INSERT INTO messages (content, media_type_id, severity) VALUES (%s, %d, %s)', (MESSAGE, media_type_id, SEVERITY))

        conn.commit()
    except Exception as e:
        print("ERROR: Unable to change the banner")
        print(e)
        traceback.print_exc()
    finally:
        conn.close()


update_banner()
