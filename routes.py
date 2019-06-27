from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
  username = {
    "user": "Eugene"
  }
  return render_template("index.html", title="Lab 2", username=username)


if __name__ == "__main__":
  app.run(debug=True)
