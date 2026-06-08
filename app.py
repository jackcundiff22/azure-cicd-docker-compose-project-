from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Multi-Container Docker App on Azure</h1>
    <p>This Flask app is running behind an Nginx reverse proxy.</p>
    <p>Managed with Docker Compose.</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
