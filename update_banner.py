import os
import pymysql
from urllib.parse import unquote
import traceback
import json

password_decoded = unquote(os.environ.get('DB_PASSWORD'))

conn = pymysql.connect(host=os.environ.get('DB_HOST'),
            user=os.environ.get('DB_USER'),
            password=password_decoded,
            db=os.environ.get('DB_NAME'),
            cursorclass=pymysql.cursors.DictCursor)

SEVERITY = os.environ.get('SEVERITY', 'info')
MESSAGES = json.loads(os.environ.get('MESSAGES'))



def update_banner():
    if not MESSAGES:
        return

    try:
        with conn.cursor() as cur:
            cur.execute('DELETE FROM messages WHERE 1=1')
            for message in MESSAGES:
                cur.execute('INSERT INTO messages (content, media_type_id, severity) VALUES (%s, %s, %s)', (message, media_type_id, SEVERITY))

        conn.commit()
    except Exception as e:
        print("ERROR: Unable to change the banner")
        print(e)
        traceback.print_exc()
    finally:
        conn.close()

update_banner()
