"""Index package initializer."""
import flask
from index.utils import stopwords, pagerank, inverted_index
# app is a single object used by all the code modules in this package
app = flask.Flask(__name__)  # pylint: disable=invalid-name

import index.api  # noqa: E402  pylint: disable=wrong-import-position
