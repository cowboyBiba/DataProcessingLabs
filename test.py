import json
string = "[{'id': 0, 'question': 'Тестовый вопрос', 'answer': 'Тестовый ответ', 'possible_feedback': 'тут будет ссылка/фидбек', 'max_value': 2}, {'id': 1, 'question': 'Тестовый вопрос 2', 'answer': 'Тестовый ответ 2', 'possible_feedback': 'тестовый фидбек 2', 'max_value': 2}]"

j = json.loads(string.replace("'", '"'))
print(j)