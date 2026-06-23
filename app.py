from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def index():
    message = os.environ.get('APP_MESSAGE', 'No message set')
    return f'Service Models Lab 2\nAPP_MESSAGE: {message}\n'

@app.route('/health')
def health():
    return 'OK\n'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
