from modules import config
import sqlite3
from os import getcwd, chdir, path
from pathlib import Path

config = config.Config()


def connect():
    chdir(path.dirname(__file__))
    conn = sqlite3.connect(f"{Path(getcwd()).parent}/{config.db_file}")
    return conn, conn.cursor()


def close(conn):
    conn.commit()
    conn.close()
