from multiprocessing import Process
import os

from pytube import YouTube

from .step import Step
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
                processes = []

                for i in range(os.cpu_count()):
                    processes.append(Process(target=Process))

                if __name__ == "__main__":
                    for process in processes:
                        process.start()
                    for process in processes:
                        process.join()
            except:
                print(f"Error when downloading {url}")
                continue

        return data
