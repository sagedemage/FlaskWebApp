import os

from dotenv import load_dotenv

load_dotenv()

DB_USERNAME = "root"
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = "notebook2"
DB_HOST = "127.0.0.1"
DB_PORT = "3306"


def mysql_db_url():
    # 'mysql://username:password@host:port/database_name'
    db_url = 'mysql+pymysql://' + DB_USERNAME + ':' + DB_PASSWORD + '@' + DB_HOST + ':' + DB_PORT + '/' + DB_NAME
    return db_url




