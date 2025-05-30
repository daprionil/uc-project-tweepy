import nltk
import tweepy
from environment import environment
from infrastructure.analizer import AnalizerAdapter
from infrastructure.requests import RequestAdapter
from infrastructure.utils import Utils
from nltk.sentiment import SentimentIntensityAnalyzer
from tweepy import Client

from tweepy_project.application.app import App

# Descarga las dependencias de nltk
nltk.download("stopwords")
nltk.download("wordnet")
nltk.download("vader_lexicon")

# Instanciación de sentimiento
sia = SentimentIntensityAnalyzer()

# Token - Variable de entorno
bearer_token = environment.__getitem__("bearer_token")

# Crea la instancia de tweepy API
client: Client = tweepy.Client(bearer_token=bearer_token, wait_on_rate_limit=True)

# Genera la instanciación de los Adaptadores
analizer = AnalizerAdapter(sia)
requests = RequestAdapter(client)
utils = Utils()

app = App(analizer=analizer, requests=requests, utils=utils)
app()
