# 데이터 타입 (숫자, 문자열, 불리언)
# 어떤 값을 담는 자료구조 (변수, 리스트, 튜플, 딕셔너리, 집합)
# 정수형 (1,-1, 2,-2) int
# 실수형 (1.24, -1.24) float
# 컴퓨터식 지수 표현 방식 (4,24e10, 4.24e-10)
# 8진수 (0o37)
# 16진수 (0x7A)

#TODO ex_1) Int
a = 1
print(type(a)) #type()은 데이터 타입을 보는 함수

#TODO ex_2) Float
a = 1.2
print(type(a))

#TODO ex_3) Float Squared
a = 4.24e10 #4.24 * 10의 10승
print(type(a))

a = 4.24e-10
print(type(a))

#TODO ex_4) Plus, minus, minus, division
a = 3
b = 4

print(a+b) #더하기

a = 5
b = 4

print(a-b) #빼기

a = 5
b = 4

print(a*b) #곱하기
print(a**b) #거듭제곱

a = 5
b = 4

print(a/b) #나누기
print(a//b) #나눈 몫
print(a%b) #나머지

#TODO ex_5) String

a = "python's very good" #문자열
print(type(a))

a = "python's very good \n program language" #이스케이프 코드 \n (다음행으로 줄바꿈)
print(a)

a = """python's very good 
program language""" # """ 줄바꿈 """ 이런식으로 \n과 같은 효과를 볼 수 있다.
print(a)

#문자열 더하기
a = 'Python'
b = 'is good'
print(a+b)

#문자열 곱하기
a = 'Python'
b = 'is good'
print(a * 100)

#TODO ex_6) 인덱싱(Indexing)
a = "Life is too short, You need Python"
print(a[0:4]) #a[이상 : 미만 : 간격]

def is_palindrome(s):
    """Check whether a string is a palindrome"""
    return s == s[::-1]

# %f 실수(float)
# %d 정수(int)
# %s 문자열(string)

a = "I eat %d apples. " % 3
print(a)


number = 10
day = "three"
a = "I ate %d apples. so I was sick for %s days." %(number, day)
print(a)

# 포매팅
name = "kim"
a = f"나의 이름은 {name}입니다."

print(a)

# 공백
a = "%10s" % "hi" # %10s 를 하면 10칸을 띄어 준다.
print(a)

#소수점 자리수 정하여 출력
# %0.4 = %간격.소수점 남기는 자리수
a = "%0.4f" % 3.421234321
print(a)

#count() 문자열 갯수 세기
a = "hobby"
print(a.count('b'))

#find() index의 번호를 찾아서 리턴해줌 없으면 -1 값을 출력한다.
a = "hobby" #01234 => 2
print(a.find('b'))

#upper()는 a라는 문자열을 대문자로 바꿔준다.
a = "hi"
print(a.upper())

#lower()는 반대로 소문자로 바꿔준다.
a = "HI"
print(a.lower())

#strip()은 공백을 없애 준다.
a = "   kim    "
print(a.strip())

#문자열 바꾸기 replace()
a = "Life is too short"
print(a.replace("Life", "Your leg"))

#split() 문자열을 띄어쓰기를 기준으로 나눠서 리스트로 보여준다.
a = "Life is too short"
print(a.split())

#TODO ex_7) 리스트(list)
a = [1,2,"test", "kim", ["nowon","thank you"]]
print(a[4][0])

#리스트(숫자,문자-알파벳순) 정렬
a = [1,5,2,0]
a.sort()
print(a)

#reverse()는 정의한 리스트의 역순으로 출력시킨다.
a = [1,4,2,7,3]
a.reverse()
print(a)

#index() 함수를 이용하여 원하는 리스트의 인덱스 값을 알수 있음
a = [1,3,4]
print(a.index(3))

#insert() 인덱스에 값을 추가
a = [1,3,5]
a.insert(0,4)
print(a)

#remove() 리스트에서 원하는 값을 지움
a = [1,3,4,5]
a.remove(1)
print(a)

#pop() 리스트의 마지막 값을 제외 시킨다.
a = [1, 5, 3]
print(a.pop())
print(a)

#TODO ex) count()를 이용하여 리스트에 원하는 인덱스 값의 갯수를 찾아준다.
a = [1,3,2,5,6,1,1,1]
print(a.count(1))

#extend()를 통하여 리스트의 마지막에 값을 추가
a = [1,3,2,5,6,1,1,1]
a.extend([2,3])
print(a)