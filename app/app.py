from Flask import Flask, jsonify
import os
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Cofre Digital Online!",
        "environment": os.getenv('ENVIRONMENT', 'unknown'),
        "version": os.getenv('APP_VERSION', '1.0.0')
    })

@app.route('/database')
def database_info():

    db_host = os.getenv('DB_HOST')
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')

    logger.info(
        f"Conectando ao banco {db_host}"
    )

    return jsonify({
        "host": db_host,
        "user": db_user,
        "configured": db_password is not None
    })

@app.route('/api-key')
def api_key_info():

    api_key = os.getenv('EXTERNAL_API_KEY')

    masked_key = (
        api_key[:4]
        + "*"*(len(api_key)-8)
        + api_key[-4:]
    )

    return jsonify({
        "key_preview": masked_key
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)