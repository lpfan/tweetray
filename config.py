import os


TWITTER_ACCESS_TOKEN = '3140580214-1bDvKuQJpdB3pvLG4MxMgkj10CHGoYGSlb4ljBk'
TWITTER_ACCESS_SECRET = 'Oob3LC4yULH9PB2djfc4SKC7qrcRphe1m1jHsDaaosuxn'

TWITTER_CONSUMER_KEY = 'J6AywCfSbGy00WDBDeJxtUAdU'
TWITTER_CONSUMER_SECRET = 'hpHiuISrjjDNzg1xTSZNeYMPS7o9D8v76tT3Zvw5sGS2O16efv'


TWEET_QUEUE_NAME = 'tweets'

BUFFERED_TWEETS_COUNT = 50
BUFFERED_TWEETS_FILES_COUNT = 4
WORKER_COUNT = 4
TRACK_WORDS = ['buzzfeed', 'putin', 'obama', 'isis']


BASE_DIR = os.path.abspath(os.path.dirname(__file__))
TEMP_FILE_PATH = os.path.join(BASE_DIR, 'temp')
LOGS_PATH = os.path.join(BASE_DIR, 'logs')


MONGO_HOST = 'localhost'
MONGO_PORT = 27017
TWITTER_DB = 'twitter'
RAW_TWEETS_COLLECTION = 'raw_tweets'
