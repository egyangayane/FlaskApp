import json


def load_candidates():
    """Получает данные из json-файла и возвращает их в виде словаря"""
    with open('candidates.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def get_all():
    """Возвращает преобразованные данные json-файла"""
    return load_candidates()


def get_by_pk(pk):
    """Получает данные кандидата по pk"""
    for candidate in load_candidates():
        if candidate['pk'] == pk:
            return candidate
    return None


def get_by_skill(skill_name):
    """Получает данные кандидатов по навыку"""
    skill_name = skill_name.lower()
    candidate_by_skills = []
    for candidate in load_candidates():
        if skill_name in candidate['skills']:
            candidate_by_skills.append(candidate)
    return candidate_by_skills

