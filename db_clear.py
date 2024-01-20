import sqlite3


with sqlite3.connect('game_data.db') as con:
    cur = con.cursor()
    cur.execute(f"""DELETE FROM results""")