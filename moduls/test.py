from requests import get, post, delete

# print(get('http://localhost:5000/api/v2/users').json())
# print(get('http://localhost:5000/api/v2/users/1').json())
# print(get('http://localhost:5000/api/v2/users/3').json())
# print(post('http://localhost:5000/api/v2/users',
#            json={'name': 'Яндекс',
#                  'about': 'lyceum',
#                  'email': 'yandex_li@yandex.ru',
#                  'password': '123'}).json())
# print(get('http://localhost:5000/api/v2/users').json())
# print(delete('http://localhost:5000/api/v2/users/5').json())
# print(delete('http://localhost:5000/api/v2/users/2').json())
# print(get('http://localhost:5000/api/v2/users').json())
# print(post('http://localhost:5000/api/v2/users',
#            json={'name': 'Яндекс',
#                  'about': 'lyceum',
#                  'password': '123'}).json())

print(post('http://localhost:5000/api/v2/news',
           json={'title': 'Заголовок',
                 'content': 'Текст новости',
                 'is_private': True,
                 'is_published': True,
                 'user_id': 'hghgf'}).json())
# print(get('http://localhost:5000/api/news/999').json())
# print(get('http://localhost:5000/api/news/q').json())
# print(post('http://localhost:5000/api/news').json())
#
# print(post('http://localhost:5000/api/news',
#            json={'title': 'Заголовок'}).json())
#
# print(post('http://localhost:5000/api/news',
#            json={'title': 'Заголовок',
#                  'content': 'Текст новости',
#                  'user_id': 1,
#                  'is_private': False}).json())
# print(get('http://localhost:5000/api/news').json())

# print(delete('http://localhost:5000/api/news/999').json())
# # новости с id = 999 нет в базе
#
# print(delete('http://localhost:5000/api/news/1').json())