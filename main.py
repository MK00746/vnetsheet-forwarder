from flask import Flask, request
import requests

app = Flask(__name__)

GOOGLE_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbz2HlquO8CkiVI2DCnIf5gyr5IW29d8fUcpOfgAMhWp5mkGp_ZkJ4AyQVaU-P20X1sh/exec"

@app.route('/forward', methods=['POST'])
def forward():
    data = request.get_json()
    print("Received:", data)
    try:
        response = requests.post(GOOGLE_SCRIPT_URL, json=data)
        return {"status": response.status_code, "msg": response.text}
    except Exception as e:
        return {"error": str(e)}, 500

@app.route('/', methods=['GET'])
def home():
    return "V-NET Gateway is running.", 200

# ✅ REQUIRED: start Flask app for Render
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
