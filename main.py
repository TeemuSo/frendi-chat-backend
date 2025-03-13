from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
import uvicorn
from app.api import router as api_router
from app.config import settings

# Initialize FastAPI app
app = FastAPI(
    title=settings.APP_NAME,
    description=settings.APP_DESCRIPTION,
    version=settings.APP_VERSION,
    debug=settings.DEBUG
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins in development
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Add routers
app.include_router(api_router)

@app.get("/")
async def root():
    """Health check endpoint."""
    return {"status": "ok", "message": f"{settings.APP_NAME} is running"}

if __name__ == "__main__":    
    # Run the application
    uvicorn.run("main:app", host="0.0.0.0", port=settings.PORT, reload=settings.DEBUG) 