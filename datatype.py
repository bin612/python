#튜플은 변경할 수 없는 값
t1 = (1,2, 'a','b')
# 슬라이싱을하여 볼 수는 있다.
print(t1[0])

t1 = (1,2, 'a','b')
t2 = (3,4)

# 더하여 새로운 튜블은 만들어 낸 것이다.
print(t1+t2)

# 튜플 자료형
t1 = (1,2, 'a','b')
print(t1[0] + 1)
a = (1,2)
a = a * 3

# (1,2) 자체가 3번 곱해져서 나오게 된다.
print(a)

# 딕셔너리
dic = {'name' : 'Kimbaul', 'age' : 15}

print(dic['name'])

# 딕셔너리 쌍 추가하기
a = {1: 'a'}
# 추가 key value
a['name'] = "노원"

# 삭제  del로 삭제
# del  value = a 안에 key 1 삭제
del a[1]

print(a)

a = {1: 'a', 1: 'b'}


a = {1 : '노원', 2 : '서울', 3 : '경기도'}

# key를 뽑는 함수(keys()) 실행
# value를 뽑는 함수(values()) 실행
# item을 뽑는 함수(items()) 실행
print(a.keys())
print(a.values())
print(a.items())

for k in a.keys():
    print(k)

for k in a.values():
    print(k)

for k in a.items():
    print(k)

# 실제 예제 순서대로 출력
for k, v in a.items():
    print("키는: " + str(k))
    print("벨류는: " + v)

b = {1 : '노원', 2 : '서울', 3 : '경기도'}
b.clear()

# clear하고 비어 있는 딕셔너리
print(b)

# get을 사용하면 딕셔너리에 없는 값이 있으면 그에 대한 none 값을 알려준다.
a = {1 : '노원', 2 : '서울', 3 : '경기도'}
print(a.get(4, '없음'))

# 4라는 key가 a라는 딕셔너리에 포함되어 있는가
print(4 in a)

# 1라는 key가 a라는 딕셔너리에 포함되어 있는가
print(1 in a)

# 중복이 없어야 한다.
# set() 집합이라는 뜻이다.
s1 = set([1,2,3])
s1 = {1,2,3}
print(type(s1))

l = [1,2,2,3,3]
newList = list(set(l))

# 중복을 제거한 나머지 값들을 보여준다.
print(newList)

# 문자를 집합으로 만들어 출력해준다. (집합으로 들어가게 된다면 쪼개지면서 나열 된다.)
s1 = set("hello")
print(s1)

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

# s1 과 s2의 교집합인(&) 부분들을 보여주게 된다.
print(s1 & s2)

#다른 방법으로 교집합(intersection()) 이라는 함수가 있다.
print(s1.intersection(s2))

# 합집합 ( | )

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

# 중복 없이 합집합이 출력된다.
print(s1 | s2)

