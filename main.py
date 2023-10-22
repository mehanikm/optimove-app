from flask import request, redirect, Flask
from redis import Redis
import os

REDIS_HOST = os.environ["REDIS_HOST"]
REDIS_PORT = os.environ["REDIS_PORT"]
redis = Redis(host=REDIS_HOST, port=REDIS_PORT)

app = Flask(__name__)


@app.route("/")
def main():
    # return f"<p>{request.remote_addr[::-1]}</p>" # Let this version exist as well.
    # Fetch IP of the remote.
    req_ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    # Split IP into bits, then reverse the components and join.
    reverse_req_ip = ".".join(req_ip.split(".")[::-1])
    # Set value in redis
    redis.set("reverse_req_ip", reverse_req_ip)
    # H1 header for computer-strained eyes.
    return f"<h1>{reverse_req_ip}</h1>"


@app.route("/rick")
def rick():
    # Undocumented.
    return redirect("https://www.youtube.com/watch?v=dQw4w9WgXcQ", code=302)


@app.route("/health")
def health():
    # Healthcheck.
    return {"message": "OK"}, 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
