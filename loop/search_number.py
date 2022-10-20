'''
랜덤숫자 10개를 뽑아서
사용자가 검색하는 숫자의 배수만 출력하는
프로그램을 개발하시오
예)[12, 23, 28...]
사용자의 input 값이 12인 경우
출력값이 12, 48만 되도록한다.
'''
from random_list import Random_List

class Search_number(object):
    def __init__(self, num) -> None:
        self.num = num
    
    def print(self):
        rl = Random_List()
        a = rl.get_random(1,100, 10)
        print(a)
        for i in a:
            if i % self.num == 0:
                print(i)
        
    @staticmethod
    def main():
        num = int(input("숫자입력: "))
        sn = Search_number(num)
        sn.print()

Search_number.main()