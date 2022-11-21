import tweepy
import csv
import time
import os
import pandas as pd

# Importar credenciales de usuario de twitter para acceder a la API

access_tweepy = pd.read_csv(r"C:\Users\vfizr\OneDrive\Documents\TFM\Login_twitter_API.csv")

consumer_key = access_tweepy["key"][0]
consumer_password = access_tweepy["key"][1]
access_token = access_tweepy["key"][2]
access_password = access_tweepy["key"][3]

authenticate = tweepy.OAuthHandler(consumer_key,consumer_password)
authenticate.set_access_token(access_token,access_password)

api = tweepy.API(authenticate)

#Se elimina el csv resultado de una iteracion anterior

try:
    os.remove('tweetsfinal1.csv')
except:
    print("El documento no existe")
    pass

#Se emplea el csv writer para almacenar los datos obtenidos

csvFile = open('tuits3.csv', 'w')

csvWriter = csv.writer(csvFile)

#Funcion buscador
data = tweepy.Cursor(api.search,q = "bitcoin",since = "2021-11-01",until="2021-11-27",lang = "en").items()


while True:
    try:
        tweet = data.next()
        
        if tweet.user.followers_count > 0: 
            #Comando completo para análisis en futuros trabajos:
            #csvWriter.writerow([tweet.user.name.encode('utf-8', errors='ignore'),tweet.user.followers_count,tweet.created_at, tweet.text.encode('utf-8', errors='ignore'),tweet.id])
            csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8', errors='ignore')])
            print("Tweet capturado")
    except tweepy.TweepError:
        print("Esperando")
        time.sleep(600)
        #En caso de que se alcancen el limite de request marcadas por la version estandar de la cuenta de Twitter se espera 10 minutos sin salir del bucle
        continue
    except StopIteration:
        print("¡CRASH!")
        break


csvFile.close()

#Resultados guardados en el directorio C:\Users\vfizr\Documents