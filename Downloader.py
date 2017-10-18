from pytube import YouTube


class Downloader:
    @staticmethod
    def getname(url):
        yt = YouTube(url)
        return yt.filename

    @staticmethod
    def getdata(url):
        yt = YouTube(url)
        def fixres():
            global yt
            res = yt.get_videos()
            return res
        return fixres()

    @staticmethod
    def download(url, res):
        yt = YouTube(url)
        yt.get('mp4', res).download('./files/dump/')
