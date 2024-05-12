from flask import Flask
import pymysql.cursors

app = Flask(__name__)

def get_db_connection():
    return pymysql.connect(host='db',
                           user='user',
                           password='password',
                           database='mydatabase',
                           cursorclass=pymysql.cursors.DictCursor)

@app.route('/')
def index():
    connection = get_db_connection()
    with connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT `msg` FROM `messages`")
            message = cursor.fetchone()
    return 'Message from the database: ' + message['msg']

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
