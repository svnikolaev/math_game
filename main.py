from random import choice, randint


class MathGame:
    def __init__(self):
        self.maths = [
            self.addition_test,
            self.subtraction_test,
            self.multiplication_test
        ]

    def turn(self):
        first = randint(0, 10)
        second = randint(0, 10)
        question, answer = choice(self.maths)(first, second)
        print(question)
        return print(bool(answer == int(input())))

    @staticmethod
    def addition_test(first: int, second: int) -> tuple:
        return (
            f'{first} + {second}',
            first + second
        )

    @staticmethod
    def subtraction_test(first: int, second: int) -> tuple:
        return (
            f'{first} - {second}',
            first - second
        )

    @staticmethod
    def multiplication_test(first: int, second: int) -> tuple:
        return (
            f'{first} * {second}',
            first * second
        )


def main():
    math_game = MathGame()
    for i in range(1, 11):
        math_game.turn()


if __name__ == "__main__":
    main()
