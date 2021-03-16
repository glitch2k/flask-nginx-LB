from flask import Flask


app = Flask(__name__)

@app.route("/")
def home():
    return "THIS IS APP01"



if __name__ == "__main__":
    app.debug=True
    app.run(host='0.0.0.0', port=1146)