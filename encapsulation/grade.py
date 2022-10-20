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
홍길동 90 90 92 272 90.6 A
홍길동 90 90 92 272 90.6 A
********************************
'''                                         
class Grade(object):                      
    def __init__(self, name, ko, en, ma): 
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
        astar = "*"*40
        schema = "이름 국어 영어 수학 총점 평균 학점"
        velues = f"{name} {ko} {en} {ma} {self.get_total()} {self.get_avg()} {self.grade()}"
        print(f"{schema}\n{velues}\n{astar}")

    @staticmethod
    def get_grade(ls):
        for i in ls:
            i.print_grade()

    @staticmethod
    def new_grade():
        name = input("이름: ")
        ko = int(input("국어: "))
        en = int(input("영어: "))
        ma = int(input("수학: "))
        return Grade(name, ko, en, ma)

    @staticmethod
    def print_menu():
        print("1. 성적표 등록")
        print("2. 성적표 출력")
        print("3. 성적표 삭제")
        print("4. 성적표 종료")
        menu = input("메뉴선택")
        return int(menu)

    @staticmethod # 스태틱은 클래스것이 아님
    def main():
        ls = []
        while True:
            menu = Grade.print_menu()
            if menu == 1:
                print("### 성적표 등록 ###")
                grade = Grade.new_grade()
                ls.append(grade)
            elif menu == 2:
                print("### 성적표 출력 ###")
                grade.get_grade(ls) 
            elif menu == 3:
                print("### 성적표 삭제 ###")
            elif menu == 4:
                print("### 성적표 어플 종료 ###")
                break
            # 숫자 아니면 되돌아가게
        
Grade.main()