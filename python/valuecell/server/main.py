"""Main entry point for ValueCell Learning Path Backend."""

import uvicorn

from valuecell.server.api.app import create_app

def main():
    """Start the server."""
    app = create_app()
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
    )

if __name__ == "__main__":
    main()
