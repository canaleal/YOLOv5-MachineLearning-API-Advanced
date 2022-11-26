from datetime import datetime
import firebase_admin
from firebase_admin import credentials, firestore
import os
from dotenv import load_dotenv
load_dotenv()
GOOGLE_APPLICATION_CREDENTIALS_PATH = os.getenv('GOOGLE_APPLICATION_CREDENTIALS_PATH')

class GoogleFirebase:

    db = None
    user_id = None
    collection_ref = None
    geojsonData = None


    def __init__(self):
        raw_credentials = credentials.Certificate(GOOGLE_APPLICATION_CREDENTIALS_PATH)
        firebase_admin.initialize_app(raw_credentials,
                                      {
                                          'databaseURL': 'https://Capstone.firebaseio.com/'
                                      })
        self.db = firestore.client()
       
        
    def set_user_id(self, user_id):
         self.user_id = user_id

    def get_firebase_users_geojson_collection(self):
        user_collections = self.db.collection('users')
        user_document = user_collections.document(self.user_id)
        self.collection_ref = user_document.collection('geojson')


    def save_geojson_to_user_collection(self, file_id, geojson_data):
        self.collection_ref.document(file_id).set(geojson_data)
        

