import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import asyncio

async def conected_firebase():
    cred_obj = credentials.Certificate("config/thienchu-ea472-firebase-adminsdk-fbsvc-564cf81652.json")
    
  
    if not firebase_admin._apps:
        firebase_admin.initialize_app(cred_obj, {
            'databaseURL': "https://thienchu-ea472-default-rtdb.firebaseio.com/"
        })
    
    print("Firebase connected successfully")