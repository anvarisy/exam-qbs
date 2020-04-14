import pyrebase
import firebase_admin
from firebase_admin import credentials


config = {
  "apiKey": "AIzaSyCnZeerLoQP-hPRYdH6dnVqysNRrMwhpPg",
  "authDomain": "qbs-exam.firebaseapp.com",
  "databaseURL": "https://qbs-exam.firebaseio.com/",
  "storageBucket": "qbs-exam.appspot.com",
  "serviceAccount": "service.json"
}

firebase = pyrebase.initialize_app(config)


cred = credentials.Certificate('service.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://qbs-exam.firebaseio.com/',
    'storageBucket': 'qbs-exam.appspot.com'
})
