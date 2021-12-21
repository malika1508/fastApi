# my_posts = [
#     {"title" : "favorit food", "content":"pizza carree", "id" : 1},
#     {"title" : "favorit car", "content":"pink atos", "id" : 2},
#     {"title" : "favorit house", "content":"nice house", "id" : 3},
# ]
# print(list(filter(lambda post :  post['id'] == 5, my_posts)))

import psycopg2

conn = psycopg2.connect(host = 'localhost', database = 'fastApi', user = 'postgres', password = 'Bellas 19')

print(conn)