from .step import Step

from pytube import YouTube
from yt_concate.settings import VIDEOS_DIR


class DownloadVideos(Step):
    def process(self, data, inputs, utils):
        yt_set = set([found.yt for found in data])  # 淘汰重複
        print("videos to download=", len(yt_set))

        for yt in yt_set:
            url = yt.url

            if utils.video_file_exists(yt):
                print(f"found existing video file for {url}, skipping")
                continue
            try:
                print("downloading", url)
                YouTube(url).streams.first().download(output_path=VIDEOS_DIR, filename=yt.id)  # 設定檔名
            except:
                print(f"Error to download{url}")
                continue
