from math import *
from random import *

# from reportlab.pdfgen import canvas
# from reportlab.pdfbase import pdfmetrics
# from reportlab.pdfbase.ttfonts import TTFont
# from reportlab.lib.pagesizes import A4

# pdfmetrics.registerFont(TTFont("맑은고딕", "malgun.ttf"))
# pdf = canvas.Canvas("test.pdf", pagesize=A4)
# pdf.setFont("맑은고딕", 16)
# pdf.drawString(30, 750, "점검보고서")
# pdf.save()

print("hello world")
print(5)
print(1000)
print(3.14)
print(7+18)
print("::풍선")
print(5>10)
print(5/10)
print(2**7)
print(15%11)

print(25//10)

print(pow(5,12))
print(float(3.17))
print(not(5>10) or (5<100))

animal = "팔팔이팔"
name = "POLO"

age = 5
hobby = "놀리기"

is_babo = age >=3

# 팔팔이 확인해 주세요.
print ("우리집 " + animal + " 이름은 " + name)
print ( name + "는 " + str(age) + "살입니다 ")
print ( name , "는", str(is_babo) , "어른일까요? ")

# print( random())

for i in animal : print( random() * 10 + 1 , animal, "입니다.")

print( 5> 3> 10)
print( 2 + 5 * 4 / 5)

namber = 3 + 2.0 + 8 * 8

namber += 5
namber /= 3

print(str(namber))
print (min(5,2))

print(floor(4.98))

jumin = "711211-1108610"


print("성별 : " + jumin [7])
print("년도 : " + jumin [0:2])
print("월 : " + jumin [2:4])
print("일 : " + jumin [0:6])

print("뒤 7자리 : " + jumin [7:])


print("뒤 7자리 : " + jumin [-7:])


print("뒤 7자리 : " + jumin [-7:])

python = "Python is Amazing!"

print(python.lower())
print(python.upper())

print(python.replace("Python", "Java"))

print(python[0].isupper())

print(len(python))

index = python.index("n")
print(index)

print(python.find("Java"))


print ("나는 %s %s 입니다." % ("아이돌", "가수") )

print ("나는 {} {} 입니다.".format("아이돌1", "가수2") )

print ("나는 {1} {0} 입니다.".format(1, 2) )


print ("나는 {type1} {type2} 입니다.".format( type1 = "노인", type2 = "돌아이" ) )

aaa1 = "미틴"
bbb2 = "도전"

print ("나는 {} {} 입니다.".format( aaa1, bbb2 ) )

# 줄바꿈 \n
print("백문이 불여일견 \n 백견이 불여일타")

print('나도 코딩 "나도코딩" 입니다.')

print("나도 코딩 \"나도코딩\" 입니다.")
 
url = "http://naver.com"

my_str = url.replace("http://","")

print(" {}".format(my_str))

#my_str = my_str.replace(".com","")
my_str = my_str[:my_str.index(".")] 
# my_str[0:5]

print(" {}".format(my_str))

password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"

print("{} {}".format(url, password))

subway = ["10", "20", "30"]

print(subway.index("20"))
subway.append("50")
print(subway)

subway.insert(2, "60")
subway.insert(2, "70")
subway.insert(2, "70")
print(subway.pop())
print(subway.reverse())

print(subway.count("70"))


print(subway.pop())
print(subway.reverse())

print(subway)
print(subway.pop())
print(subway)
print(subway.pop())
print(subway)

print(subway.pop())

cabi ={ 3:"BOX", 100: "CIR"}

print(cabi[3])

print(cabi.get(3))

print(cabi.get(3,"사용가능"))

weather = "비"
weather = input ("오늘 날씨는 어때요?")


if weather == "비" or "눈" :
  print("우산을 챙기세요")
elif weather == "미세먼지" :
  print("마스크를 챙기세요")
else :
  print("아무것도 필요없어요")









