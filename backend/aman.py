from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import psycopg2
# from dotenv import load_dotenv
# import os

app = Flask(__name__, static_folder='static')
CORS(app)


# PostgreSQL database configuration
# Your database connection configuration
db_host = "34.130.22.95"
db_name = "myappdb"
db_user = "myuser"
db_password = "mypassword"

def connect_to_db():
    try:
        conn = psycopg2.connect(
            dbname=db_name,
            user=db_user,
            password=db_password,
            host=db_host
        )
        return conn
    except psycopg2.Error as e:
        print("Error connecting to PostgreSQL database:", e)
        return None

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/upload', methods=['POST'])
def upload_to_database():
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')

    conn = connect_to_db()
    if conn is None:
        return jsonify({'error': 'Failed to connect to database'}), 500
    
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO aman (first_name, last_name) VALUES (%s, %s)", (first_name, last_name))
        conn.commit()
        return jsonify({'message': 'Data uploaded successfully'}), 200
    except psycopg2.Error as e:
        conn.rollback()
        return jsonify({'error': 'Failed to upload data to database You can check code once', 'details': str(e)}), 500
    finally:
        cur.close()
        conn.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
