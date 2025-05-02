from flask import Flask,request, jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)

mysql = MySQL(app)

@app.route('/')

def home():
    return 'Backend Sistem Pakar Kecanduan Game Online'

# Endpoint User
@app.route('/users', methods=['POST'])
def add_user():
    data = request.json
    nama = data.get('nama_lengkap')
    usia = data.get('usia')
    angkatan = data.get('angkatan')
    program_studi = data.get('program_studi')
    domisili = data.get('domisili')
    jenis_kelamin = data.get('jenis_kelamin')
    
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO users(nama_lengkap, usia, angkatan, program_studi, domisili, jenis_kelamin) VALUES (%s, %s, %s, %s, %s, %s)", (nama, usia, angkatan, program_studi, domisili, jenis_kelamin))
    mysql.connection.commit()
    cur.close()
    
    return jsonify({"message": "User berhasil ditambahkan"}), 201


# Endpoint Kuesioner
@app.route('/kuesioner', methods=['POST'])
def add_kuesioner():
    data = request.json
    user_id = data.get('user_id')
    pertanyaan = data.get('pertanyaan')
    jawaban = data.get('jabawan')
    
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO kuesioner (user_id, pertanyaan, jawaban) VALUES (%s, %s, %s)", (user_id, pertanyaan, jawaban))
    mysql.connection.commit()
    cur.close()

if __name__ == '__main__':
    app.run(debug=True)