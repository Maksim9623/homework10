import json


def load_candidates():
    with open('candidates.json', 'r', encoding='utf-8') as file:
        date = json.load(file)
        candidates = {}
        for i in date:
            candidates[i['id']] = i
        # print(candidates)
        return candidates


load_candidates()
