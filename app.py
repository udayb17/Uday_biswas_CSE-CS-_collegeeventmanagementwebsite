from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Allow cross-origin if needed

# Dummy database (in-memory)
events = [
    {
        'id': 1,
        'title': 'Annual Tech Fest',
        'date': 'April 10, 2025',
        'location': 'College Auditorium',
        'description': 'Join us for a day of workshops, talks, and exhibitions showcasing the latest in technology!',
         'imageUrl': 'https://images.pexels.com/photos/2582937/pexels-photo-2582937.jpeg'
    },
    {
        'id': 2,
        'title': 'Sports Day',
        'date': 'May 5, 2025',
        'location': 'College Sports Ground',
        'description': 'Prepare for a day full of athletic competitions, team spirit, and healthy competition!',
         'imageUrl': 'https://images.pexels.com/photos/3621104/pexels-photo-3621104.jpeg'
    },
    {
        'id': 3,
        'title': 'Cultural Festival',
        'date': 'June 15, 2025',
        'location': 'College Grounds',
        'description': 'A day of dance, music, food, and celebration of cultural diversity!',
         'imageUrl': 'https://images.pexels.com/photos/2263436/pexels-photo-2263436.jpeg'
    }
]

team_members = [
    {
        'id': 1,
        'name': 'Aman Singh',
        'role': 'Event Manager',
        #'imageUrl': 'https://images.pexels.com/photos/2379004/pexels-photo-2379004.jpeg'
    },
    {
        'id': 2,
        'name': 'Uday Biswas',
        'role': 'Marketing Head',
        #'imageUrl': 'https://images.pexels.com/photos/2182970/pexels-photo-2182970.jpeg'
    },
    {
        'id': 3,
        'name': 'Abhisekh Maurya',
        'role': 'Logistics Coordinator',
        #'imageUrl': 'https://images.pexels.com/photos/2681751/pexels-photo-2681751.jpeg'
    }
]

@app.route('/')
def home():
    return app.send_static_file('home.html')

@app.route('/events', methods=['GET'])
def get_events():
    return jsonify(events)

@app.route('/team', methods=['GET'])
def get_team():
    return jsonify(team_members)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    print(f'Login attempt: {email}, {password}')
    return jsonify({'message': 'Login attempt received'}), 200

@app.route('/create-event', methods=['POST'])
def create_event():
    data = request.get_json()
    new_event = {
        'id': len(events) + 1,
        'title': data.get('title'),
        'date': data.get('date'),
        'location': data.get('location'),
        'description': data.get('description'),
        'imageUrl': data.get('imageUrl')
        
    }
    events.append(new_event)
    return jsonify({
        'message': 'Event created successfully!',
        'event': new_event
    }), 201

@app.route('/contact', methods=['POST'])
def contact():
    data = request.get_json()
    print('Contact form received:', data)
    return jsonify({'message': 'Message sent successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True, port=8080)