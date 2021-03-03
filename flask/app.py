from flask import Flask, render_template, request, redirect, url_for
from flask import redirect, jsonify
import mysql.connector
import sys


mybdd = mysql.connector.connect(
    host="db_1",
    user="root",
    database="cloudflix_db",
    password="example",
)


app = Flask(__name__)


@app.route('/')
def index():
    cursor = mybdd.cursor()
    sql = "SELECT * FROM videos"
    cursor.execute(sql)
    results = cursor.fetchall()
    return render_template('index.html', results=results, len=len(results))


@app.route('/addvideo')
def add_video():
    return render_template('addvideo.html')


@app.route('/upload_video', methods=["POST", "GET"])
def upload_video():

    if request.method == "POST":
        lien = request.form.get('lien')
        categorie = request.form.get('categorie')
        titre = request.form.get('titre')
        author = request.form.get('author')
        description = request.form.get('description')
        anne_video = request.form.get('anne_video')

        cursor = mybdd.cursor()
        cursor.execute('''INSERT INTO  videos
                        (titre, author, lien, anne_video, description, categorie) 
                        VALUES (%s, %s, %s, %s, %s, %s)''',
                       (titre, author,lien ,anne_video, description,categorie ))

        mybdd.commit()
    return redirect('/')


@app.route('/apivideo', methods=['GET'])
def api_video():
    dict_videos = []
    cursor = mybdd.cursor(dictionary=True)
    print('Curseur --->', cursor)
    sql = 'select * from videos'
    cursor.execute(sql)

    for i in cursor:
        dict_videos.append(i)

    resp = jsonify(dict_videos)
    return resp


if __name__ == '__main__':
    print('hello', file=sys.stderr)
    app.run(host='0.0.0.0', port=4000, debug=True)