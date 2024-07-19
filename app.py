from flask import Flask
from utils import get_all, get_by_pk, get_by_skill

app = Flask(__name__)

@app.route('/')
def index():
    """Главная страница"""
    candidates = get_all()
    result = '<pre>'
    for candidate in candidates:
        result += f"Имя кандидата - {candidate['name']}\n"
        result += f"Позиция кандидата - {candidate['position']}\n"
        result += f"Навыки - {candidate['skills']}\n\n"
    result += '</pre>'
    return result


@app.route('/candidates/<int:pk>')
def candidate_profile(pk):
    """Поиск профиля кандидата по pk"""
    candidate = get_by_pk(pk)
    if not candidate:
        return 'Кандидат не найден'

    result = f"<img src='{candidate['picture']}'>\n<pre>\n"
    result += f"Имя кандидата - {candidate['name']}\n"
    result += f"Позиция кандидата - {candidate['position']}\n"
    result += f"Навыки - {candidate['skills']}\n"
    result += '</pre>'
    return result


@app.route('/skills/<skill>')
def candidates_by_skill(skill):
    """Поиск профилей кандидатов по навыку"""
    candidates = get_by_skill(skill)
    if not candidates:
        return 'Кандидаты не найдены'

    result = '<pre>'
    for candidate in candidates:
        result += f"Имя кандидата - {candidate['name']}\n"
        result += f"Позиция кандидата - {candidate['position']}\n"
        result += f"Навыки - {candidate['skills']}\n\n"
    result += '</pre>'
    return result

app.run()


