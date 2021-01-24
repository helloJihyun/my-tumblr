qna_data = []

    # 1번 Q&A
qna_data.append(
    {'q':'평소 커피를 사러 나가면',
     'a':[
         ('내 입맛에 맛는 카페만 들러 단골이 된다.',{'type1': 10, 'type2': 0, 'type3': 2, 'type4' : 1, 'type5' : 1, 'type6' : 2, 'type7' : 3, 'type8' : 1}),
         ('그 날에 기분에 따라 내키는 곳으로 간다.',{'type1' : 0, 'type2' : 10, 'type3' : 1, 'type4' : 2, 'type5' : 2, 'type6' : 1, 'type7' : 1, 'type8' : 3}),
         ]
     })
    # 2번 Q&A
qna_data.append(
    {'q':'당신이 음료를 마실 땐',
     'a':[
         ('얼어 죽어도 아이스!',{'type1' : 0, 'type2' : 0, 'type3' : 0, 'type4' :10, 'type5' :3, 'type6' :1, 'type7' :2, 'type8' :1}),
         ('더워죽어도 뜨끈하게!',{'type1' : 0, 'type2' : 0, 'type3' : 10, 'type4' :0, 'type5' :1, 'type6' :3, 'type7' :1, 'type8' :2}),
         ]
     })
    # 3번 Q&A
qna_data.append(
    {'q': '오랜만에 꿀 같은 휴일날',
     'a': [
         ('가까운 근교로 당일치기 여행가기', {'type1' :0, 'type2' :0, 'type3' :0, 'type4' :0, 'type5' :0, 'type6' :0, 'type7' :0, 'type8' :0}),
         ('하루종일 카페에서 바깥 풍경보며 책 읽기', {'type1' :0, 'type2' :0, 'type3' :0, 'type4' :0, 'type5' :0, 'type6' :10, 'type7' :0, 'type8' :0}),
     ]
     })
    # 4번 Q&A
qna_data.append(
    {'q': '플라스틱 빨대를 버릴 땐',
     'a': [
         ('일반 쓰레기통에 버린다.', {'type1' :0, 'type2' :0, 'type3' :0, 'type4' :0, 'type5' :0, 'type6' :0, 'type7' :10, 'type8' :2}),
         ('깨끗하게 씻어 재활용 쓰레기통에 버린다.', {'type1' :0, 'type2' :0, 'type3' :0, 'type4' :0, 'type5' :0, 'type6' :0, 'type7' :0, 'type8' :0}),
     ]
     })
    # 5번 Q&A
qna_data.append(
    {'q': '규칙을 만들 때는',
     'a': [
         ('무슨 일이 있어도 지킬 생각으로 만든다.', {'type1' :3, 'type2' :0, 'type3' :0, 'type4' :0, 'type5' :0, 'type6' :0, 'type7' :1, 'type8' :0}),
         ('상황에 따라 바꿀 생각으로 만든다.', {'type1' :0, 'type2' :3, 'type3' :0, 'type4' :0, 'type5' :0, 'type6' :0, 'type7' :0, 'type8' :1}),
     ]
     })
    # 6번 Q&A
qna_data.append(
    {'q': '당신의 집 찬장에는',
     'a': [
         ('종류별 컵이 웬만큼 구비되어 있다. ', {'type1' :0, 'type2' :0, 'type3' :0, 'type4' :0, 'type5' :0, 'type6' :0, 'type7' :0, 'type8' :3}),
         ('기본적인 컵만 구비되어 있다.', {'type1' :0, 'type2' :0, 'type3' :0, 'type4' :0, 'type5' :0, 'type6' :0, 'type7' :1, 'type8' :0}),
     ]
     })
    # 7번 Q&A
