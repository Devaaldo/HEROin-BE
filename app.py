from flask import Flask,request, jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS
from config import Config

app = Flask(__name__)
CORS(app)

# Register Blueprint
app.register_blueprint(user_bp, url_prefix="/api/user")
app.register_blueprint(admin_bp, url_prefix="/api/admin")

if __name__ == "__main__":
    app.run(debug=True)