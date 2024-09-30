from flask import Flask, render_template, request

# app = Flask(__name__, template_folder='')
app = Flask(__name__)

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