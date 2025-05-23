# HEROin - Backend

HEROin (Health Evaluation for Reducing Online-gaming negative impact) adalah sistem pakar untuk mengidentifikasi dampak negatif kecanduan game online di kalangan mahasiswa. Backend aplikasi ini menangani logika sistem pakar dengan metode backward chaining dan certainty factor. test

## Fitur

- API RESTful untuk frontend
- Implementasi metode backward chaining untuk pemilihan hipotesis
- Implementasi metode certainty factor untuk perhitungan tingkat keyakinan
- Penyimpanan data dengan MySQL
- Generate laporan dalam format Excel dan PDF
- Statistik untuk dashboard

## Teknologi yang Digunakan

- Python 3.7+
- Flask
- Flask-SQLAlchemy
- Flask-CORS
- MySQL
- XlsxWriter (untuk laporan Excel)
- ReportLab (untuk laporan PDF)
- Pandas (untuk manipulasi data)

## Persyaratan Sistem

- Python 3.7 atau lebih baru
- MySQL 5.7 atau lebih baru
- Pip (Python package manager)

## Cara Instalasi

1. Clone repositori
```sh
git clone https://github.com/username/heroin-backend.git
cd heroin-backend
```

2. Buat dan aktifkan virtual environment
```sh
python -m venv venv
source venv/bin/activate  # Di Windows: venv\Scripts\activate
```

3. Install dependensi
```sh
pip install -r requirements.txt
```

4. Siapkan database MySQL
```sh
mysql -u root -p < migrations.sql
```
Atau jalankan query SQL secara manual di MySQL

5. Sesuaikan konfigurasi database di `app.py`
```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/heroin_db'
```

6. Jalankan aplikasi
```sh
python app.py
```

Server akan berjalan di http://localhost:5000

## Struktur API

| Endpoint | Method | Deskripsi |
|----------|--------|-----------|
| `/api/user-info` | POST | Menyimpan informasi pengguna |
| `/api/hypotheses` | GET | Mendapatkan daftar hipotesis |
| `/api/selected-hypothesis` | POST | Menyimpan hipotesis yang dipilih |
| `/api/questions/:hypothesis_id` | GET | Mendapatkan pertanyaan berdasarkan hipotesis |
| `/api/submit-questionnaire` | POST | Mengirim jawaban kuesioner |
| `/api/result/:result_id` | GET | Mendapatkan hasil analisis |
| `/api/result/:result_id` | DELETE | Menghapus hasil analisis |
| `/api/download-report/:result_id` | GET | Mengunduh laporan individu (Excel/PDF) |
| `/api/statistics` | GET | Mendapatkan statistik untuk dashboard |
| `/api/download-all-reports` | GET | Mengunduh laporan keseluruhan (Excel/PDF) |

## Metode Sistem Pakar

### Backward Chaining

Backend mengimplementasikan backward chaining sederhana dengan langkah:
1. Pengguna memilih hipotesis (dampak negatif)
2. Sistem memberikan pertanyaan terkait hipotesis tersebut
3. Jawaban dianalisis untuk memverifikasi hipotesis

### Certainty Factor

Perhitungan certainty factor menggunakan rumus:
1. Jika CF1 dan CF2 keduanya positif: CF = CF1 + CF2 * (1 - CF1)
2. Jika CF1 dan CF2 keduanya negatif: CF = CF1 + CF2 * (1 + CF1)
3. Jika CF1 dan CF2 berbeda tanda: CF = (CF1 + CF2) / (1 - min(|CF1|, |CF2|))

## Model Database

Backend menggunakan 5 tabel utama:
- `user` - Data mahasiswa
- `hypothesis` - Jenis-jenis dampak negatif
- `question` - Pertanyaan untuk setiap hipotesis
- `result` - Hasil analisis
- `answer` - Jawaban kuesioner

```
├── user
│   ├── id
│   ├── nama
│   ├── usia
│   ├── angkatan
│   ├── program_studi
│   ├── domisili
│   ├── jenis_kelamin
│   └── created_at
│
├── hypothesis
│   ├── id
│   ├── code
│   └── description
│
├── question
│   ├── id
│   ├── hypothesis_id
│   ├── code
│   └── text
│
├── result
│   ├── id
│   ├── user_id
│   ├── hypothesis_id
│   ├── cf_value
│   ├── diagnosis
│   ├── recommendation
│   └── created_at
│
└── answer
    ├── id
    ├── result_id
    ├── question_id
    └── cf_value
```

## Troubleshooting

### Masalah Koneksi Database
- Pastikan server MySQL berjalan
- Verifikasi kredensial database di file konfigurasi
- Periksa apakah database `heroin_db` sudah dibuat

### Error Flask before_first_request
Jika menggunakan Flask versi terbaru, gunakan pendekatan ini:
```python
if __name__ == '__main__':
    with app.app_context():
        initialize_database()
    app.run(debug=True)
```

## Kontribusi

Kontribusi selalu diterima! Silakan buat pull request atau buka issue untuk diskusi fitur baru atau perbaikan.

## Lisensi

[MIT License](LICENSE)

## Kontak

akbarprdn2512@gmail.com
