# 구현 : 주문(name, address, size 서버가 저장)_post, 주문목록보여주기_get(로딩완료되자마자요청)
from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
client = MongoClient('클러스터 URL')
db = client.team

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route("/hello", methods=["POST"])
def web_post():
    name_receive = request.form['name_give']
    hi_receive = request.form['hi_give']

    doc = {
        'name': name_receive,
        'hi': hi_receive,
    }
    db.introduce.insert_one(doc)  # 하나추가요
    return jsonify({'msg': '작성완료!'})


@app.route("/hello", methods=["GET"])
def web_get():
    intro_list = list(db.introduce.find({}, {'_id': False})
                      )  # db.mars라는 곳에서 찾기(모든 내역, id제외)
    return jsonify({'intro': intro_list})  # orders라는 키로 order_list 찾은거 내려줌


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
