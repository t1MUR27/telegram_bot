import sqlite3

database = sqlite3.connect('weather_bot.db')

cursor = database.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS client_tegram(
    history_id INTEGER PRIMARY KEY AUTOINCREMENT,
    telegram_id BIGINT,
    full_name TEXT,
    date INTEGER,
    city TEXT,
    weather_desc TEXT,
)

''')
database.commit()
database.close()
