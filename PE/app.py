import flask from flask

app = Flask(__name__)

@app.route('/)'
def hello():
    return 'Hello World...Again'

if __name__ = '__main__':
    app.run(host=os.environment.get('IP'),
        port=int(os.environment.get('PORT')),
        debug=True)