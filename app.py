from flask import Flask

app = Flask(__name__)


@app.route('/test')
def get_test_page():
    return render_template('question1.html')


if __name__ == '__main__':
    app.run()
