from flask import Flask

from score import get_current_score
from utils import BAD_RETURN_CODE

app = Flask(__name__)


@app.route("/")
def score_server():
    score = get_current_score()
    if score:
        html = f'''<html>
                        <head>
                            <title>Scores Game</title>
                        </head>
                        <body>
                            <h1>
                                The score is:
                            </h1>
                            <div id="score">{score}</div>
                        </body>
                    </html>'''
    else:
        html = f'''<html>
                        <head>
                            <title>Scores Game</title>
                        </head>
                        <body>
                            <h1>
                                ERROR:
                            </h1>
                            <div id="score" style="color:red">{BAD_RETURN_CODE}</div>
                        </body>
                    </html>'''

    return html


if __name__ == '__main__':
    app.run(host='0.0.0.0')
