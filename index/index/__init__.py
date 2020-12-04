"""Index package initializer."""
import flask

# app is a single object used by all the code modules in this package
app = flask.Flask(__name__)  # pylint: disable=invalid-name

from index.utils import stopwords, pagerank, inverted_index
import index.api  # noqa: E402  pylint: disable=wrong-import-position
