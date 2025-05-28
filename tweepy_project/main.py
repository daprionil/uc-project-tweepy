import functools
import re
from typing import Any, List

import nltk
import tweepy
from environment import environment
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.stem import WordNetLemmatizer

nltk.download("stopwords")
nltk.download("wordnet")
nltk.download("vader_lexicon")

bearer_token = environment.__getitem__("bearer_token")

client = tweepy.Client(bearer_token=bearer_token, wait_on_rate_limit=True)

sia = SentimentIntensityAnalyzer()


@functools.lru_cache()
def get_tweets(
    query: str,
    max_results: int,
) -> Any:
    return client.search_recent_tweets(
        query=query,
        max_results=max_results,
        tweet_fields=["lang", "created_at", "text"],
    )


def clean_text(text: str) -> str:
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


def clean_tweets(tweets: List[str]) -> List[str]:
    return [clean_text(tweet) for tweet in tweets]


# query = "#react lang:es"

# tweets = get_tweets(query, 10)
# ['RT @AikawaOficial: REACT | SOL DIVINO - Lorde Escanor (Nanatsu no Taizai) | Gabriza &amp; Anny - Orgulho ft. @blxckoficial\n@Gabrizaoficial @ann…', 'Dulce Boludo Kaprichoso Bajo El Mar Mágico 🙈🦆🪽🏃😅👉👈❤️🇦🇷🏍️💎🇪🇨🥂😂🔥🐍🏍️💎👑⏳♥️😇🙏🌈💪 CORAZÓN TURCO 🇹🇷💕 #mar #agua #aqua #mermaid  #indio #react #argentina🇦🇷 #funkbrasil #ecuador🇪🇨 #turquia #turco #drama #love #romance #foryou #show #ecuador #guayaquil #world #views #new https://t.co/CwzkYhDANR', 'Carros japoneses? Temos\nYoutube: \nhttps://t.co/X0DhITQ9L4\n #Vtuber #Youtube  #gameplay #react #Vtubing #ENVtuber', '🚀 Estoy desarrollando un aula virtual especializada para el seguimiento de prácticas profesionalizantes en mi instituto.\nEsta es mi primera experiencia trabajando en un proyecto que tendrá un impacto real.\nTe cuento cómo lo estoy construyendo\n#dev #nodejs #react #mysql', 'Esta es la realidad de #zazza el #italiano en #chile es tremendo su trabajo #react https://t.co/kM00MLulQB', 'Introducción al desarrollo web con @plone #Seven y #React 👩\u200d💻 #javascript #Python #BeethovenSprint #CMS #Plone https://t.co/04OmIFgIaU', 'Una pequeña app hecha en Gemini. \nIndicadores económicos. \n\ny nada mas ni nada menos que "Desarrollado con React y Tailwind CSS." 🤔\n\n#React #CSS \n\nhttps://t.co/c41YZrioyg', '3 cosas que mejoran cualquier UI con React:\n✅ Loading states claros\n✅ Animaciones sutiles\n✅ Layouts responsivos bien pensados\n¡Y si le sumás Tailwind y buenas prácticas, vuela! 🚀\n#React #TailwindCSS #FrontendTips https://t.co/yqV9cSJv4d', 'Que Hermoso Es Saber Que Todo Pasa Por Algo 🥹👉👈♥️🤣❤️🇦🇷🥂🇪🇨 Es Rico Volver A Levantarse 💪💊🔪😭🍌📷👃⏳🪽🦆🙈🇨🇴🍀🐍🏍️💎👑🌈🏃😅🐸🔥😂🙏😇🥂🇪🇨🇦🇷❤️👉👈♥️🥹 CORAZÓN TURCO 🇹🇷💕 #wepray #tini #tinistoessel #indio #react #argentina🇦🇷 #funkbrasil #ecuador🇪🇨 #turquia #turco #drama https://t.co/WCPngArUwi', 'traumas Que No Eh Superado 😅😭🥂🔪❤️🤣😂👉👈♥️ Jajaja 💊🐸💪👃📷No Estaba Roto , No Estaba Loco Vos Me Hiciste Asi⏳🪽🌈🥂🔥👑💎🏍️🐍🇦🇷🍀🇨🇴🙈🦆🏃😅😇♥️🥹🔥 CORAZÓN TURCO 🇹🇷💕 #tumehicisteasi #marrendon @Mar Rendón #indio #react #argentina🇦🇷 #funkbrasil #ecuador🇪🇨 #turquia #turco https://t.co/H0Qwf6Cw4J']

