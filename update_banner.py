import os
import pymysql


conn = pymysql.connect(os.environ.get('DB_HOST'), os.environ.get('DB_USER'),
    os.environ.get('DB_PASSWORD'), os.environ.get('DB_NAME'))

MESSAGE = os.environ.get('MESSAGE')



def update_banner():
    if not MESSAGE:
        return

    try:
        with conn.cursor() as cur:
            cur.execute('DELETE FROM messages where 1=1')
            cur.execute('INSERT INTO messages (content) VALUES (%s)', (MESSAGE))

        conn.commit()
    finally:
        conn.close()


update_banner()