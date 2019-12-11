greeting = '안녕하세요..!!!!'

# print(greeting)
#단순출력


menus =['순남시래기','케이에프씨', '콩나물국밥']
# print(menus[1])
# 리스트 출력

phone_book = {'순남시래기':'010-2345-2356','케이에프씨':'010-2345-2356', '콩나물국밥':'010-2345-2356'}

# print(phone_book['순남시래기'])
# 딕셔너리 키 값으로 value 출력
#-----------------------------------------------------------------------

#for 반복문으로 여러번 인사하는 코드 짜기
# for i in range(5):
#     print(greeting)


# n = 0
# while n<5:
#     print(greeting)
#     n = n+1 #== n+=1

# dust = 87
# if dust >151:
#     print("매우나쁨")
# elif 80<dust<=150:
#     print("나쁨")
# elif 30<dust<=80:
#     print("보통")
# else :
#     print("좋음")

#랜덤으로 로또 번호 추첨하기
import random

# numbers =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
# ran = random.sample(numbers, 6)
# print(ran)

numbers = random.sample(range(1,46),6)
print(numbers)