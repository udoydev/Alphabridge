import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from core.wsgi import application

# Vercel expects a variable named 'app' or a function named 'handler'
app = application
