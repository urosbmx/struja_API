import firebase_admin
from firebase_admin import credentials, firestore

import web_scraping
from latin_converter import CharactersMapper


# Initialize Firebase Admin SDK
cred = credentials.Certificate('api-firebase.json')
firebase_admin.initialize_app(cred)

# Initialize Firestore DB
db = firestore.client()

# Read JSON data from file or directly

test = web_scraping.Web_scraping()
data = test.web_scraping(0)
headers = data[0]
translated_responses = CharactersMapper.translate_responses(data)
convert_head = CharactersMapper.header_convert(headers)
json_data = [dict(zip(convert_head, row)) for row in translated_responses[1:]]

# Upload data to Firestore
for i, entry in enumerate(json_data):
    db.collection('Belgrade').document(f'document_{i}').set(entry)