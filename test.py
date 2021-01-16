from pymongo import MongoClient

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.my_tumblr


answers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
all_qnas = list(db.qna.find({},{'_id':False}))

for qna in all_qnas:
    i = 0
    question_score = qna['a'][answers[i]][1]
    i += 1
    print(question_score)

