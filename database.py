import sqlite3
from config import DATABASE_NAME


def get_connection():
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        username TEXT,
        full_name TEXT,
        join_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        last_seen TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        points INTEGER DEFAULT 0,
        referrals INTEGER DEFAULT 0,
        is_banned INTEGER DEFAULT 0
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS channels (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        channel_id TEXT UNIQUE,
        channel_name TEXT,
        channel_username TEXT,
        force_join INTEGER DEFAULT 1
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS replies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        trigger TEXT UNIQUE,
        response TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS referrals (
        inviter_id INTEGER,
        invited_id INTEGER UNIQUE,
        join_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS settings (
        key TEXT PRIMARY KEY,
        value TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        action TEXT,
        user_id INTEGER,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()


def add_user(user_id, username, full_name):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    INSERT OR IGNORE INTO users
    (user_id, username, full_name)
    VALUES (?, ?, ?)
    """, (user_id, username, full_name))

    conn.commit()
    conn.close()


def update_last_seen(user_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    UPDATE users
    SET last_seen=CURRENT_TIMESTAMP
    WHERE user_id=?
    """, (user_id,))

    conn.commit()
    conn.close()


def get_user(user_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
    user = cur.fetchone()

    conn.close()
    return user


def get_statistics():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM users")
    users = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM users WHERE is_banned=1")
    banned = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM channels")
    channels = cur.fetchone()[0]

    conn.close()

    return {
        "users": users,
        "banned": banned,
        "channels": channels
    }


def add_channel(channel_id, name, username):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    INSERT OR IGNORE INTO channels
    (channel_id, channel_name, channel_username)
    VALUES (?, ?, ?)
    """, (channel_id, name, username))

    conn.commit()
    conn.close()


def get_channels():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    SELECT * FROM channels
    ORDER BY id
    """)

    data = cur.fetchall()

    conn.close()

    return data
def add_log(action, user_id=None):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO logs(action, user_id)
    VALUES (?, ?)
    """, (action, user_id))

    conn.commit()
    conn.close()

def delete_channel(channel_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    DELETE FROM channels
    WHERE channel_id = ?
    """, (channel_id,))

    deleted = cur.rowcount

    conn.commit()
    conn.close()

    return deleted > 0
