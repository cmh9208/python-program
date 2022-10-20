'''
과일 판매상에서 메뉴를 진열하는 어플을 제작하고자 합니다.
입력되는 값은 없다.
다만 실행했을 때 출력되는 결과는 다음과 같다.
### 과일번호표 ###
********************************
1번과일: 바나나
2번과일: 사과
3번과일: 망고
********************************
구매할 과일: 바
'''
class Fruits(object):
    def __init__(self,name):
      self.menu = ["바나나", "사과", "망고"]
      self.name = name
    
    def pprint(self):
        print("### 과일번호표 ###")
        print("*"*40)
        if self.name[:1] == "바":
            print(f'1번과일: {"바나나"}')
        elif self.name[:1] == "사":
            print(f'2번과일: {"사과"}')    
        elif self.name[:1] == "망":
            print(f'3번과일: {"망고"}')   
        print("*"*40)

    @staticmethod
    def ddd():
        name = input("구매할 과일: ")
        ddd = Fruits(name)
        ddd.pprint()

Fruits.ddd()