qna_data.append(
    {'q': '당신이 물건을 살 때는',
     'a': [
         ('디자인을 최우선으로 고려한다.', {'type1' :0, 'type2' :0, 'type3' :0, 'type4' :0, 'type5' :0, 'type6' :0, 'type7' :0, 'type8' :0}),
         ('실용성 및 기능을 최우선으로 고려한다.', {'type1' :0, 'type2' :0, 'type3' :0, 'type4' :0, 'type5' :0, 'type6' :0, 'type7' :0, 'type8' :10}),
     ]
     })
    # 8번 Q&A
qna_data.append(
    {'q': '당신의 현재 생활패턴',
     'a': [
         ('고정적인 장소 없이 여기저기 이동이 많다.', {'type1' :0, 'type2' :1, 'type3' :0, 'type4' :0, 'type5' :1, 'type6' :0, 'type7' :0, 'type8' :0}),
         ('집-학교 또는 집-회사', {'type1' :1, 'type2' :0, 'type3' :0, 'type4' :0, 'type5' :0, 'type6' :3, 'type7' :0, 'type8' :0}),
     ]
     })
    # 9번 Q&A
qna_data.append(
    {'q': '평소 내 가방에는',
     'a': [
         ('최소한의 짐만 넣고 다닌다.', {'type1' :1, 'type2' :0, 'type3' :0, 'type4' :0, 'type5' :0, 'type6' :0, 'type7' :1,'type8' :0}),
         ('만일의 상황을 대비한 갖가지 물건이 많다.', {'type1' :0, 'type2' :1, 'type3' :0, 'type4' :0, 'type5' :3, 'type6' :0, 'type7' :0, 'type8' :1}),
     ]
     })
    # 10번 Q&A
qna_data.append(
    {'q': '내 책상을 꾸민다면',
     'a': [
         ('내가 좋아하는 캐릭터 디자인 소품을 들인다', {'type1' :0, 'type2' :0, 'type3' :0, 'type4' :0, 'type5' :0, 'type6' :0, 'type7' :0, 'type8' :0}),
         ('심플하고 모던한 느낌의 소품들을 들인다', {'type1' :1, 'type2' :0, 'type3' :0, 'type4' :0, 'type5' :0, 'type6' :0, 'type7' :0, 'type8' :0}),
     ]
     })
    # 11번 Q&A
qna_data.append(
    {'q': '심각한 환경오염 영상을 본 ',
     'a': [
         ('일회용품을 평소와 같이 사용한다.', {'type1' :0, 'type2' :0, 'type3' :0, 'type4' :0, 'type5' :0, 'type6' :0, 'type7' :3, 'type8' :0}),
         ('최대한 일회용품 사용을 줄이려고 노력한다.', {'type1' :0, 'type2' :0, 'type3' :0, 'type4' :0, 'type5' :0, 'type6' :0, 'type7' :0, 'type8' :0}),
     ]
     })
    # 12번 Q&A
qna_data.append(
    {'q': '당신이 물건을 살 땐',
     'a': [
         ('남들과는 차별된 독특한 스타일', {'type1' :0, 'type2' :1, 'type3' :0, 'type4' :0, 'type5' :0, 'type6' :0, 'type7' :0, 'type8' :0}),
         ('언제 어디서나 어울리는 일반적인 스타일', {'type1' :1, 'type2' :0, 'type3' :0, 'type4' :0, 'type5' :0, 'type6' :0, 'type7' :0, 'type8' :0}),
     ]
     })

result_data = {}

