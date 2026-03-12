from backend.app import create_app

# Vercel expects the WSGI/ASGI callable to be named `app` or `handler`.
# We create it once so the serverless runtime can invoke it.
app = create_app()
