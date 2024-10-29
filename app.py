from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/template')
def template_page():
    return render_template('template.html')

@app.route('/index2')
def halaman_kedua():
    return render_template('index2.html')

if __name__ == '__main__':
    app.run(debug=True)