tweets_list: List[str] = [
    "RT @AikawaOficial: REACT | SOL DIVINO - Lorde Escanor (Nanatsu no Taizai) | Gabriza &amp; Anny - Orgulho ft. @blxckoficial\n@Gabrizaoficial @ann…",
    "Dulce Boludo Kaprichoso Bajo El Mar Mágico 🙈🦆🪽🏃😅👉👈❤️🇦🇷🏍️💎🇪🇨🥂😂🔥🐍🏍️💎👑⏳♥️😇🙏🌈💪 CORAZÓN TURCO 🇹🇷💕 #mar #agua #aqua #mermaid  #indio #react #argentina🇦🇷 #funkbrasil #ecuador🇪🇨 #turquia #turco #drama #love #romance #foryou #show #ecuador #guayaquil #world #views #new https://t.co/CwzkYhDANR",
    "Carros japoneses? Temos\nYoutube: \nhttps://t.co/X0DhITQ9L4\n #Vtuber #Youtube  #gameplay #react #Vtubing #ENVtuber",
    "🚀 Estoy desarrollando un aula virtual especializada para el seguimiento de prácticas profesionalizantes en mi instituto.\nEsta es mi primera experiencia trabajando en un proyecto que tendrá un impacto real.\nTe cuento cómo lo estoy construyendo\n#dev #nodejs #react #mysql",
    "Esta es la realidad de #zazza el #italiano en #chile es tremendo su trabajo #react https://t.co/kM00MLulQB",
    "Introducción al desarrollo web con @plone #Seven y #React 👩\u200d💻 #javascript #Python #BeethovenSprint #CMS #Plone https://t.co/04OmIFgIaU",
    'Una pequeña app hecha en Gemini. \nIndicadores económicos. \n\ny nada mas ni nada menos que "Desarrollado con React y Tailwind CSS." 🤔\n\n#React #CSS \n\nhttps://t.co/c41YZrioyg',
    "3 cosas que mejoran cualquier UI con React:\n✅ Loading states claros\n✅ Animaciones sutiles\n✅ Layouts responsivos bien pensados\n¡Y si le sumás Tailwind y buenas prácticas, vuela! 🚀\n#React #TailwindCSS #FrontendTips https://t.co/yqV9cSJv4d",
    "Que Hermoso Es Saber Que Todo Pasa Por Algo 🥹👉👈♥️🤣❤️🇦🇷🥂🇪🇨 Es Rico Volver A Levantarse 💪💊🔪😭🍌📷👃⏳🪽🦆🙈🇨🇴🍀🐍🏍️💎👑🌈🏃😅🐸🔥😂🙏😇🥂🇪🇨🇦🇷❤️👉👈♥️🥹 CORAZÓN TURCO 🇹🇷💕 #wepray #tini #tinistoessel #indio #react #argentina🇦🇷 #funkbrasil #ecuador🇪🇨 #turquia #turco #drama https://t.co/WCPngArUwi",
    "traumas Que No Eh Superado 😅😭🥂🔪❤️🤣😂👉👈♥️ Jajaja 💊🐸💪👃📷No Estaba Roto , No Estaba Loco Vos Me Hiciste Asi⏳🪽🌈🥂🔥👑💎🏍️🐍🇦🇷🍀🇨🇴🙈🦆🏃😅😇♥️🥹🔥 CORAZÓN TURCO 🇹🇷💕 #tumehicisteasi #marrendon @Mar Rendón #indio #react #argentina🇦🇷 #funkbrasil #ecuador🇪🇨 #turquia #turco https://t.co/H0Qwf6Cw4J",
]

# Comentado solo porque la API no deja hacer peticiones de manera continua
# for tweet in tweets.data:
#     tweets_list.append(tweet.text)

tweets = clean_tweets(tweets_list)

# Analiza el sentimiento de cada tweet
sentiments = [sia.polarity_scores(tweet) for tweet in tweets]

# Clasifica los sentimientos
sentiment_labels = [
    "Positivo"
    if sentiment["compound"] > 0.05
    else "Negativo"
    if sentiment["compound"] < -0.05
    else "Neutro"
    for sentiment in sentiments
]

print(sentiment_labels)
