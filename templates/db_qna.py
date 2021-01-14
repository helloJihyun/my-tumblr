from pymongo import MongoClient

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.my_tumblr  # 'dbsparta'라는 이름의 db를 사용합니다. 'dbsparta' db가 없다면 새로 만듭니다.

# MongoDB에 insert 하기

# 'qnas'라는 collection에 데이터를 생성합니다.
db.qna.insert_one(
    # 1번 Q&A
    {'q':'평소 커피를 사러 나가면',
     'a':[
         ('내 입맛에 맛는 카페만 들러 단골이 된다.',[('type1',10), ('type2',0), ('type3',2), ('type4',1), ('type5',1), ('type6',2), ('type7',3), ('type8',1)]),
         ('그 날에 기분에 따라 내키는 곳으로 간다.',[('type1',0), ('type2',10), ('type3',1), ('type4',2), ('type5',2), ('type6',1), ('type7',1), ('type8',3)]),
         ]
     })
    # 2번 Q&A
db.qna.insert_one(
    {'q':'당신이 음료를 마실 땐',
     'a':[
         ('얼어 죽어도 아이스!',[('type1',0), ('type2',0), ('type3',0), ('type4',10), ('type5',3), ('type6',1), ('type7',2), ('type8',1)]),
         ('더워죽어도 뜨끈하게!',[('type1',0), ('type2',0), ('type3',10), ('type4',0), ('type5',1), ('type6',3), ('type7',1), ('type8',2)]),
         ]
     })
    # 3번 Q&A
db.qna.insert_one(
    {'q': '오랜만에 꿀 같은 휴일날',
     'a': [
         ('가까운 근교로 당일치기 여행가기', [('type1',0), ('type2',0), ('type3',0), ('type4',0), ('type5',0), ('type6',0), ('type7',0), ('type8',0)]),
         ('하루종일 카페에서 바깥 풍경보며 책 읽기', [('type1',0), ('type2',0), ('type3',0), ('type4',0), ('type5',0), ('type6',10), ('type7',0), ('type8',0)]),
     ]
     })
    # 4번 Q&A
db.qna.insert_one(
    {'q': '다 쓴 플라스틱 빨대를 버릴 땐',
     'a': [
         ('일반 쓰레기통에 버린다.', [('type1',0), ('type2',0), ('type3',0), ('type4',0), ('type5',0), ('type6',0), ('type7',10), ('type8',2)]),
         ('깨끗하게 씻어 재활용 쓰레기통에 버린다.', [('type1',0), ('type2',0), ('type3',0), ('type4',0), ('type5',0), ('type6',0), ('type7',0), ('type8',0)]),
     ]
     })
    # 5번 Q&A
db.qna.insert_one(
    {'q': '규칙을 만들 때는',
     'a': [
         ('무슨 일이 있어도 지킬 생각으로 만든다.', [('type1',3), ('type2',0), ('type3',0), ('type4',0), ('type5',0), ('type6',0), ('type7',1), ('type8',0)]),
         ('상황에 따라 바꿀 생각으로 만든다.', [('type1',0), ('type2',3), ('type3',0), ('type4',0), ('type5',0), ('type6',0), ('type7',0), ('type8',1)]),
     ]
     })
    # 6번 Q&A
db.qna.insert_one(
    {'q': '당신의 집 찬장에는',
     'a': [
         ('종류별 컵이 웬만큼 구비되어 있다. ', [('type1',0), ('type2',0), ('type3',0), ('type4',0), ('type5',0), ('type6',0), ('type7',0), ('type8',3)]),
         ('기본적인 컵만 구비되어 있다.', [('type1',0), ('type2',0), ('type3',0), ('type4',0), ('type5',0), ('type6',0), ('type7',1), ('type8',0)]),
     ]
     })
    # 7번 Q&A
db.qna.insert_one(
    {'q': '당신이 물건을 살 때는',
     'a': [
         ('디자인을 최우선으로 고려한다.', [('type1',0), ('type2',0), ('type3',0), ('type4',0), ('type5',0), ('type6',0), ('type7',0), ('type8',0)]),
         ('실용성 및 기능을 최우선으로 고려한다.', [('type1',0), ('type2',0), ('type3',0), ('type4',0), ('type5',0), ('type6',0), ('type7',0), ('type8',10)]),
     ]
     })
    # 8번 Q&A
db.qna.insert_one(
    {'q': '당신의 현재 생활패턴',
     'a': [
         ('고정적인 장소 없이 여기저기 이동이 많다.', [('type1',0), ('type2',1), ('type3',0), ('type4',0), ('type5',1), ('type6',0), ('type7',0), ('type8',0)]),
         ('집-학교 또는 집-회사', [('type1',1), ('type2',0), ('type3',0), ('type4',0), ('type5',0), ('type6',3), ('type7',0), ('type8',0)]),
     ]
     })
    # 9번 Q&A
db.qna.insert_one(
    {'q': '평소 내 가방에는',
     'a': [
         ('최소한의 짐만 넣고 다닌다.', [('type1',1), ('type2',0), ('type3',0), ('type4',0), ('type5',0), ('type6',0), ('type7',1),('type8',0)]),
         ('만일의 상황을 대비한 갖가지 물건이 많다.', [('type1',0), ('type2',1), ('type3',0), ('type4',0), ('type5',3), ('type6',0), ('type7',0), ('type8',1)]),
     ]
     })
    # 10번 Q&A
db.qna.insert_one(
    {'q': '내 책상을 꾸민다면',
     'a': [
         ('내가 좋아하는 캐릭터 디자인 소품을 들인다', [('type1',0), ('type2',0), ('type3',0), ('type4',0), ('type5',0), ('type6',0), ('type7',0), ('type8',0)]),
         ('심플하고 모던한 느낌의 소품들을 들인다', [('type1',1), ('type2',0), ('type3',0), ('type4',0), ('type5',0), ('type6',0), ('type7',0), ('type8',0)]),
     ]
     })
    # 11번 Q&A
db.qna.insert_one(
    {'q': '심각한 환경오염 영상을 본 다음날',
     'a': [
         ('일회용품을 평소와 같이 사용한다.', [('type1',0), ('type2',0), ('type3',0), ('type4',0), ('type5',0), ('type6',0), ('type7',3), ('type8',0)]),
         ('최대한 일회용품 사용을 줄이려고 노력한다.', [('type1',0), ('type2',0), ('type3',0), ('type4',0), ('type5',0), ('type6',0), ('type7',0), ('type8',0)]),
     ]
     })
    # 12번 Q&A
db.qna.insert_one(
    {'q': '당신이 물건을 살 땐',
     'a': [
         ('남들과는 차별된 독특한 스타일', [('type1',0), ('type2',1), ('type3',0), ('type4',0), ('type5',0), ('type6',0), ('type7',0), ('type8',0)]),
         ('언제 어디서나 어울리는 일반적인 스타일', [('type1',1), ('type2',0), ('type3',0), ('type4',0), ('type5',0), ('type6',0), ('type7',0), ('type8',0)]),
     ]
     })


