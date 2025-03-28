from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from chat.router import router as chat_router

app = FastAPI(
    title="Frendi Chat Backend",
    description="Backend service for Frendi Chat application with LLM and GepZep integration",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(chat_router)

@app.get("/")
async def root():
    return {"message": "Welcome to Frendi Chat Backend API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"} 