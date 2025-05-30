from typing import List

from tweepy import Client

from ..domain.port import RequestAdapterPort


class RequestAdapter(RequestAdapterPort):
    client: Client

    def __init__(self, client: Client) -> None:
        self.client = client

    def get_tweets(self, query: str, max_results: int) -> List[str]:
        # client.search_recent_tweets(
        #     query=query,
        #     max_results=max_results,
        #     tweet_fields=["lang", "created_at", "text"],
        # )
        # tweets_list = []
        # Comentado solo porque la API no deja hacer peticiones de manera continua
        # for tweet in tweets.data:
        #     tweets_list.append(tweet.text)

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

        return tweets_list
