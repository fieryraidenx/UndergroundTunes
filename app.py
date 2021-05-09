from flask import *
import spotify_processing

app = Flask(__name__)

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/")
def start():
    return redirect("/home")


print(spotify_processing.process_data(False, True, False))
#app.run(debug=True)
