# Fast-api

## Description
Fast-api is a high-performance web framework for building APIs with Python 3.6+ based on standard Python type hints. The key features are:
- Fast: Very high performance, on par with NodeJS and Go (thanks to Starlette and Pydantic).
- Fast to code: Increase the speed to develop features by about 200% to 300%.
- Fewer bugs: Reduce about 40% of human (developer) induced errors.
- Intuitive: Great editor support. Completion everywhere. Less time debugging.
- Easy: Designed to be easy to use and learn. Less time reading docs.
- Short: Minimize code duplication. Multiple features from each parameter declaration. Fewer bugs.
- Robust: Get production-ready code. With automatic interactive documentation.
- Standards-based: Based on (and fully compatible with) the open standards for APIs: OpenAPI and JSON Schema.

## Installation
To install Fast-api, you need to have Python 3.6 or above installed. You can install Fast-api using pip:
```bash
pip install fastapi
```
You will also need an ASGI server, for production such as `uvicorn`:
```bash
pip install "uvicorn[standard]"
```

To install Streamlit and scikit-learn, you can use pip:
```bash
pip install streamlit scikit-learn
```

## Usage
Here's a simple example of how to use Fast-api:
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
```
To run the example, use the following command:
```bash
uvicorn main:app --reload
```
This will start a server at `http://127.0.0.1:8000` with the interactive API documentation available at `http://127.0.0.1:8000/docs`.

To run the Streamlit app, use the following command:
```bash
streamlit run app.py
```
This will start a Streamlit server at `http://localhost:8501` where you can interact with the ML model and see the predictions.
