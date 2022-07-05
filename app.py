from flask import Flask

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def index():
    try:
        return "This is an END-TO-END Machine Learning Heat Load & Cool Load Estimation Project"
    except Exception as e:
        return e

if __name__ == "__main__":
    app.run(debug=True)