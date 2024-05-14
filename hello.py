from flask import Flask, render_template,jsonify,request,url_for
from dotenv import load_dotenv
from os import getenv
load_dotenv()

app = Flask(__name__)

@app.route('/')
@app.route('/hello/<name>')
def index(name=None):
    if name is None:
        print(url_for('index'))
        return render_template('index.html', name=name)
    else:
        return f"Hello {name}!"

if __name__ == '__main__':
    app.run(debug=True, port=int(getenv('PORT')), host=getenv('IP'))