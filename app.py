from flask import Flask ,render_template #1 st flask represent module another represent class

app = Flask(__name__)


@app.route("/")
def hello_world():
  return render_template('home.html')


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
