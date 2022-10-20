from random_list import Random_List

class Bubble(object):
    def __init__(self) -> None:
        pass

    def print_bubble(self):
        rl = Random_List()
        ls = rl.get_random(10,100,10)
        print(ls)
        for i in range(len(ls)-1):
            for j in range(len(ls)-1):
                if ls[j] > ls[j+1]:
                    ls[j], ls[j+1] = ls[j+1], ls[j]
                    
        print("*"*30)
        print(ls)
        
    @staticmethod
    def main():
        bubble = Bubble()
        bubble.print_bubble()

Bubble.main()