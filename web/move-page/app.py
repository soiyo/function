# use flask, html file-move
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/page1')
def page1():
    return render_template('page-1.html')\
        
@app.route('/page2')
def page2():
    return render_template('page-2.html')

@app.route('/page3')
def page3():
    return render_template('page-3.html')

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)