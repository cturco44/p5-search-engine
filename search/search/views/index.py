import flask
from flask import request, redirect, url_for
import requests
import search
import pdb

@search.app.route("/", methods=["GET"])
def show_index():
    if request.method == "GET":
        q_string_param = request.args.get('q')
        w_decimal_param = request.args.get('w')

        #Person just wants page and hasn't made request
        if q_string_param is None and w_decimal_param is None:
            return flask.render_template("index.html",results=[],nothing=False)
        
        # parameters = {'q': q_string_param, 's': w_decimal_param}
        # hits = requests.get("/api/v1/hits/", params=parameters)
        
        # TODO: Remove hardcoded array and convert hits to dict
        # hits = {
        #     "hits": []
        # }
        hits = {
            "hits": [
                {
                    "docid": 23154957,
                    "score": 0.06573732
                },
                {
                    "docid": 3957342,
                    "score": 0.06573732
                },
                {
                    "docid": 32841952,
                    "score": 0.06573732
                },
                {
                    "docid": 46790,
                    "score": 0.06573732
                },
                {
                    "docid": 367154,
                    "score": 0.06573732
                },
                {
                    "docid": 634802,
                    "score": 0.06573732
                },
                {
                    "docid": 1329192,
                    "score": 0.06573732
                },
                {
                    "docid": 1757140,
                    "score": 0.06573732
                },
                {
                    "docid": 1191599,
                    "score": 0.06573732
                },
                {
                    "docid": 27593182,
                    "score": 0.06573732
                },
                {
                    "docid": 8783748,
                    "score": 0.06573732
                },
                {
                    "docid": 20994373,
                    "score": 0.06573732
                }
                
            ]
        }
        # Generate SQL query for posts in order
        #pdb.set_trace()
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
        