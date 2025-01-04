import psycopg2
from psycopg2 import extras

connection = psycopg2.connect(dbname='films')

# try:
#     with connection:
#         with connection.cursor(cursor_factory=extras.DictCursor) as cursor:
#             cursor.execute("""
#                 SELECT * FROM films JOIN directors
#                     ON films.director_id = directors.id
#                     WHERE name = 'Sidney Lumet';
#                             """)
#             film = cursor.fetchone()
# finally:
#     connection.close()

# print(film['title'])

# try:
#     with connection:
#         with connection.cursor(cursor_factory=extras.DictCursor) as cursor:
#             cursor.execute("""
#                 SELECT * FROM films
#                 JOIN directors
#                 ON films.director_id = directors.id
#                 WHERE name = 'Francis Ford Coppola'
#                 ORDER BY duration DESC
#             """)
#             films = cursor.fetchall()
# finally:
#     connection.close()

# print(films[1]['duration'])

try:
    with connection:
        with connection.cursor(cursor_factory=extras.DictCursor) as cursor:
            cursor.execute("""
                    SELECT genre, count(id) FROM films
                    WHERE duration < 110
                    GROUP BY genre;
                            """)
            counts = cursor.fetchall()
finally:
    connection.close()

print(dir(counts))

# If you print out the counts object it doesn't look like a dictionary. This is because it is a dict-row object from psycopg2
for genre, count in counts:
    print(f"{genre}: {count}")

