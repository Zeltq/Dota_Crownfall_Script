from flask import Flask, render_template, request, session
from heroes import heroes_list
import secrets
from main import find_best_heroes

secret_key = secrets.token_urlsafe(32)
app = Flask(__name__)

app.secret_key = secret_key


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
    selected_tokens = []

    if request.method == 'POST':
        selected_tokens = request.form.getlist('tokens')
        # Удаляем пустые значения из списка выбранных жетонов
        selected_tokens = [token for token in selected_tokens if token]
        heroes_with_3_tokens, heroes_with_2_tokens = find_best_heroes(heroes_list, selected_tokens)
        session['selected_tokens'] = selected_tokens
    elif 'selected_tokens' in session:
        selected_tokens = session['selected_tokens']

    num_selects = 10
    token_options_list = []
    for i in range(num_selects):
      token_options = [{'value': token, 'selected': token == selected_tokens[i] if i < \
                        len(selected_tokens) else False} for token in tokens]
      token_options_list.append(token_options)

    return render_template('index.html', tokens=token_options_list, heroes_with_3_tokens=\
                           heroes_with_3_tokens, heroes_with_2_tokens=heroes_with_2_tokens)

if __name__ == '__main__':
    app.run(debug=True)