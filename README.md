Machine Learning Algorithms with Flask Deployment

This repository contains implementations of various Machine Learning algorithms along with a Flask-based API for easy deployment and inference.

Features

Implementation of multiple ML algorithms

REST API built using Flask for model inference

Preprocessing and feature engineering scripts

Instructions for running the project locally and deploying it on the cloud
Poetry for dependency management

Installation

Clone the repository:

git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

Create and activate a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

or use poetry 

poetry shell

Install dependencies using Poetry:

poetry install

Activate the virtual environment:

Usage

Running the Flask API

Train the model (if not already trained):

python train.py --- See respective folder as name can be different for different algorithms.

Start the Flask server:

python app.py

Make API requests to test the model:

curl -X POST "http://127.0.0.1:5000/predict" -H "Content-Type: application/json" -d '{"input_data": [your_input_values]}'


Cloud Deployment

The project can be deployed on platforms like AWS, GCP, or Heroku.

More deployment instructions will be added soon.

Project Structure

.
├── app.py              # Flask API
├── train.py            # Model training script
├── model.pkl           # Saved model file
├── static/             # Static files (if any)
├── templates/          # HTML templates (if needed for UI)
├── pyproject.toml      # Poetry configuration file
├── poetry.lock         # Poetry lock file
├── Dockerfile          # Docker setup
├── README.md           # Project documentation
└── .gitignore          # Git ignore file

Contributing

Feel free to fork this repository, create a new branch, and submit a pull request. Suggestions and improvements are welcome!
