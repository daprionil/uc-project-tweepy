import re
from typing import List

from matplotlib import pyplot as plt
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from wordcloud import WordCloud

from tweepy_project.domain.port import UtilsPort


class Utils(UtilsPort):
    def __init__(self) -> None:
        pass

    def generate_graphic(self, sentiments: List[str]) -> None:
        sentiment_counts = {
            "Positive": sentiments.count("Positive"),
            "Negative": sentiments.count("Negative"),
            "Neutral": sentiments.count("Neutral"),
        }
        # Grafica los resultados de análisis de sentimientos
        plt.bar(sentiment_counts.keys(), sentiment_counts.values())
        plt.xlabel("Sentiment")
        plt.ylabel("Count")
        plt.title("Sentiment Analysis Results")
        plt.show()

    def generate_positive_analythics(
        self, sentiments: List[str], tweets: List[str]
    ) -> None:
        positive_tweets = [
            tweets[i] for i in range(len(sentiments)) if sentiments[i] == "Positive"
        ]
        positive_text = " ".join(positive_tweets)
        wordcloud = WordCloud(width=800, height=400, background_color="black").generate(
            positive_text
        )
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        plt.show()

    def clean_text(self, text: str) -> str:
        stop_words = set(stopwords.words("spanish"))
        lemmatizer = WordNetLemmatizer()

        text = text.lower()
        text = re.sub(r"http\S+|www\S+", "", text)
        # Eliminar URLs
        text = re.sub(r"@\w+", "", text)
        # Eliminar menciones
        text = re.sub(r"#\w+", "", text)
        # Eliminar hashtags
        text = re.sub(r"[^a-zA-Záéíóúüñ\s]", "", text)
        # # Eliminar caracteres especiales
        words = text.split()
        words = [lemmatizer.lemmatize(word) for word in words if word not in stop_words]
        return " ".join(words)

    def clean_tweets(self, tweets: List[str]) -> List[str]:
        return [self.clean_text(tweet) for tweet in tweets]
