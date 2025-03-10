from django.shortcuts import render, redirect
import pyrebase
import json

firebase_config = {
    "apiKey": "AIzaSyBrm2OZhgEi5UF0hTr36t-X8CJ7jffc_z8",
    "authDomain": "test-24ea0.firebaseapp.com",
    "databaseURL": "https://test-24ea0-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "test-24ea0",
    "storageBucket": "test-24ea0.appspot.com",
    "messagingSenderId": "811829331453",
    "appId": "1:811829331453:web:12930831feba2f3a098594",
    "measurementId": "G-5EQ2SMHDSY"
}

try:
    print("\n=== Initializing Firebase ===")
    firebase = pyrebase.initialize_app(firebase_config)
    database = firebase.database()
    
    # Test database connection and print structure
    print("Testing database connection...")
    test_ref = database.child('Data').get()
    
    if test_ref.val():
        print("Database connection successful!")
        print("\nDatabase structure:")
        print(json.dumps(test_ref.val(), indent=2))
        print("\nAvailable keys:", list(test_ref.val().keys()))
    else:
        print("Database connection successful but no data found in 'Data' node")
        
except Exception as e:
    print(f"\nError connecting to Firebase: {str(e)}")
    raise e