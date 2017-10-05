from flask import Flask, render_template, request, send_from_directory

from Downloader import Downloader
from mp4tomp3 import m4tm3

app = Flask(__name__)
name = ""

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/downloader/")
def downloader():
    return render_template('downloader.html')


@app.route("/process", methods=['POST'])
def process():
    print("fetching...")
    url = request.form['inputUrl']
    global name
    name = Downloader.getname(url)
    Downloader.getdata(url)
    res = '360p'
    print("downloading...")
    Downloader.download(url, res)
    print("converting...")
    m4tm3('./files/dump/', './files/fresh/')
    return "Done!"


@app.route("/downloader/processed")
def processed():
    global name
    print("returning file as mp3: {0}".format(name))
    return send_from_directory('./files/fresh', '{0}.mp3'.format(name),
                               as_attachment=True, attachment_filename=name + '.mp3')
