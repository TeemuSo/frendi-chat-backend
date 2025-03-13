# Frendi Chat Backend

A FastAPI backend service for the Frendi Chat application, deployable on Render.com.

## Features

- RESTful API with FastAPI
- Ready for deployment on Render.com
- Dockerized for easy containerization
- Sample message API endpoints

## Local Development

### Prerequisites

- Python 3.11+
- pip (Python package manager)

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/frendi-chat-backend.git
   cd frendi-chat-backend
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file (copy from `.env.example`):
   ```bash
   cp .env.example .env
   ```

5. Run the development server:
   ```bash
   uvicorn main:app --reload
   ```

6. Visit the API documentation at http://localhost:8000/docs

## API Endpoints

- `GET /` - Health check
- `GET /api/messages` - Get all messages
- `POST /api/messages` - Create a new message
- `GET /api/messages/{message_id}` - Get a specific message

## Deployment to Render.com

1. Push your code to a GitHub repository.

2. Create a new Web Service on Render.com.

3. Connect your GitHub repository.

4. Render will automatically detect the `render.yaml` configuration.

5. Click "Create Web Service" and your API will be deployed!

## Docker Usage

Build the Docker image:
```bash
docker build -t frendi-chat-backend .
```

Run the container:
```bash
docker run -p 8000:8000 -e PORT=8000 frendi-chat-backend
```

## Testing

Run tests with pytest:
```bash
pytest
```

## License

MIT 