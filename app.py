from flask import Flask, render_template, request, redirect, url_for
from flask import redirect, jsonify
import mysql.connector


mybdd= mysql.connector.connect(user='cary', password='cordoba#1234AA', host='localhost', database='e_learning', use_unicode=True, charset='utf8')


app = Flask(__name__)


@app.route('/')
def index():
    cursor = mybdd.cursor()
    sql = "SELECT * FROM videos"
    cursor.execute(sql)
    results = cursor.fetchall()
    return render_template('index.html', results = results, len=len(results))


@app.route('/addvideo')
def add_video():
    return render_template('addvideo.html')
    
@app.route('/upload_video', methods = ["POST", "GET"])
def upload_video():

    if request.method == "POST":
        lien           = request.form.get('lien')
        categorie      = request.form.get('categorie')
        titre          = request.form.get('titre')
        author         = request.form.get('author')
        description    = request.form.get('description')
        anne_video     = request.form.get('anne_video')

        cursor = mybdd.cursor()
        cursor.execute('''INSERT INTO  videos
                        (titre, author, lien, anne_video, description, categorie) 
                        VALUES (%s, %s, %s, %s, %s, %s)''',
                        (lien, categorie, titre, author, description, anne_video))

        mybdd.commit()
    return redirect('/')





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