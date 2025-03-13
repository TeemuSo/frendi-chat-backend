# Frendi Chat Backend

A FastAPI backend service for the Frendi Chat application, deployable on Render.com.

# Frendi outline
## Chat interface
Users can send messages to a chatbot. The chatbot has access to the user's GepZep knowledge graph.

The flow:
1. User sends a message
2. Message is sent to Supabase Edge functions
3. Supabase Edge function calls Render.com FastAPI /chat endpoint
4. The /chat endpoint has LLM, that fetches information from gepZep knowledge graph if needed
5. The FastAPI endpoint returns the response back to Edge function, which returns it to interface

The LLM:
We should try using new https://github.com/openai/openai-agents-python
1. The agent checks "does the user question need background information from knowledge graph?"
2. If yes, it queries getZep knowledge graph
3. If no, it responds normally

Basically, the agent has to have a set of tools it can use, and it calls them automatically. 

**To understand**: you should understand how LLM tool calling works and how LLM structured responses work. For now, we don't have to do any streaming but just return the response when it's needed.


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