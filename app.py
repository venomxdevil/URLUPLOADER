from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Legend Sources!'

if __name__ == '__main__':
    # Run the Flask app on port 80
    app.run(host='0.0.0.0', port=80)
