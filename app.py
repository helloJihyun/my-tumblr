from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.my_tumblr
app = Flask(__name__)


@app.route('/test')
def get_test_page():
    return render_template('question1.html')

@app.route('/')
def get_main_page():
    return render_template('index.html')

@app.route('/question')
def get_question_page():
    return render_template('question1.html')

@app.route('/resut')
def get_result_page():
    answers = request.args.get('answers')

    #

    return render_template('result.html')



@app.route('/qnas', methods=['GET'])
def show_qna():
    qnas = list(db.qna.find({}, {'_id': False}))
    return jsonify({'result': 'success', 'qna': qnas})


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True, port=5000)
