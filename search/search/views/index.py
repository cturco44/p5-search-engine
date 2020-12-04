import flask
from flask import request, redirect, url_for
import requests
import search
import urllib
import pdb

@search.app.route("/", methods=["GET"])
def show_index():
    if request.method == "GET":
        q_string_param = request.args.get('q')
        w_decimal_param = request.args.get('w')

        #Person just wants page and hasn't made request
        if q_string_param is None and w_decimal_param is None:
            return flask.render_template("index.html",results=[],nothing=False)
        
        parameters = { 'w': w_decimal_param,'q': q_string_param}
        encoded_query = urllib.parse.urlencode(parameters)
        final_url = search.app.config["INDEX_API_URL"] + '?' + encoded_query + '/'
        response = requests.get(final_url)
        hits = response.json()


        connection = search.model.get_db()
        final = []
        if hits["hits"]:
            for i, item in enumerate(hits["hits"]):
                if i >= 10:
                    break
                cur = connection.execute(
                    """
                    SELECT * from Documents
                    WHERE docid = ?
                    """, [item["docid"]]
                )
                document = cur.fetchall()
                final.append(document[0])

        else:
            return flask.render_template("index.html", results=[], nothing=True)
        return flask.render_template("index.html",results=final,nothing=False)
        