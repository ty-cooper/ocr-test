from flask import Flask, render_template, request
from PIL import Image
import pytesseract

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if 'image' in request.files:
        output_text = pytesseract.image_to_string(Image.open(request.files['image']))
        return render_template("index.html", text=output_text)
    else:
        return render_template("index.html", text='')