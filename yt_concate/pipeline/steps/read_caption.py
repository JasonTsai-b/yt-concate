from .step import Step


class ReadCaption(Step):
    def process(self, data, inputs, utils):
        for yt in data:
            if not utils.caption_file_exists(yt):
                continue

            captions = {}
            with open(yt.cation_filepath, "r") as f:  # 路徑組裝
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
            yt.captions = captions  # 把captions字典再存入data字典, data[key] = value

        return data
