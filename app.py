from flask import Flask, render_template
from flask import redirect

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/addvideo')
def add_video():
    return render_template('addvideo.html')

if __name__ == '__main__':
    app.run()
