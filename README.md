# Air Ticket Platform Example

This repository contains a small example of a flight booking service with a simple front end and a Flask back end. It demonstrates the overall architecture of an air ticket platform.

## Structure

- `backend/` – Flask application providing flight search, order creation and payment endpoints.
- `frontend/` – Minimal web page for searching flights.

## Setup

1. Install dependencies for the backend:

```bash
pip install -r backend/requirements.txt
```

2. Run the server:

```bash
python backend/app.py
```

3. Open `frontend/index.html` in your browser. By default the Flask server runs at `http://127.0.0.1:5000` and serves API requests for the front end.

This example uses in-memory data and mock payment handling. It is intended as a starting point for integrating real flight, payment and ticketing APIs.
