print("hello world")
print(123456789)
print("%s 입니다." %"홍길동")
print("%s 입니다." %1234)

price=1000
print(price)
price_type=type(price) # <class'int'>
print(price_type)

text = "hello"
text_type=type(text)
print(text_type)

float = 3.3
print(float)
float_type=type(float)
print(float_type)

boolean = False
print(boolean)
boolean_type=type(boolean)
print(boolean_type)


name = "kiwom"
if name == "kiwom":
    print("통과!")

stock_price = 4000
if stock_price > 3000:
    print("pass")
elif stock_price >=3000:
    print("pass2")
elif stock_price <=3000:
    print("pass3")
else:
    print("not")

for i in range(5, 100):
    print(i)
    if i == 10:
        break

for i in range(1,6):
    for a in range(0,3):
        print("2중 for문 : %s %s" %(a, i))

stick_buy=True
count=0
while stick_buy:
    count = count +1

    if count == 10:
        break
print(count)

kakao=1000
kiwom=500
for i in range(1,4):
    kakao = kakao + 500
    kiwom = kiwom + 1000
if kiwom >= kakao:
    print("Kakao : %s" % kakao)
    print("kiwom : %s" % kiwom)
    print("키움이 더 높다")

for i in range(2,10):
    for a in range(1,10):
        print("%s * %s = %s" %(i,a,i*a))

# ----------------------------------------------
a_list = ("kiwom", "kakao", "daesin")
for val in a_list:
    print(val)
a_list = ["kiwom","kakao","daesin"]
a_list.append("naver")
for val in a_list:
    print(val)
print("---------------------")
print(a_list[3])
a_list[3]="daum"
print(a_list[3])
del a_list[1]
for val in a_list:
    print(val)
print("===================")
for idx, val in enumerate(a_list):
    print("인덱스 : %s, 값: %s" %(idx, val))

a_dict = {"kiwom" : 1300, "kakao" : 1500, "naver" : 1000}
print(a_dict.get("kiwom"))
# print(a_dict['test']) -> key error 발생
print(a_dict.get("test"))

print(a_dict.values())

for key, value in a_dict.items():
    print("키 : %s , value값 : %s " % (key,value))

dict = {"kiwom" : 5000, "kakao" : 3000, "naver" : 2000}
sum=0
for key, value in dict.items():
    sum=sum+value
print("3개의 총액 : %s" %sum)
print("..........................")
count=115000
kiwom_count=0
kakao_count=0
naver_count=0
flag=True

while flag:
    for key in dict:
        print("count : %s " % count)
        if dict.get(key) > count:
            flag=False
            break
        print("현재 남은금액 : %s" %count)
        count=count-dict.get(key)
        if key =="kiwom":
            kiwom_count = kiwom_count +1
        elif key == "kakao":
            kakao_count = kakao_count +1
        elif key =="naver":
            naver_count = naver_count +1

print("kiwom : %s주 / kakao : %s주 / naver : %s주" % (kiwom_count, kakao_count, naver_count))
day=1000
flag=True
while flag:
    for key in dict:
        print(dict.get(key))
        dict[key] = dict.get(key)+day
        print(dict.get(key))
        if dict.get(key) == 10000:
            dict.update({"이베스트":5000})
            print(dict)
            flag=False
            break;

# week 2
def english():
    print("영어")
english()

def math(name):
    print(name)
math("tomas")

def academy(name1, name2, name3):
    print(name1)
    print(name2)
    print(name3)
academy("edison","tom", "billy")
print("----------------")

def test():
    help("help")
def help(txt):
    print(txt)
test()


def name():
    name="광수"
    return name

who=name()
print(who)

def two():
    return "a", "b"
a,b=two()
result=two()
print(result)
print(a,b)

class B_school():
    def __init__(self):
        print("b학교 초기화")
B_school()

class A_school():
    def __init__(self):
        print("초기화 1")
        self.student_name=None

        b=self.math()
        print("수학과 학생 : %s " %b)

    def math(self):
        self.student_name="영수"
        name = self.student_name
        return name
A_school()

class B_school():
    def __init__(self):
        print("b대학 초기화")
        self.school_name = "b학교"

class A_school():
    def __init__(self):
        print("생성자")
        self.student1_name=None

        b=self.math()
        print("수학과 : %s" %b)

        b_school = B_school()
        print(b_school.school_name)
    def math(self):
        self.student1_name = "영수"
        name = self.student1_name
        return name
A_school()