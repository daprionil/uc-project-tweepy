from typing import List

from nltk.sentiment import SentimentIntensityAnalyzer

from tweepy_project.domain.port import AnalizerPort


class AnalizerAdapter(AnalizerPort):
    sia: SentimentIntensityAnalyzer

    def __init__(self, sia: SentimentIntensityAnalyzer) -> None:
        self.sia = sia

    def give_sentiments(self, tweets: List[str]):
        # Analiza el sentimiento de cada tweet
        sentiments = [self.sia.polarity_scores(tweet) for tweet in tweets]

        # Clasifica los sentimientos
        sentiment_labels = [
            "Positive"
            if sentiment["compound"] > 0.05
            else "Negative"
            if sentiment["compound"] < -0.05
            else "Neutral"
            for sentiment in sentiments
        ]
        return sentiment_labels
