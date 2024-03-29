from flask import Flask, request, render_template
from pymongo import MongoClient
from urllib.parse import quote_plus

app = Flask(__name__)

# Escape special characters in username and password
username = quote_plus('dora')
password = quote_plus('Dora@123')

# Connect to MongoDB Atlas
client = MongoClient(f'mongodb+srv://{username}:{password}@doradb.4prru5z.mongodb.net/')
db = client['photo_database']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/capture_photo', methods=['POST'])
def capture_photo():
    photo_data = request.json['photo']
    ip_address = request.remote_addr
    # Save photo data and IP address to MongoDB
    db.photos.insert_one({'photo': photo_data, 'ip_address': ip_address})
    return 'Photo captured successfully!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
