from collections import Counter
from heroes import heroes_list


def find_best_heroes(heroes, required_tokens):
    best_heroes = []
    max_tokens = 0

    required_count = Counter(required_tokens)

    for hero in heroes:
        hero_count = Counter(hero.tokens)

        matching_tokens = sum(min(hero_count[token], required_count[token]) for token in required_count)

        if matching_tokens > max_tokens:
            max_tokens = matching_tokens
            best_heroes = [hero.name]
        elif matching_tokens == max_tokens:
            best_heroes.append(hero.name)

    return best_heroes, max_tokens

def main(heroes_list):


    required_tokens = input("Enter the required tokens separated by a space: ").split(",")

    required_tokens = [token.strip().capitalize() for token in required_tokens]

    best_heroes, max_tokens = find_best_heroes(heroes_list, required_tokens)

    print(f"Best heroes: {', '.join(best_heroes)} you can get: {max_tokens} tokens if you win")

if __name__ == "__main__":
    main(heroes_list)
