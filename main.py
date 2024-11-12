from collections import Counter
from heroes import heroes_list


def find_best_heroes(heroes, required_tokens):
    best_heroes = []
    max_tokens = 0

    # Подсчитываем количество необходимых жетонов
    required_count = Counter(required_tokens)

    for hero in heroes:
        # Подсчитываем жетоны героя
        hero_count = Counter(hero.tokens)

        # Считаем количество жетонов, которые есть у героя и которые нужны пользователю
        matching_tokens = sum(min(hero_count[token], required_count[token]) for token in required_count)

        if matching_tokens > max_tokens:
            max_tokens = matching_tokens
            best_heroes = [hero.name]
        elif matching_tokens == max_tokens:
            best_heroes.append(hero.name)

    return best_heroes, max_tokens

def main(heroes_list):
    # Пример списка героев

    # Ввод жетонов, которые нужны пользователю
    required_tokens = input("Введите жетоны, которые вам нужны (через запятую): ").split(",")

    # Убираем лишние пробелы
    required_tokens = [token.strip() for token in required_tokens]

    best_heroes, max_tokens = find_best_heroes(heroes_list, required_tokens)

    print(f"Лучшие герои: {', '.join(best_heroes)} с количеством жетонов: {max_tokens}")

if __name__ == "__main__":
    main(heroes_list)
