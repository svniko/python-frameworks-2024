from flask import Flask, render_template, request
from flask import redirect, url_for, flash
import random

# app = Flask(__name__, template_folder='')
app = Flask(__name__)
app.secret_key = 'super secret key'

pets = [
    {
        'species':'cat',
        'name':'Tom',
        'age':10,
        'color':'grey'
    },
    {
        'species':'cat',
        'name':'Vasko',
        'age':5,
        'color':'white'
    },
    {
        'species':'dog',
        'name':'Patron',
        'age':7,
        'color':'brown'
    },
]

game = {}
# game = {
#     'choise':None,
#     'you_win': 0,
#     'comp_win': 0,
#     'round': 0
# }

def init():
    global game
    # game = {
    #     'choise':None,
    #     'you_win': 0,
    #     'comp_win': 0,
    #     'round': 0
    # }

    game['choise'] = None
    game['comp_win'] = 0
    game['you_win'] = 0
    game['round'] = 0
    

@app.route('/start/')
def start():
    # game['choise'] = None
    # game['comp_win'] = 0
    # game['you_win'] = 0
    # game['round'] = 0
    init()
    return render_template('rsp.jinja',
                           title = 'Game',
                           start=True)

@app.route('/select/<ch>')
def select(ch):
    game['choise'] = ch
    return redirect(url_for('rsp'))

@app.route('/game/')
def rsp():
    if game['round'] < 5:
        game['round'] += 1
        n = random.randint(0,2)
        if game['choise'] == '0' and n == 0:
            flash('Draw', category='warning')
        elif game['choise'] == '0' and n == 1:
            flash('You win', category='warning')
            game['you_win'] += 1
        elif game['choise'] == '0' and n == 2:
            flash('Comp win', category='warning')
            game['comp_win'] += 1
        else:
            pass
    else:
        if game['comp_win'] > game['you_win']:
            flash('Total Com win', category='danger')
        elif game['comp_win'] == game['you_win']:
            flash('Total Draw', category='info')
        else:
            flash('Total Your win', category='success')


    return render_template('rsp.jinja',
                           title = 'Game')


@app.route("/pets/")
def our_pets():
    return render_template('pets.jinja', 
                           pets=pets,
                           title="Our Pets"
                        )              


@app.route("/")
def hello_world():
    name, age, profession = "Mark", 19, 'Programmer'
    template_context = dict(name=name, age=age, profession=profession)
    # return "<h1>Hello, NTU 'Khpi'!</h1>"
    return render_template('index.jinja', 
                        #    name=name,
                        #    age=age,
                        #    profession=profession
                        **template_context
                           )

@app.route("/about/")
def about():
    return """<h1>About</h1>
            <p>First page</p>"""

@app.route("/user/<name>")
def user(name):
    return f"<h1>Hello, {name}!</h1>"

@app.route('/lect3/')
def lect3():
    return render_template('lecture3.jinja')

@app.route('/hello/', methods=['GET','POST'])
def sbm():
    if request.method == "GET":
        return render_template('hello.jinja',
                           name='stranger')
    else:
        name = request.form.get('name')
        if not name:
            return render_template('lecture3.jinja', flag=0)
        
        return render_template('hello.jinja',
                            name=name,
                            flag = 1)

@app.errorhandler(405)
def method_not_allowed(e):
    return render_template('405.jinja'), 405


# if __name__ == '__main__':
#     app.run(port=8000)