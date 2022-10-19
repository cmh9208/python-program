'''
국어. 영어, 수학점수를 입력받아서 학점을 출력하는 프로그램을 완성하시오.
각 과목 점수는 0 ~ 100 사이이다.
평균에 따라 다음과 같이 학점이 결정된다
90이상은 A학점
80이상은 B학점
70이상은 C학점
60이상은 D학점
50이상은 E학점
그 이하는 F학점
출력되는 결과는 다음과 같다.
### 성적표 ###
********************************
이름 국어 영어 수학 총점 평균 학점
*******************************
홍길동 90 90 92 272 90.6 A
********************************
'''                                       # 인스턴스는 클래스 안에  
class Grade(object):                      # 생성자는 인스턴스를 만든다.
    def __init__(self, name, ko, en, ma): # 생성자(클래스안)로 들어간 데이터는 property가 된다.
        self.name = name
        self.ko = ko
        self.en = en
        self.ma = ma
    
    def get_total(self):
        return self.ko + self.en + self.ma

    def get_avg(self):
        return self.get_total() / 3

    def grade(self):
        avg = self.get_avg()
        h = ""
        if avg >= 90: h = "A학점"
        elif avg >= 80: h = "B학점"
        elif avg >= 70: h = "C학점"
        elif avg >= 60: h = "D학점"
        elif avg >= 50: h = "E학점"
        else: h = "F학점"
        return h

    def print_grade(self):
        name = self.name
        ko = self.ko
        en = self.en
        ma = self.ma
        title = "### 성적표 ###"
        astar = "*"*40
        schema = "이름 국어 영어 수학 총점 평균 학점"
        velues = f"{name} {ko} {en} {ma} {self.get_total()} {self.get_avg()} {self.grade()}"
        print(f"{title}\n{astar}\n{schema}\n{astar}\n{velues}\n{astar}")

    @staticmethod # 스태틱은 클래스것이 아님
    def main():
        name = input("이름: ")
        ko = int(input("국어: "))
        en = int(input("영어: "))
        ma = int(input("수학: "))
        grade = Grade(name, ko, en, ma) # 인스턴스 = 생성자다
        grade.print_grade()
        
Grade.main()