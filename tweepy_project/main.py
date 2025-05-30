import nltk
import tweepy
from app import App
from environment import environment
from nltk.sentiment import SentimentIntensityAnalyzer
from tweepy import Client

from .infrastructure.analizer import AnalizerAdapter
from .infrastructure.requests import RequestAdapter
from .infrastructure.utils import Utils

nltk.download("stopwords")
nltk.download("wordnet")
nltk.download("vader_lexicon")

sia = SentimentIntensityAnalyzer()

bearer_token = environment.__getitem__("bearer_token")

client: Client = tweepy.Client(bearer_token=bearer_token, wait_on_rate_limit=True)

analizer = AnalizerAdapter(sia)
requests = RequestAdapter(client)
utils = Utils()

app = App(analizer=analizer, requests=requests, utils=utils)
