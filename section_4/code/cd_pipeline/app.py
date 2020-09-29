from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
        "https://media.giphy.com/media/kreQ1pqlSzftm/giphy.gif",
        "https://media.giphy.com/media/Z9tvqoD1SEQcomTVaK/giphy.gif",
        "https://media.giphy.com/media/fItgT774J3nWw/giphy.gif",
        "https://media.giphy.com/media/eYilisUwipOEM/giphy.gif"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")  
