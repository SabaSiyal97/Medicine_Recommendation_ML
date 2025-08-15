from waitress import serve # type: ignore
from main import app  # Replace 'app' with your file name if not 'app.py'

serve(app, host='0.0.0.0', port=8080)