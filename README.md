# City Metrics Tracker
This application allows users to track various metrics for different cities within the hospitality industry. It includes both frontend and backend components to visualize and manage data stored in a MongoDB database.


### Frontend
The frontend of the application is built using React and utilizes various chart components from react-chartjs-2 to display metrics for net sale, net expense, and target remaining by city.

Prerequisites
Node.js
npm (Node Package Manager)

#### Running the Frontend Locally
Extract the content of The Zip file 

Navigate to the frontend directory:
cd frontend
Install dependencies:
npm install

Start the development server:
npm start
Access the application at http://localhost:3000 in your web browser.

### Backend
The backend of the application is built using Flask, providing endpoints to fetch data from a MongoDB database based on specified parameters.

Prerequisites
Python (3.6 or higher)
Flask
pymongo
Flask-CORS
Running the Backend Locally
Ensure you have Python installed on your machine.

Install dependencies using pip:

pip install Flask pymongo flask-cors

Navigate to the backend directory:

cd backend

Run the Flask application:

python app.py
T
he backend server should now be running at http://localhost:5000.

API Endpoints
GET /data: Fetches data for a specified city for the past 15 days.
Parameters:
city: The name of the city for which data is requested.
Response:
Success: Returns JSON data containing metrics for the specified city.
Error: Returns JSON error message if any issue occurs during data retrieval.
Note
Ensure that the MongoDB connection string is correctly configured in the backend code (app.py). Also, make sure the MongoDB server is running and accessible from the backend application.
