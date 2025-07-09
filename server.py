from http.server import BaseHTTPRequestHandler, HTTPServer
import os
from urllib.parse import urlparse, parse_qs
import json

from is_meaning_similar import is_meaning_similar


# creating a class for handling
# basic Get and Post Requests
class GFG(BaseHTTPRequestHandler):

    # creating a function for Get Request
    def do_GET(self):
        params = parse_qs(urlparse(self.path).query)
        p1 = params.get("p1", [""])[0]
        p2 = params.get("p2", [""])[0]

        print(p1, p2)
        if not p1 or not p2:
            self.wfile.write(
                json.dumps(
                    {"error": "Both parameters p1 and p2 are required."}
                ).encode()
            )
            return

        # Run the similarity check
        similarity, is_similar = is_meaning_similar(p1, p2)
        print(similarity)

        self.send_response(200)

        self.send_header("content-type", "application/json")
        self.end_headers()

        # sending the response
        response = {
            "similarity": similarity,
            "is_similar": is_similar,
        }
        self.wfile.write(
            json.dumps(
                response,
                ensure_ascii=False,
            ).encode()
        )

    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "*")
        self.send_header("Access-Control-Allow-Headers", "*")
        BaseHTTPRequestHandler.end_headers(self)


port = int(os.getenv("PORT", "35026"))

# this is the object which take port
# number and the server-name
# for running the server
server = HTTPServer(("", port), GFG)
print(f"is_meaning_similar serving at http://localhost:{port}")


# this is used for running our
# server as long as we wish
# i.e. forever
server.serve_forever()
