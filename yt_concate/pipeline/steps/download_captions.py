# import os
import time

from pytube import YouTube

from yt_concate.pipeline.steps.step import Step
# from .step import StepException


class DownloadCaptions(Step):
    def process(self, data, inputs, utils):
        start = time.time()
        for url in data:
            print("downloading caption for", url)
            if utils.caption_file_exists(url):
                print("found existing caption file")
                continue

            print(url)
            try:
                source = YouTube(url)
                en_caption = source.captions.get_by_language_code('a.en')
                en_caption_convert_to_srt = (en_caption.generate_srt_captions())
            except:
                print("KeyError or AttributeError when downloading caption for:", url)
                continue

            # print(en_caption_convert_to_srt)

            text_file = open(utils.get_captions_filepath(url), "w", encoding="utf-8")
            text_file.write(en_caption_convert_to_srt)
            text_file.close()

        end = time.time()
        print("took", end-start, "seconds")
