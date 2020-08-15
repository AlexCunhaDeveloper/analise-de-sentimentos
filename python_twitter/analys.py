import auth
import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, SentimentOptions, KeywordsOptions, RelationsOptions


services = NaturalLanguageUnderstandingV1(
    version='2019-07-12',
    url= auth.urlaul,
    iam_apikey= auth.apikeyaul
    
)



def analise(texto):
    lista = []
    for t in texto:
        response =  services.analyze(text=t, language='pt',features=Features(
            sentiment=SentimentOptions()
        )).get_result()
        lista.append(response)
    return lista




    



