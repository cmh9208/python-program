from random_list import Random_List

class Odd_even(object):
    def __init__(self) -> None:
        pass

    def print(self):
        rl = Random_List()
        print(rl.get_random(10,100,10))
        for i in rl.get_random(10,100,10):
            if i % 2 == 0:
                print(f"짝수: {i}")
            else:
                print(f"홀수: {i}")

    @staticmethod
    def main():
        odd = Odd_even()
        odd.print()
        
Odd_even.main()