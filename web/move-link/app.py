from flask import Flask, render_template, redirect
app = Flask(__name__)


@app.route('/')
def naver(): return render_template("main.html")


@app.route('/git')
def daum(): return redirect("https://github.com/soiyo/")


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
