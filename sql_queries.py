# DROP TABLES

song_select = ("""
    SELECT song_id, artists.artist_id
    FROM songs JOIN artists  ON songs.artist_id = artists.artist_id
    WHERE songs.title = %s
    AND artists.name = %s
    AND songs.duration = %s
""")

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"


def create_fields(fields):
    """Generet sting with field and type"""
    return ",".join(" {} {} ".format(key, lst) for key, lst in fields.items())

# CREATE TABLES
songplays = {
       "songplay_id": "VARCHAR",
       "start_time": "timestamp",
       "user_id": "INT NOT NULL",
       "level": "VARCHAR NOT NULL",
       "song_id": "VARCHAR",
       "artist_id": "VARCHAR",
       "session_id": "INT NOT NULL",
       "location": "VARCHAR",
       "user_agent": "TEXT"}

users = {"user_id": "VARCHAR",
        "first_name": "VARCHAR",
        "last_name": "VARCHAR",
        "gender": "VARCHAR",
        "level": "VARCHAR"
}

songs = {"song_id": "VARCHAR",
         "title": "VARCHAR",
         "artist_id": "VARCHAR NOT NULL",
         "year": "INT",
         "duration": "FLOAT"}

artists = {"artist_id": "VARCHAR",
           "name": "VARCHAR",
           "location": "VARCHAR",
           "latitude": "DECIMAL(9,6)",
           "longitude": "DECIMAL(9,6)"}

time = {"start_time": "TIMESTAMP",
        "hour": "INT",
        "day": "INT",
        "week": "INT",
        "month": "INT",
        "year": "INT",
        "weekday": "INT"}


songplay_table_create = ("""CREATE TABLE IF NOT EXISTS {} ({});""".format(
    'songplays', create_fields(songplays)))
user_table_create = ("""CREATE TABLE IF NOT EXISTS {} ({});""".format(
    'users', create_fields(users)))
song_table_create = ("""CREATE TABLE IF NOT EXISTS {} ({});""".format(
    'songs', create_fields(songs)))
artist_table_create = ("""CREATE TABLE IF NOT EXISTS {} ({});""".format(
    'artists', create_fields(artists)))
time_table_create = ("""CREATE TABLE IF NOT EXISTS {} ({});""".format(
    'time', create_fields(time)))

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplays VALUES (DEFAULT, %s, %s, %s, %s, %s, %s, %s, %s)
""")

user_table_insert = ("""INSERT INTO users (user_id, first_name, last_name, gender, level) VALUES (%s, %s, %s, %s, %s)
""")

song_table_insert = ("""INSERT INTO songs (song_id, title, artist_id, year, duration) VALUES (%s, %s, %s, %s, %s)
""")

artist_table_insert = ("""INSERT INTO artists (artist_id, name, location, latitude, longitude) VALUES (%s, %s, %s, %s, %s)
""")


time_table_insert = ("""INSERT INTO time VALUES (%s, %s, %s, %s, %s, %s, %s)                      
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]


