from flask import Flask, render_template, url_for

app = Flask(__name__)


#Routes
@app.route("/")
def Home():
    return render_template('Home.html')

@app.route("/contact")
def Contact():
    return render_template('Contact.html')

@app.route("/blogs")
def Blog():
    return render_template('Blog.html')

@app.route("/login")
def Login():
    return render_template('Login.html')

@app.route("/register")
def Register():
    return render_template('Register.html')

if __name__ == "__main__" :
    app.run(debug=True)