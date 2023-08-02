# извлекает информацию об объектах (как каталогах, так и файлах)
import os
from . import size_bit


def get_objects(directory):
    objects = []
    for root, dirs, files in os.walk(directory):
        parent = os.path.dirname(root)
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            size = size_bit.get_size(dir_path)
            objects.append({"name": dir, "type": "directory", "parent": parent, "size": size})
        for file in files:
            file_path = os.path.join(root, file)
            size = size_bit.get_size(file_path)
            objects.append({"name": file, "type": "file", "parent": parent, "size": size})
    return objects