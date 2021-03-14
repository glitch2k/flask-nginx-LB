from flask import Flask


app = Flask(__name__)

@app.route("/")
def home():
    return "THIS IS APP02"



if __name__ == "__main__":
    app.debug=True
    app.run(host='192.168.1.81', port=1158)