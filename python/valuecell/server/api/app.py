"""FastAPI application factory."""

from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware



def create_app() -> FastAPI:
    """Create and configure FastAPI application."""
    
    @asynccontextmanager
    async def lifespan(app: FastAPI):
        # Startup
        print("ValueCell Learning Path Server starting up...")
        yield
        # Shutdown
        print("Server shutting down...")

    app = FastAPI(
        title="ValueCell Learning Path API",
        description="Learning backend for financial multi-agent system",
        version="0.1.0",
        lifespan=lifespan,
        docs_url="/docs",
        redoc_url="/redoc",
    )

    # CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Basic routes
    @app.get("/")
    async def home_page():
        return {"message": "Welcome to ValueCell Learning Path API"}

    @app.get("/health")
    async def health_check():
        return {"status": "healthy"}
    
    

    return app
