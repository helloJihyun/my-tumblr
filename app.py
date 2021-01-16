from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.my_tumblr
app = Flask(__name__)


@app.route('/')
def get_main_page():
    return render_template('index.html')

@app.route('/question')
def get_question_page():
    return render_template('question1.html')

@app.route('/result')

def get_result_page():
    answers = list(request.args.get('answers'))
    all_qnas = list(db.qna.find({}, {'_id': False}))

    for qna in all_qnas:
        i = 0
        question_score = qna['a'][answers[i]][1]
        i += 1
    print(question_score)

    return render_template('result.html')




@app.route('/qnas', methods=['GET'])
def show_qna():
    qnas = list(db.qna.find({}, {'_id': False}))
    return jsonify({'result': 'success', 'qna': qnas})


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True, port=5000)
