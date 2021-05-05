from flask import *

app = Flask(__name__)

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/")
def start():
    return redirect("/home")



app.run(debug=True)