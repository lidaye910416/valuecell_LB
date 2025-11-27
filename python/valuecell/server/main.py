"""Main entry point for ValueCell Learning Path Backend."""

import uvicorn

from valuecell.server.api.app import create_app

def main():
    """Start the server."""
    app = create_app()
    uvicorn.run(
        "valuecell.server.api.app:create_app",
        host="0.0.0.0",
        port=8000,
        reload=True, # Enable auto-reload for development
    )

if __name__ == "__main__":
    main()
