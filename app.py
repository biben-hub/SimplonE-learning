from flask import Flask, render_template
from flask import redirect, jsonify
import mysql.connector


mybdd= mysql.connector.connect(user='cary', password='cordoba#1234AA', host='localhost', database='e_learning', use_unicode=True, charset='utf8')


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/jinja')
def jinja():
    cursor = mybdd.cursor()
    sql = "SELECT * FROM videos"
    cursor.execute(sql)
    results = cursor.fetchall()
    return render_template('index.html', results = results, len=len(results))


@app.route('/addvideo')
def add_video():
    return render_template('addvideo.html')   



@app.route('/apivideo',methods=['GET'])
def api_video():
    dict_videos=[]
    cursor = mybdd.cursor(dictionary=True)
    print('Curseur --->',cursor)
    sql='select * from videos'
    cursor.execute(sql)

    for i in cursor:
        dict_videos.append(i)

    resp = jsonify(dict_videos)
    return resp

if __name__ == '__main__':
    app.run(debug=True)