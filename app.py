from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/tuna')
def get_tune():
    return '<h1>TUNA</h1>'


@app.route('/tuna/<username>')
def get_tune_name(username):
    return '<h1>%s</h1>' % username


@app.route('/tuna/<int:age>')
def get_tune_age(age):
    return '<h1>%s</h1>' % age


@app.route('/method')
def get_method_used():
    return "Method used is: %s " % request.method


@app.route('/bacon', methods=['GET', 'POST'])
def get_post_method():
    return "Method used is: %s " % request.method


@app.route('/profile/<name>')
def profile(name):
    return render_template("profile.html", name=name)


@app.route('/check')
@app.route('/check/<user>')
def index(user=None):
    return render_template("user.html", user=user)


@app.route('/shopping')
def shop():
    food = ["Cheese", "Tuna", "Beef"]
    return render_template("shopping.html", food=food)


if __name__ == '__main__':
    app.run(debug=True)
