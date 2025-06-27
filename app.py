from flask import Flask, request, render_template, redirect, url_for
import os
from process_resume import process_resume

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def upload_resume():
    if request.method == 'POST':
        file = request.files['resume']
        if file.filename.endswith('.pdf'):
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)
            data = process_resume(file_path)
            return render_template('result.html', data=data)
        else:
            return "❌ Please upload a PDF file."

    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)
