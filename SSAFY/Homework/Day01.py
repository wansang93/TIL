# 데일리실습 1-1. 제어문 기초
class FactorialLoop01:

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
        while True:
            # TODO: 랜덤값 해결하기
            break


if __name__ == '__main__':
    FactorialLoop01.day01_01(3)
