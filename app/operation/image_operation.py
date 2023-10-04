import hashlib


def files_to_md5(files: bytes) -> str:
    """
    文件转md5进行简单的校验查重
    :param files:
    :return: md5
    """
    md = hashlib.md5()
    md.update(files)
    res = md.hexdigest()
    return res


if __name__ == '__main__':
    filepath = r"E:\壁纸\wallhaven-6dyv1l_1920x1080.png"
    with open(filepath, 'rb') as f:
        result = f.read()
    print(files_to_md5(result))
