# 데일리실습 1-1. 제어문 기초
class FactorialLoop:

    def day01_01(N):
        result = 1
        for i in range(1, N+1):
            result *= i

        print(f'{N}! = {result}')


# 데일리실습 1-2. 조건 & 반복문
import random
class UpAndDown:

    def day01_02():
        number = random.randint(1, 101)
        cnt = 0
        while True:
            print("숫자를 추측해 주세요!")
            n = int(input())
            cnt += 1
            if n == number:
                print(f"정답입니다! {cnt}번만에 해결했습니다.")
                break
            elif n > number:
                print(f"{n}보다 작은 수를 입력하세요. {cnt}번 시도하였습니다.")
            else:
                print(f"{n}보다 큰 수를 입력하세요. {cnt}번 시도하였습니다.")


# 데일리실습 1-3. 기본 문법 응용
class DegitTest1:
    
    def day01_03():
        n = 1
        for i in range(5):
            print("   " * i, end="")
            for j in range(i, 5):
                print(f"{n:3d}", end="")
                n += 1
            print()


class DegitTest2:

    def day01_03():
        n = 1
        NUM = 17
        while n <= NUM:
            print(f"{n:3d}", end="")

            n += 1

# 1 2 3 4 5
# 2 1 0 1 2
# 5 3 1 3 5
# 0 1 2 1 0

import random
class GameTest:

    def day01_03():
        pass


if __name__ == '__main__':
    # FactorialLoop.day01_01(3)
    # UpAndDown.day01_02()
    # DegitTest1.day01_03()
    DegitTest2.day01_03()
    # GameTest.day01_03()
