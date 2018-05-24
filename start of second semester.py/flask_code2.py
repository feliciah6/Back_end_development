from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
  return "Welcome Student"

@app.route('/home')
def home():
  return "Welcome home"
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=8080)