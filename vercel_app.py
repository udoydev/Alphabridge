from core.wsgi import application

# Vercel serverless function handler
def handler(request, context):
    return application(request.environ, context)
