import os 
# Задание 1
# print("Текущая директория", os.getcwd())
# print(os.uname())
# # if not os.path.exists("09dz"):
# #     os.mkdir("09dz")
# # os.makedirs(os.path.join("09dz", "txt_1", "py_1"))
# # f = open("text.txt", "w", encoding= "utf-8")
# # f_1 = open("file1.py", "w", encoding= "utf-8")

# import glob
# import shutil
# # extensions = {
# #     "txt": "text",
# #     "py": "piton"
# # }
# # path = ""

# # for extensions, folder_name in extensions.items():
# #     files = glob.glob(os.path.join(path, f"*.{extensions}"))
# #     if not os.path.isdir(os.path.join(path, folder_name)) and files:
# #         os.mkdir(os.path.join(path, folder_name))
# #     for file in files:
# #         basename = os.path.basename(file)
# #         dst = os.path.join(path, folder_name, basename)
# #         print(f"[*] Перенесен файл '{file} в {dst}")
# #         shutil.move(file, dst)


# # это мне стоило титанических усилий хоть и с помощью гугла. прошу подробнее про перенос файлов по папкам по расширениям


# os.chdir("text")
# os.rename("text.txt", "renametext.txt")

# Задание 2

import json
with open("employees.json", "r") as json_file:
    data = json.load(json_file)
    print(type(data), data)