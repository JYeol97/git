# 중괄호를 사용 key : value 를 :를 사용하여 구분함
dic = {'name' : 'pey', 'phone' : '010-9220-1761', 'birth' : 1110}
print(dic)
print(type(dic))

a = {1: 'hi'}
print(a)

a = {'a': 'hi'}
print(a)

a = {1: 'a'}
a[2] = 'b' # a에 2라는 key를 추가하고 벨류를 'b'추가한다 리스트에선 바꿔주는 개념이지만 딕셔너리에선 추가하는 개념
print(a)

#ex
a = {'임재열': '앙 김호취'}
a['임재똥'] = '잉 김호취'
print(a)

a = {1: 'a', 2: 'b', 'name': 'pey', 3: [1, 2, 3]}
# del a[key]
del a['name']
print(a)
print(a[1])

grade = {'pey': 10, 'julliet': 99}
print(grade['pey']) # gared[]를 사용하면 그 key에 해당하는 value를 획득가능


dic = {'name' : '28', 'phone' : '010-9220-1761', 'birth' : 1110}
print(dic['name'], dic['birth'])

a = {'name' : 'pey', 'phone' : '010-9220-1761', 'birth' : 1110}
print(a.keys()) # key만 가져오기
print(list(a.keys()))

a = {'name' : 'pey', 'phone' : '010-9220-1761', 'birth' : 1110}
for k in a.keys(): # key를 깔끔하게 가져오기
    print(k)

a = {'name' : 'pey', 'phone' : '010-9220-1761', 'birth' : 1110}
print(a.items()) # (key, value) 쌍으로 얻기

a = {'name' : 'pey', 'phone' : '010-9220-1761', 'birth' : 1110}
a.clear()

print(a) # 안에 값을 모두 날린다

a = {'name' : 'pey', 'phone' : '010-9220-1761', 'birth' : 1110}
print(a['name'])
print(a.get('hi', "값이 없습니다")) # get 함수는 없어도 none으로 값이 나옴 "값이 없습니다" 로 바꿔서 나오는것도 확인

a = {'name' : 'pey', 'phone' : '010-9220-1761', 'birth' : 1110}
print('name'in a) # name 이라는 key가 a안에 있니? 물어보는것

# 아래 두개는 개념이 비슷함
a = [1, 2, 3] # 리스트
print(a[0]) 

a = {0:1, 1:2, 2:3} # 딕셔너리
print(a[0])

