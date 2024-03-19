import requests as req
import Settings
import json

#Utforsk 1

def hent_film_info(tittel):

    "Henter informasjon om film"

    api_key = Settings.API_KEY
    api_url = f"https://www.omdbapi.com/?apikey={api_key}&t={tittel}" 
    #Henter url-en til data som inneholder tittel som er definert

    response = req.get(api_url) #Henter data fra url-en

    if response.status_code == 200:
        film_data = response.json() #Gjør data om til JSON-format
        if film_data["Response"] == "False": #Sjekker om vi har respons i server
            print(film_data["Error"]) 
            return None
        return film_data
    
if __name__=="__main__":

    print(hent_film_info("Star Wars: Episode III"))

