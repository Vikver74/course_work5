import os
import dotenv

from flask import Flask, render_template, request, redirect

from classes.unit import unit
from classes.arena import Arena
from write_log import open_log_file, write_log, close_log_file
from utils import create_enemy, create_hero, choose_unit_hero, choose_unit_enemy


app = Flask(__name__)

dotenv.load_dotenv(override=True)

if os.environ.get('APP_CONFIG') == 'development':
    from config import DevConfig
    app.config.from_object(DevConfig)
elif os.environ.get('APP_CONFIG') == 'production':
    from config import ProductConfig
    app.config.from_object(ProductConfig)

app.app_context().push()

app.secret_key = app.config.get('SECRET_KEY')
arena = Arena()


@app.route('/')
def start_game():
    return render_template('index.html')


@app.route('/choose-hero/', methods=['GET', 'POST'])
def choose_player():
    if request.method == 'GET':
        header: str = 'Выберите героя'
        return render_template('hero_choosing.html', unit=unit, header=header), 200

    if request.method == 'POST':
        choose_unit_hero(request)
        return redirect('/choose-enemy'), 302


@app.route('/choose-enemy', methods=['GET', 'POST'])
def choose_enemy():
    if request.method == 'GET':
        header: str = 'Выберите врага'
        return render_template('hero_choosing.html', unit=unit, header=header), 200

    if request.method == 'POST':
        choose_unit_enemy(request)
        return redirect('/fight'), 302


@app.route('/fight', methods=['GET'])
def fight():
    hero = create_hero()
    enemy = create_enemy()
    result: str = 'Игра начата'
    open_log_file()
    arena.start_game(hero=hero, enemy=enemy)
    return render_template('fight.html', heroes=arena, result=result), 200


@app.route('/fight/hit', methods=['GET'])
def fight_hit():
    result: str = arena.hit()
    write_log(result + '\n')
    return render_template('fight.html', heroes=arena, result=result), 200


@app.route('/fight/pass-turn', methods=['GET'])
def skip_move():
    result: str = arena.skip_move()
    write_log(result + '\n')
    return render_template('fight.html', heroes=arena, result=result), 200


@app.route('/fight/use-skill', methods=['GET'])
def use_skill():
    result: str = arena.use_skill()
    write_log(result + '\n')
    return render_template('fight.html', heroes=arena, result=result), 200


@app.route('/fight/end-fight', methods=['GET'])
def end_fight():
    close_log_file()
    return redirect('/'), 302


if __name__ == '__main__':
    app.run()


