# Dictionary

#첫번째 방법
my_dict = {'한국어':'안녕', '영어':'hi','독일어':'Guten tag'}

#두번째 방법
my_dict2 ={}
my_dict2['한국어']='안녕'
my_dict2['영어']='hi'
my_dict2['독일어']='Guten tag'

#세번째 방법
my_dict3=dict(한국어='안녕', 영어='하이', 독일어='구텐탁')

# print(my_dict)
# print(my_dict2)
# print(my_dict3)

area_code = {'서울':'02'}
area_code['경기도'] ='031'
# print(area_code)


# for key in area_code:
    # print(key)  #key 값 출력
    # print(area_code[key])  #value 값 출력

#key와 value값을 각각 
# for key, value in area_code.items():
#     print(key, value)

#value값만
for value in area_code.values():
    print(value)

#key 값만
for key in area_code.keys():
    print(key)    