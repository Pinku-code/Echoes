from flask import Flask, render_template, url_for

app = Flask(__name__)


#Routes
@app.route("/")
def Home():
    return render_template('Home.html')

@app.route("/contact")
def Contact():
    return render_template('Contact.html')

if __name__ == "__main__" :
    app.run(debug=True)