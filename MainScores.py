from flask import Flask, request
import Utils



app = Flask("wog")


@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        f = open(Utils.SCORES_FILE_NAME, 'r')
        SCORE = int(f.read())
        return f'<html><head><title>Scores Game</title></head><body><h1>The score is <div id="score">{SCORE}</div></h1></body></html>'
    elif request.method == 'POST':
        return "saved new car"


# @app.route('/moshe')
# def my_func():
#     return "hello and welcome to the world of games"
#
# @app.route('/')
# def default_func():
#     return "dani"


app.run(host="0.0.0.0", port=5001, debug=False)