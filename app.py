from flask import Flask, render_template, request, send_from_directory

from Downloader import Downloader
from mp4tomp3 import m4tm3

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/downloader/")
def downloader():
    return render_template('downloader.html')


@app.route("/downloader/process/", methods=['POST'])
def process():
    url = request.form['inputUrl']
    name = Downloader.getname(url)
    Downloader.getdata(url)
    res = '360p'
    Downloader.download(url, res)
    m4tm3('./files/dump/', './files/fresh/')
    print("returning file as mp3: {0}".format(name))
    return send_from_directory('./files/fresh', '{0}.mp3'.format(name))
