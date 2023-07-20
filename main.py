from utils import load_random_word
from player import Player

def main():

    player = Player(input("Введите свое имя: "))
    word = load_random_word()


    while True:


        print(f"загаданое слово: {word}")
        print(f"всего ответов:{word.count_subwords()}")
        user_word = input("Введите ответ: ")

        if len(user_word) < 3:
            print("Слово слишком короткое")
            continue

        if user_word in ("стоп", "stop"):
            print("принудительное завершение")
            break

        if word.check_input(user_word):
            print("Ответ верный вы получаете 1 балл")
            continue

        if not word.check_input(user_word):
            print("Ответ не верный")
            continue

        if player.check_answers(user_word):
            print("такое слово уже есть")
            continue

        if word.count_subwords() == word.count_answers(user_word):
            print("Конец")
            break




# нужна проверка что слово есть в списке ответов
# если угаданое слово коректно то добавляем в список пользователя
# если кол-во угаданы слов пользователя = кол-во загаданых слов то игра завершаеться

if __name__ == "__main__":
    main()