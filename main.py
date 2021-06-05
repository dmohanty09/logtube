# This is a sample Python script.
import logtube.tasks
from logtube.scraper import YoutubeScraper, transcribe_video
from logtube.config import config

CHANNEL_NAME = 'smosh'
PLAYLIST_ID = 'PLShD8ZZW7qjkTzS17ENOnfpk6Sq220k1z'

if __name__ == '__main__':
    print(YoutubeScraper().get_most_popular())
    # yt_scraper = YoutubeScraper()
    # task = logtube.tasks.crawl_most_popular.delay()
    # print(task)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
