# Fast-api

## Project Description

This project demonstrates how to build a machine learning model using FastAPI. FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints. In this project, we will create a simple machine learning model and expose it via a FastAPI server.

## Setup and Run FastAPI Server

1. Clone the repository:
   ```bash
   git clone https://github.com/varun2388/Fast-api.git
   cd Fast-api
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

The server will be running at `http://127.0.0.1:8000`.

## Using the Machine Learning Model

1. Make a POST request to the `/predict` endpoint with the input data in JSON format. For example:
   ```bash
   curl -X 'POST' \
     'http://127.0.0.1:8000/predict' \
     -H 'accept: application/json' \
     -H 'Content-Type: application/json' \
     -d '{
     "feature1": value1,
     "feature2": value2,
     ...
   }'
   ```

2. The server will respond with the prediction result in JSON format.
