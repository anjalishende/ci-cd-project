from flask import Flas

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Devops!'

if __name__ == '__main__':
    app.run()
