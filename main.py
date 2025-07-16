from flask import Flask, request
import requests

app = Flask(__name__)

GOOGLE_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbxqKVaJzr0xWgZCk_Awf1EqmpO3O6-I4d7gXXFJ3kch-vZ8Al9xl2uKdVcBuaUiHKCK/exec"

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
