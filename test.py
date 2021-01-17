from pymongo import MongoClient
from collections import Counter

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.my_tumblr


answers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
all_qna = list(db.qna.find({},{'_id':False}))

all_a_score = []

def get_answer_score():
    for qna in all_qna:
        i = 0
        a_score = qna['a'][answers[i]][1]
        i += 1
        all_a_score.append(a_score)

    q1 = Counter(all_a_score[0])
    q2 = Counter(all_a_score[1])
    q3 = Counter(all_a_score[2])
    q4 = Counter(all_a_score[3])
    q5 = Counter(all_a_score[4])
    q6 = Counter(all_a_score[5])
    q7 = Counter(all_a_score[6])
    q8 = Counter(all_a_score[7])
    q9 = Counter(all_a_score[8])
    q10 = Counter(all_a_score[9])
    q11 = Counter(all_a_score[10])
    q12 = Counter(all_a_score[11])

    type_score = q1+q2+q3+q4+q5+q6+q7+q8+q9+q10+q11+q12
    return type_score

d = get_answer_score()
print(d)


#사용자가 1번~12번문제에서 선택한 답에 따른 점수(a_score)를 구하고, 하나의 리스트(all_a_score) 안에 넣는다.
#리스트에서 같은 키값의 벨류끼리 더한다.







