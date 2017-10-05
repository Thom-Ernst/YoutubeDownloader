from pytube import YouTube


class Downloader:
    @staticmethod
    def getname(url):
        yt = YouTube(url)
        return yt.filename

    @staticmethod
    def getdata(url):
        yt = YouTube(url)
        return yt.get_videos()

    @staticmethod
    def download(url, res):
        yt = YouTube(url)
        yt.get('mp4', res).download('./files/dump/')
