from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

client = MongoClient('mongodb://jihyun:jihyun9802@localhost',27017)
db = client.my_tumblr
app = Flask(__name__)

from data_qna import qna_data, result_data

@app.route('/')
def get_main_page():
    return render_template('index.html')

@app.route('/question')
def get_question_page():
    return render_template('question1.html')

@app.route('/result')
def get_result_page():
    answers = list(request.args.get('answers'))
    result_type = calc_result(answers)
    result = result_data[result_type]
    return render_template('result.html', result=result)


def calc_result(answers):
    all_qna = qna_data
    score_dict = dict()

    for i in range(8):
        score_dict['type'+str(i+1)] = 0

    for i in range(len(answers)):
        answer = int(answers[i])
        qna = all_qna[i]
        score = qna['a'][answer][1]

        for s in score:
            key = s
            val = score[s]
            score_dict[key] += val

    result = max(score_dict, key=score_dict.get)
    return result


@app.route('/qnas', methods=['GET'])
def show_qna():
    qnas = qna_data
    return jsonify({'result': 'success', 'qna': qnas})

@app.route('/prod_info', methods=['GET'])
def prod_info():
    prod_info = list(db.prod_info.find({}, {'_id': 0}))
    return jsonify({'result': 'success', 'prod_info': prod_info})

if __name__ == '__main__':
    app.run('0.0.0.0', debug=True, port=5000)