result_data['type1'] = ['한 우물만 파는 당신,','클래식 텀블러','한 우물만 팔 수 있다는 건 굉장히 대단한 능력이에요. 한번 시작한 일은 끝을 보고야 마는 당신은 뭐든지 이루어낼 수 있겠네요!','당신과 닮은 텀블러', '1913년부터 텀블러만 만들었다.','Stanley','스탠리','http://www.citycreek.co.kr/shopimages/20201110143655_509_0.jpg']
result_data['type2'] = ['언제나 새로움을 추구하는 당신,','카멜레온 텀블러','당신의 변화무쌍한 모습은 항상 주변인에게 일상의 영감이 됩니다. 새로운 도전도 마다하지 않는 당신은 이 시대에 꼭 필요한 사람이네요!','당신과 닮은 텀블러','기분에 따라 바꾸는 텀블러 색깔!','Alex','알렉스','https://www.alexlife.co.kr/wp-content/uploads/2018/06/alex-tumbler-16oz-white-lilac-copy.jpg']
result_data['type3'] = ['언제나 핫한 당신,','핫!뜨거 텀블러','꽁꽁 얼어버린 마음도 한순간에 녹일 만큼 따뜻한 감성을 가지셨네요. 세상을 당신의 편으로 만들어버리는 대단한 능력!','당신과 닮은 텀블러','독보적 진공 단열 기술로 따뜻하게','THERMOS','써모스','https://thermosshop.kr/web/product/extra/big/20200602/46c1c4c88597ac63a80e9f6da1209f3d.png']
result_data['type4'] = ['언제 어디서나 쿨한 당신,','앗!차거 텀블러','당신의 쿨워터향에 모두가 이미 취해버렸어요. 현실적인 안목으로 무슨 일이든 당당하게 척척 해내는 당신은 만능 재주꾼!','당신과 닮은 텀블러','보기만 해도 시원해지는 텀블러','Pilmoa','필모아','http://pilmoa.com/web/product/medium/202012/acdcbc510c0763069a49242b5a9007f2.png']
result_data['type5'] = ['오지에 가도 살아남을 당신,','아웃도어 텀블러','넘치는 에너지를 가진 도시의 모험가이시군요! 모험심으로 위기상황을 극복하고 새로운 세상을 개척하는 이 시대의 콜롬버스!','당신과 닮은 텀블러','최초의 스테인레스 텀블러','Klean Kanteen','클린켄틴','http://img.gqkorea.co.kr/gq/2018/09/style_5ba4bed9aefb5.jpg']
result_data['type6'] = ['의자와 물아일체된 당신,','인도어 텀블러','그 누구보다 몰입력이 뛰어나군요! 한 번 몰입하면 진심을 다하는 당신, 당신의 결과물은 감히 그 누구도 쉽게 상상하지 못할거에요.','당신과 닮은 텀블러','커피에 커피를, 커피 찌꺼기 텀블','Huskee','허스키','https://media1.popsugar-assets.com/files/thumbor/tGtiNiDQcpwvcJZ5LvO2K_Bp41s/fit-in/1024x1024/filters:format_auto-!!-:strip_icc-!!-/2019/12/09/197/n/36735815/68506a375d8f9984_Warm_1_1024x1024_2x/i/HuskeeCup-SmoothieJuiceIced-Coffee-Huskee-Cup-Straw-Bundle35.jpg']
result_data['type7'] = ['환경을 두번 생각하는 당신,','친환경 텀블러','우러러 볼수록 높아만지는 환경을 향한 당신의 마음. 혼란스러운 세상에서도 본질적인 가치를 알고 있는 당신은 절대 무너지지 않는 단단한 사람입니다.','당신과 닮은 텀블러','판매의 10퍼센트를 환경단체에 기부',"S'well",'스웰','http://img.gqkorea.co.kr/gq/2018/09/style_5ba4bedd27ad5.jpg']
result_data['type8'] = ['도구를 쓸 줄 아는 당신,','꿀기능 텀블러','도구를 사용하면 몸이 덜 고생한다! 그 누구보다 도구를 잘 사용하는 당신은 동시에 여러가지 일을 척척 해낼 수 있는 멀티플레이어이군요!','당신과 닮은 텀블러','물 마실 시간을 알려주는 스마트 텀블러','EQUA','EQUA','https://cdn.shopify.com/s/files/1/0252/8526/3469/products/equa-smart-water-bottle-pink_400x.gif?v=1605648714']
