"""Search server configuration."""

import pathlib

# Root of this application, useful if it doesn't occupy an entire domain
APPLICATION_ROOT = '/'

SEARCH_ROOT = pathlib.Path(__file__).resolve().parent.parent
DATABASE_FILENAME = SEARCH_ROOT/'search'/'var'/'wikipedia.sqlite3'

INDEX_API_URL = "http://localhost:8001/api/v1/hits/"
