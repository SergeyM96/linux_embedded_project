from flask import Flask, jsonify

HOST, PORT = "0.0.0.0", 5001

app = Flask(__name__)

@app.route("/alive")
def alive():
    return jsonify(status="alive")

@app.errorhandler(404)
def not_found(e):
    return jsonify(error="not found"), 404

@app.errorhandler(405)
def method_not_allowed(e):
    return jsonify(error="method not allowed"), 405, {"Allow": ", ".join(e.valid_methods)}

if __name__ == "__main__":
    app.run(host=HOST, port=PORT, debug=False)