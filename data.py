player = {
    'name': '',
    'armor': 0.95,
    'hp': 100,
    'attack': 20,
    'luck': 5,
    'money': 1000,
    'inventory': []
}

enemies = [
    {
        'name': 'Бражник', 
        'hp': 50,
        'attack': 10,
        'script': 'Ты не должен быть здесь! Я сделаю из тебя бабочку за то, что явился(ась) сюда!',
        'win': 'Я сделал это! Иди поплачь.',
        'loss': 'Ну и ладно, пойду поплачу'
    },
    {
        'name': 'Винни Пух',
        'hp': 70,
        'attack': 25,
        'script': 'Как ты тут оказался? Я должен защитить свои запасы меда!',
        'win': 'Я съем весь мед этого мира, но с тобой больше не поделюсь.',
        'loss': 'А я думал мы друзья, но видимо только я так считал...'
    },

    {
        'name': 'Соловей-разбойник',
        'hp': 90,
        'attack': 50,
        'script': 'Ты посмел явиться на мою территорию, значит ты не выйдешь отсюда живым(ой).',
        'win': 'Я всегда сдерживаю свои обещания.',
        'loss': 'Как же так...'
    }
]

items = {
    "1" : {
        "name" : "Зелье удачи",
        "price" : 1500
    },
    "2" : {
        "name" : "Пропуск тренировки",
        "price" : 1000
    }
}