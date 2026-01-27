from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def index():
    env = os.getenv("ENV", "Not Set")
    version = os.getenv("APP_VERSION", "1.0")

    return f"""
    <h1>Hello from Azure App Service</h1>
    <p>ENV = {env}</p>
    <p>Version = {version}</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))

