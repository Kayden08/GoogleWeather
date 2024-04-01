from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def search():
    return render_template("home.html")
@app.route('/results', methods=["GET", "POST"])
def results():
    api_key = "b12703d2df47873eaf71613c74db92a2"
    city = request.form.get('city')
    url = 'https://api.openweathermap.org/data/2.5/weather?q=' + city + "&appid=" + api_key

if __name__ == '__main__':
    app.run(debug=True)
