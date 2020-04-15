import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate('service.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://pondok-f2805.firebaseio.com/',
    'storageBucket': 'pondok-f2805.appspot.com'
})