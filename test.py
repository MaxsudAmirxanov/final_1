import uuid
import os
print(uuid.uuid4())

# for filename in os.listdir(path ='Users\HP\Desktop\final_1'):
#     # print (filename)
#     pass

book = os.listdir(path='book')
print(book)

# dirnum = 0
# filenum = 0
# path = 'Путь к целевой папке'
 
# for lists in os.listdir(path):
#     sub_path = os.path.join(path, lists)
#     print(sub_path)
#     if os.path.isfile(sub_path):
#         filenum = filenum+1
#     elif os.path.isdir(sub_path):
#         dirnum = dirnum+1
 
# print('dirnum: ',dirnum)
# print('filenum: ',filenum)
 

