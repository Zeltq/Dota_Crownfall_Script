from flask import Flask, render_template, request
from heroes import heroes_list
from collections import Counter

app = Flask(__name__)

def find_best_heroes(heroes, required_tokens):
    heroes_with_3_tokens = []
    heroes_with_2_tokens = []
    
    required_count = Counter(required_tokens)

    for hero in heroes:
        hero_count = Counter(hero.tokens)

        matching_tokens = sum(min(hero_count[token], required_count[token]) for token in required_count)

        if matching_tokens == 3:
            heroes_with_3_tokens.append(hero.name)
        elif matching_tokens == 2:
            heroes_with_2_tokens.append(hero.name)

    return heroes_with_3_tokens, heroes_with_2_tokens

@app.route('/', methods=['GET', 'POST'])
def index():
    tokens = [
    "Pride",
    "Gluttony",
    "Sloth",
    "Greed",
    "Envy",
    "Wrath",
    "Lust",
    "Discipline",
    "Love",
    "Mischief",
    "Mountain",
    "City",
    "Plains",
    "Desert",
    "Tundra",
    "Cave",
    "Sky",
    "Sea",
    "Forest",
    "Cosmos",  
]  # Список жетонов
    tokens.sort()
    heroes_with_3_tokens = []
    heroes_with_2_tokens = []

    if request.method == 'POST':
        selected_tokens = request.form.getlist('tokens')
        # Удаляем пустые значения из списка выбранных жетонов
        selected_tokens = [token for token in selected_tokens if token]
        heroes_with_3_tokens, heroes_with_2_tokens = find_best_heroes(heroes_list, selected_tokens)

    return render_template('index.html', tokens=tokens, heroes_with_3_tokens=heroes_with_3_tokens, heroes_with_2_tokens=heroes_with_2_tokens)

if __name__ == '__main__':
    app.run(debug=True)