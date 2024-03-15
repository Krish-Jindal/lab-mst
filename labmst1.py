from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '\n\n\t\tKrish Jindal | 21BCS7871'

if __name__ == '__main__':
    app.run(debug=True)
