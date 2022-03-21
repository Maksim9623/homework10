from flask import Flask
import utils

app = Flask(__name__)
candidates = utils.load_candidates()


@app.route('/', )
def page_index():
    representation = '<pre>'
    for candidate in candidates.values():
        representation += f"'Имя кандидата -' {candidate['name']} \n'Позиция кандидата -'{candidate['position']} \n'Навыки через запятую -'{candidate['skills']}\n\n"
    representation += '<pre>'
    return representation


@app.route('/candidate/<int:id>')
def page_profile(id):
    candidate = candidates[id]
    rep_profile = f"<img src={candidate['picture']}> <br><br>'Имя кандидата -' {candidate['name']} <br>'Позиция кандидата -' {candidate['position']} <br>'Навыки через запятую -' {candidate['skills']}<br><br>"
    return rep_profile


@app.route('/skills/<skill>')
def page_skills(skill):
    representation = '<pre>'
    for candidate in candidates.values():
        candidates_skills = candidate['skills'].split(', ')
        candidates_skills = [x.lower() for x in candidates_skills]
        if skill in candidates_skills:
            representation += f"'Имя кандидата -' {candidate['name']} \n'Позиция кандидата -' {candidate['position']} \n'Навыки через запятую -' {candidate['skills']}\n\n"
    representation += '</gitpre>'
    return representation


app.run()
