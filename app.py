from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def search():
    return render_template("home.html")

if __name__ == '__main__':
    app.run(debug=True)
