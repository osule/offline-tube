from .config import configure_defaults
from .app import create_app

app = create_app(configure_defaults())
