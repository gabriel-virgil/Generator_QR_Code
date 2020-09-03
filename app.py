'''

Project: QR Generator // III.IX.MMXX
GitHub: https://github.com/gabriel-virgil


'''

from flask import Flask, send_file, render_template, request
from pyzbar.pyzbar import decode
from PIL import Image
import qrcode

app = Flask(__name__, template_folder='template')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/download')
def download_file():
    p = "static/images/output.png"
    return send_file(p,as_attachment=True)

@app.route('/send_data', methods = ['GET', 'POST'])
def get_data_from_html():
        qrtext = request.form['qrtext']
        img = qrcode.make(qrtext)
        img.save('static/images/output.png')
        return render_template('codeqrdata.html')

if __name__=="__main__":
    app.run(debug=True)