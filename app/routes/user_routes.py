from flask import Blueprint, request, jsonify
from config import get_db_connection

user_bp = Blueprint("user_bp", __name__)

@user_bp.route("/identitas", methods=["POST"])
def submit_identitas():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    
    sql = "INSERT INTO users(nama, usia, angkatan, prodi, domisili, jenis_kelamin) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (data["nama"], data['usia'], data['angkatan'], data['prodi'], data['domisili'], data['jenis_kelamin'])
    
    cursor.execute(sql, val)
    conn.commit()
    cursor.close()
    conn.close()
    
    return jsonify({"message": "Identitas berhasil disimpan."})