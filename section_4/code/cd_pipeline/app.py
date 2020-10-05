from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
        "https://media.giphy.com/media/cKhTE6YDCmPm0p5cWG/giphy.gif",
        "https://media.giphy.com/media/L4fv5eLVk6geaVmkaO/giphy.gif",
        "https://media.giphy.com/media/mpfMDb6MB6EWQ/giphy.gif",
        "https://media.giphy.com/media/xTiTnHXbRoaZ1B1Mo8/giphy.gif",
        "https://media.giphy.com/media/ASzK5wWjMtc6A/giphy.gif"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")  
