import random
class Bubble(object):
    def __init__(self) -> None:
        pass

    def extract_random(self):
        return random.sample(range(1,101), 100)

    def excute_bubble(self):
        for i in self.extract_random():
            if i % 2 == 0:
                print(i)
        
    @staticmethod
    def main():
        bubble = Bubble()
        bubble.excute_bubble()

Bubble.main()

