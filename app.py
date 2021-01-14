from flask import Flask, render_template, jsonify, request

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

@app.route('/question', methods=['GET'])
def show_qna():
    return jsonify({'result': 'success'})


if __name__ == '__main__':
    app.run('0.0.0.0',debug=True,port=5000)
