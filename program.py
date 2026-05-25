from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Dinesh! Flask app running inside Docker and Kubernetes 🚀"

@app.route("/health")
def health():
    return {"status": "success"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
