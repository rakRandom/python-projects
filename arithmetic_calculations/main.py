import random as rnd


def get_random_calc(vals: dict) -> tuple[str, int]:
    question: list[str | int] = list()
    answer: int = 0
    operation: int
    number: int

    def get_number():
        if operation == 4:
            return rnd.randint(1, tuple(vals.values())[operation])
        return rnd.randint(0, tuple(vals.values())[operation])

    number = rnd.randint(0, tuple(vals.values())[1])
    question.append(number)
    answer += number

    for _ in range(vals["t"] - 1):
        operation = rnd.randint(1, 4)
        number = get_number()

        c = 0
        while operation == 4 and (answer / number) % 1 != 0 and c < 10:
            number = get_number()
        if c == 10:
            operation = rnd.randint(1, 3)

        question.append("+-*/"[operation-1])
        question.append(number)

        if operation == 1:
            answer += number
        elif operation == 2:
            answer -= number
        elif operation == 3:
            answer *= number
        elif operation == 4:
            answer /= number

    return " ".join(map(str, question)), answer


def main():
    user_difficulty_selection: int = 0
    game_over: bool = False
    score: int = 0
    question: str
    correct_answer: int
    player_answer: int

    print("Welcome to the Math Game.\nAnswer the arithmetic questions in sequential order (without PEMDAS).")

    while user_difficulty_selection not in (1, 2, 3):
        user_difficulty_selection = int(input("Select a difficulty:\n[1] Easy\n[2] Medium\n[3] Hard\n: "))

    print("\n")

    while not game_over:
        question, correct_answer = get_random_calc(DIFFICULTIES[user_difficulty_selection - 1])

        print(f"Score: {score}")
        player_answer = int(input(f"Question: {question} = ?\n: "))

        if player_answer == correct_answer:
            print("You got it.")
            score += 1
        else:
            print("How can you be so dumb?")
            score -= 1

        game_over = score < 0

    print("See ya!")


if __name__ == '__main__':
    DIFFICULTIES = [
        {"t": 2, "+": 100, "-": 100, "*": 10, "/": 10},
        {"t": 4, "+": 500, "-": 250, "*": 25, "/": 15},
        {"t": 8, "+": 2000, "-": 1000, "*": 50, "/": 25}
    ]

    main()
