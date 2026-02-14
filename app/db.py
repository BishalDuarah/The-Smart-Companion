# app/db.py
import sqlite3

def get_conn():
    conn = sqlite3.connect("smart_companion.db")
    return conn
