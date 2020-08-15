import tweepy
import auth

key = tweepy.OAuthHandler(auth.apy_key, auth.api_secret_key)
key.set_access_token(auth.access_token, auth.access_token_secret)
api = tweepy.API(key)

def buscar_dados(valor):
    text = tweepy.Cursor(api.search, q=valor, lang='pt').items(3)
    response = []
    for twitter in text:
        response.append(twitter.text)
    return response


def limpar_dados(valor):
    lista = []
    for v in valor:
        x = v.replace('\n', '')
        lista.append(x)
    return lista



