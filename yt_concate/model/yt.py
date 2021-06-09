import os

from yt_concate.settings import CAPTIONS_DIR
from yt_concate.settings import VIDEOS_DIR


class YT:
    def __init__(self, url):
        self.url = url
        self.id = self.get_video_id_from_url(self.url)
        self.cation_filepath = self.get_captions_filepath()
        self.video_filepath = self.get_video_filepath()
        self.captions = None

    @staticmethod  # can ignore "self"
    def get_video_id_from_url(url):
        return url.split("watch?v=")[-1]  # split開後取後半部

    def get_captions_filepath(self):
        return os.path.join(CAPTIONS_DIR, self.id + ".txt")

    def get_video_filepath(self):
        return os.path.join(VIDEOS_DIR, self.id + ".mp4")

    def __str__(self):
        return "<YT(" + self.id + ")>"

    def __repr__(self):
        content = " : ".join([
            "id=" + str(self.id),
            "caption_filepath=" + str(self.cation_filepath),
            "video_filepath" + str(self.video_filepath),
        ])
        return "<Found(" + content + ")>"
