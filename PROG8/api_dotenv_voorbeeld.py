# Requests voor het versturen van HTTP verzoeken
import requests

# Hulp library voor JSON
import json

# Importeer dotenv om API key te beschermen
from dotenv import load_dotenv
import os

# Bee movie ID
beemovie = "tt0389790"

# Load environment variables from the .env file (if present)
load_dotenv()

# Laad de API key via de OS library
apikey = os.getenv('API_KEY')
print(f'API key length: {len(apikey)}')

# Bouw de URI op
uri = f"https://www.omdbapi.com/?i={beemovie}&apikey={apikey}"

# Voer het verzoek uit
r = requests.get(uri)

# Ging het verzoek goed?
if r.status_code == 200:
    print("Verzoek ging goed!")
    print(json.dumps(r.json(), indent=4))
else:
    print(f"Verzoek is niet gelukt met status code {r.status_code}.")


