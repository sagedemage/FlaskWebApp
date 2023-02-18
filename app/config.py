import os

from dotenv import load_dotenv

load_dotenv()

# MySQL
DB_USERNAME = "root"
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = "notebook2"
DB_HOST = "127.0.0.1"
DB_PORT = "3306"

# SQLite
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_DIR = "tests/database"


def mysql_db_url():
    # 'mysql://username:password@host:port/database_name'
    db_url = 'mysql+pymysql://' + DB_USERNAME + ':' + DB_PASSWORD + '@' + DB_HOST + ':' + DB_PORT + '/' + DB_NAME
    return db_url


def sqlite_path():
    db_path = os.path.join(BASE_DIR, DB_DIR, "test.sqlite")
    return db_path


def sqlite_url():
    db_url = "sqlite:///" + os.path.join(BASE_DIR, DB_DIR, "test.sqlite")
    return db_url




