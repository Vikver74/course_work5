from flask import render_template

from app import app


@app.route('/fight')
def start_game():
    return render_template('')