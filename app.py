from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/login')
def login():
    return render_template('pages/login.html')


@app.route('/signup')
def sign_up():
    return render_template('pages/signup.html')


if __name__ == '__main__':
    app.run()
