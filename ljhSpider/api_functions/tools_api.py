import json
import chardet


# 分割列表
def chunks(data_list, chunk_size):
    """
    :param data_list: 列表
    :param chunk_size: 每个子列表的长度
    :return: 大列表包小列表[[], [], [], []......]
    """
    for i in range(0, len(data_list), chunk_size):
        yield data_list[i : i + chunk_size]


def read_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.loads(f.read())


def read_txt(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.readlines()


# 获取文件的编码格式
def get_encoding(path):
    with open(path, "rb") as file:
        data = file.read()
    return chardet.detect(data)["encoding"]
