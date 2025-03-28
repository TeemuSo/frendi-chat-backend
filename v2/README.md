# Frendi Chat Backend (v2)

A FastAPI backend service for the Frendi Chat application that integrates with a GepZep knowledge graph and uses LLM for intelligent responses.

## System Architecture

### Overview
The Frendi Chat application consists of:
1. **Frontend**: User interface for sending/receiving messages
2. **Supabase Edge Functions**: Middleware for routing messages
3. **Backend FastAPI Service** (this repository): Core chat processing system
4. **GepZep Knowledge Graph**: External data source for contextual information

### Flow Diagram
```
User → Frontend UI → Supabase Edge Functions → FastAPI Backend → LLM + GepZep Knowledge Graph → Response back through the chain
```

## Components

### 1. Core API Layer
- FastAPI framework
- Authentication & authorization
- Rate limiting and security measures
- Health monitoring endpoints

### 2. Chat Processing Engine
- `/chat` endpoint implementation
- Request validation and formatting
- Response serialization
- Error handling for failed requests

### 3. LLM Integration
- OpenAI Agents integration (https://github.com/openai/openai-agents-python)
- Tool-calling architecture for dynamic knowledge retrieval
- Prompt engineering for optimal responses
- Model parameter configuration

### 4. GepZep Knowledge Graph Connection
- API client for GepZep
- Query optimization
- Caching strategy
- Error handling for failed retrievals

### 5. Demonstration Frontend
- Simple Streamlit application for testing the backend
- Message history display
- Easy-to-use chat interface
- Development-only (separate from production frontend)

## Implementation Plan

### Phase 1: Foundation (Week 1)
- [x] Project setup and virtual environment configuration
- [ ] Configure FastAPI with proper error handling and logging
- [ ] Add authentication middleware for secure connections
- [ ] Implement basic `/chat` endpoint structure
- [ ] Set up testing framework and initial tests
- [ ] Create Docker configuration for local development

### Phase 2: LLM Integration (Week 2)
- [ ] Integrate OpenAI Agents Python library
- [ ] Create agent definition with appropriate tools
- [ ] Implement tool-calling logic for the LLM
- [ ] Add prompt templates and conversation context management
- [ ] Write comprehensive tests for the LLM integration

### Phase 3: Knowledge Graph Connection (Week 3)
- [ ] Create GepZep client module
- [ ] Implement knowledge retrieval tools
- [ ] Add caching layer for frequent queries
- [ ] Design fallback mechanisms for failed retrievals
- [ ] Test integration with sample knowledge graphs

### Phase 4: Streamlit Demo Interface (Week 4)
- [ ] Create simple Streamlit application 
- [ ] Implement chat UI with message history
- [ ] Add configuration options for testing different scenarios
- [ ] Connect to backend API endpoints
- [ ] Style the interface for better usability

### Phase 5: Deployment & Optimization (Week 5)
- [ ] Finalize Render.com deployment configuration
- [ ] Implement performance optimization
- [ ] Add monitoring and analytics
- [ ] Complete documentation
- [ ] Security audit and final testing

## Technical Specifications

### API Endpoints

#### Chat Endpoint
```
POST /chat
```

Request Body:
```json
{
  "user_id": "string",
  "message": "string",
  "conversation_id": "string (optional)",
  "metadata": {
    "additional_info": "any (optional)"
  }
}
```

Response Body:
```json
{
  "response": "string",
  "sources": [
    {
      "title": "string",
      "url": "string (optional)",
      "content_snippet": "string (optional)"
    }
  ],
  "metadata": {
    "tokens_used": "integer",
    "knowledge_graph_accessed": "boolean",
    "processing_time": "float (seconds)"
  }
}
```

### Environment Variables
```
OPENAI_API_KEY=your_openai_api_key
GEPZEP_API_KEY=your_gepzep_api_key
GEPZEP_API_URL=your_gepzep_api_url
DEBUG=true/false
PORT=8000
```

### Dependencies
- Python 3.11+
- FastAPI
- Pydantic
- OpenAI Agents Python
- GepZep Client (to be developed)
- Streamlit (for demo UI)
- Pytest (for testing)
- Docker (for containerization)

## Project Structure
```
frendi-chat-backend/
├── app/
│   ├── __init__.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── chat.py           # Chat endpoint implementation
│   │   └── healthcheck.py    # Health monitoring endpoints
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py         # Application configuration
│   │   └── security.py       # Auth and security functions
│   ├── llm/
│   │   ├── __init__.py
│   │   ├── agent.py          # OpenAI Agent implementation
│   │   ├── prompts.py        # Prompt templates
│   │   └── tools.py          # LLM tool definitions
│   ├── knowledge/
│   │   ├── __init__.py
│   │   ├── gepzep.py         # GepZep client
│   │   └── cache.py          # Caching mechanisms
│   └── models/
│       ├── __init__.py
│       ├── chat.py           # Pydantic models for chat
│       └── responses.py      # Pydantic models for responses
├── streamlit/
│   ├── __init__.py
│   ├── app.py                # Streamlit demo application
│   └── utils.py              # Helper functions for the demo
├── tests/
│   ├── __init__.py
│   ├── conftest.py           # Test configuration
│   ├── test_api.py           # API endpoint tests
│   ├── test_llm.py           # LLM integration tests
│   └── test_knowledge.py     # Knowledge graph tests
├── main.py                   # Application entry point
├── Dockerfile                # Docker configuration
├── docker-compose.yml        # Docker Compose for local dev
├── requirements.txt          # Python dependencies
├── .env.example              # Example environment variables
├── .gitignore                # Git ignore file
├── render.yaml               # Render.com deployment config
└── README.md                 # Project documentation
```

## Setup Instructions

### Local Development

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

5. Update the `.env` file with your API keys and configuration.

6. Run the development server:
```bash
uvicorn main:app --reload
```

7. For the Streamlit demo:
```bash
cd streamlit
streamlit run app.py
```

### Docker Setup

1. Build and run with Docker Compose:
```bash
docker-compose up --build
```

2. Access the API at http://localhost:8000 and the Streamlit demo at http://localhost:8501

## Testing

Run tests with pytest:
```bash
pytest
```

For specific test files:
```bash
pytest tests/test_api.py
```

## Deployment to Render.com

1. Push your code to a GitHub repository

2. Create a new Web Service on Render.com

3. Connect your GitHub repository

4. Render will automatically detect the `render.yaml` configuration

5. Set the required environment variables in the Render dashboard

6. Deploy the service

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

MIT 