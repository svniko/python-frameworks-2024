from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    # return "<h1>Hello, NTU 'Khpi'!</h1>"
    return render_template('index.html')

@app.route("/about/")
def about():
    return """<h1>About</h1>
            <p>First page</p>"""

@app.route("/user/<name>")
def user(name):
    return f"<h1>Hello, {name}!</h1>"

# if __name__ == '__main__':
#     app.run(port=8000)