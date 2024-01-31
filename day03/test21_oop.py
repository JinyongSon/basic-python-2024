# file: test21_oop.py
# desc: 객체지향 클래스 만들기

# 클래스(사람이라는 객체를 만들기 위한 청사진) 만들기
class Person: # 사람 클래스 선언
    name = '' # 멤버변수 
    age = 0
    gender = ''

    # 생성자 함수(스페셜 함수) 클래스의 객체를 생성할때
    def __init__(self) -> None:
        pass

    # 멤버함수
    def walk(self): # 멤버함수 매개변수 self 필수!
        print(f'{self.name}이(가) 걷습니다.')

    def stop(self):
        print(f'{self.name}이(가) 멈춥니다.')


# 사람 객체 생성, instance(사례, 예제)
mg = Person() # 함수호출처럼 사용하면 됨
es = Person()
# print(type(mg))
# print(id(mg)) # 다른 객체인지 확인
# print(id(es))

mg.name = '손진용' # 객체명.멤버변수 = ...
mg.age = 26
mg.gender = '남'

es.name = '애슐리'
es.age = 40
es.gender = '여자'

print(f'mg => 이름:{mg.name} / 나이:{mg.age} / 성별:{mg.gender}')
print(f'es => 이름:{es.name} / 나이:{es.age} / 성별:{es.gender}')

mg.walk()
print('1분동안 걷는다')
mg.stop()

es.walk()
print('걷기 싫어함')
es.stop()