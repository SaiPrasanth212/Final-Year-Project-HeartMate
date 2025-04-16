import sys
import os

# Add your project directory to the sys.path
project_home = '/home/SaiPrasanth212/Project'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Set environment variable
os.environ['SESSION_SECRET'] = 'cac52d33f8de3c7452525d0b02647ee3c186efc7'

# Import Flask app
from main import app as application
