from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'secured'

@app.route("/")
def index():
    if not "num" in session:
        session['num'] = 0
    session['num'] += 1
    return render_template("index.html")

@app.route("/count")
def count():
    if not "num" in session:
        session['num'] = 0
    session['num'] += 1
    print(['num'])
    return render_template("index.html")

@app.route("/count2")
def doublecount():
    if not "num" in session:
        session['num'] = 0
    session['num'] = session['num'] + 2
    return render_template("index.html")

@app.route('/destroy_session')
def clear():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)