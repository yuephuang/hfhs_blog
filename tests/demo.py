import hashlib

filepath = r"E:\壁纸\wallhaven-6dyv1l_1920x1080.png"
file = open(filepath, "rb")
md = hashlib.md5()
md.update(file.read())
res1 = md.hexdigest()
print(res1)
