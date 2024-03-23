# App Initialization
from . import create_app # from __init__ file

app = create_app()

# Hello World!
@app.route('/')
def hello():
    return "Hello World!"

# Tasks
from .tasks import urls

if __name__ == "__main__":
    app.run()