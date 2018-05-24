from flask import flask
from Flask request flask
app= Flask(__name__)
@app.route('/')
def index(name="student"):
  return "Welcome {} to Akirachix".format(name)

  @app.route("/Welcome/<name>")
  def Welcome(name = "student"):
    return "Welcome {} to Akireachix".format (name)
    if__name__ =="__main__"
    app.run(host='0.0.0.0',port=8080)