from flask import *
import spotify_processing
import os
import graph_maker

app = Flask(__name__)
app.secret_key = os.urandom(16)

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/results")
def results():
    return render_template("results.html", data=session.pop('spotify_data',None), gurl=session.pop('graph_url',None))

@app.route("/")
def start():
    return redirect("/home")

@app.route("/handle_data", methods=["POST"])
def handle_data():
    processed_data = spotify_processing.process_data(
        to_bool(request.form['bpm']), 
        to_bool(request.form['positivity']),
        to_bool(request.form['nrgy'])
    )
    formatted_data = []

    #Aditya takes in genre list and returns image url of graph
    graph_url = graph_maker.get_graph_url(processed_data)

    NUM_GENRES_TO_RETURN = 5
    c = 1
    for genre in processed_data:
        if c > NUM_GENRES_TO_RETURN: break
        temp_data = (trunc(genre.final_rating), genre.songlist, trunc(genre.avg_bpm), trunc(genre.avg_pos), trunc(genre.avg_nrgy), genre.genre_name)
        formatted_data.append(temp_data)
        c += 1
    session['spotify_data'] = formatted_data
    session['graph_url'] = graph_url
    return redirect(url_for("results"))

def trunc(flt):
    '''
    Truncates float past one decimal point
    '''
    return str(flt)[:str(flt).index('.')+2]

def to_bool(string):
    return True if string == 'T' else False

app.run(debug=True)
