import os

path = r'C:\Users\ivano\Desktop\Project1\Total'
# path = os.path.normpath(path)
# for root, dirs, files in os.walk(path):
#     if root == path:
#         print(root, dirs, files, path)

full_path = os.path.abspath('proba.txt')
print(full_path)