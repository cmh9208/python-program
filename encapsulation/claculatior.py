'''디스크(세이브된 객체)'''
class Calaulator(object):
    def __init__(self, num1, op, num2):
        self.num1 = num1
        self.op = op
        self.num2 = num2 
        
    def ex(self):
        '''지역변수 = 전역변수'''
        num1 = self.num1  
        op = self.op
        num2 = self.num1

        if self.op == "+":
           result = num1 + num2
        elif self.op == "-":
             result = num1 - num2
        elif self.op == "*":
             result = num1 * num2
        elif self.op == "/":
             result = num1 / num2
        elif self.op == "%":
             result = num1 % num2
        else:
            result = "잘못된 연산입니다"
            print(f'{num1} {self.op} {num2} = {result}')

    @staticmethod
    def main():
          num1 = int(input("숫자 : "))
          op = input("+,-,*,/,% : ")
          num2 = int(input("숫자 : "))
          calaulator = Calaulator(num1, op, num2)
          calaulator.ex()
          
Calaulator.main()

'''메모리(로딩된 객체)'''       