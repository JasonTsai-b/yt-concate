import os
from pprint import pprint
from .step import Step
from yt_concate.settings import CAPTIONS_DIR

class ReadCaption(Step):
    def process(self, data, inputs, utils):
        data = {}
        for caption_file in os.listdir(CAPTIONS_DIR):  # 列出資料夾檔案(os.listdir)
            captions = {}
            with open(os.path.join(CAPTIONS_DIR, caption_file), "r") as f:  # 路徑組裝
                time_line = False
                time = None
                caption = None
                for line in f:
                    line = line.strip()
                    if "-->" in line:
                        time_line = True
                        time = line
                        continue
                    if time_line:
                        caption = line
                        captions[caption] = time  # captions[key] = value
                        time_line = False  # 繼續往下抓
            data[caption_file] = captions  # 把captions字典再存入data字典, data[key] = value

        pprint(data)
        return data
