#Importamos librerias
import tweepy

class TweetsListener(tweepy.StreamListener):
  #Metodos
  def on_conected(self):
    print("EstoyConectado")
  
  def on_status(self,status):
    print(status.text)

  def on_error(self,status_code):  
    print("Error",status_code)

#declaramos variables de configuracion
consumer_key = "K4w3BdA2256jIKBpYBjHISM8L"
consumer_secret = "681Rjqm0Nw9coNoxPLlqDMASEZQ96TPPph5UqRBJlVhzWZRLEk"
acces_token = "377174771-c6YHNTRNlHDeb7oW4hlAI0uO30vJKrdC2rmzcNCx"
acces_token_secret = "WyJgZLs69RzdqxYbgiScBRp9kIRjte1nLmvm1b2ab62R2"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(acces_token,acces_token_secret)

api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

stream = TweetsListener()
streamingApi = tweepy.Stream(auth = api.auth,listener= stream)
streamingApi.filter(locations=[-74.1640501996,4.5911360274,-74.1562825223,4.597531256])