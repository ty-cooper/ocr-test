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
        image = request.files['image']
        output_text = pytesseract.image_to_string(Image.open(image), config='--psm 6 --oem 3 -l eng')
        return render_template("index.html", text=output_text)
    else:
        return render_template("index.html", text='')