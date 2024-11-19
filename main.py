from collections import Counter
from heroes import heroes_list


def find_best_heroes(heroes, required_tokens):
    heroes_with_3_tokens = []
    heroes_with_2_tokens = []
    
    required_count = Counter(required_tokens)

    for hero in heroes:
        hero_count = Counter(hero.tokens)

        matching_tokens = sum(min(hero_count[token], required_count[token]) \
                              for token in required_count)

        if matching_tokens == 3:
            heroes_with_3_tokens.append(hero.name)
        elif matching_tokens == 2:
            heroes_with_2_tokens.append(hero.name)

    return heroes_with_3_tokens, heroes_with_2_tokens


def main(heroes_list):
    required_tokens = input("Enter the required tokens separated by a space: ").split(",")

    required_tokens = [token.strip().lower().capitalize() for token in required_tokens]

    heroes_with_3_tokens, heroes_with_2_tokens = find_best_heroes(heroes_list, required_tokens)

    print(f"Heroes with 3 matching tokens: \n\n{', '.join(heroes_with_3_tokens) \
                                                if heroes_with_3_tokens else 'None'}")
    print("\n--------------")
    print(f"Heroes with 2 matching tokens: \n\n{', '.join(heroes_with_2_tokens) \
                                                if heroes_with_2_tokens else 'None'}")
    print("\n--------------")

if __name__ == "__main__":
    main(heroes_list)

