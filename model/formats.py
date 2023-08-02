import json
import csv
import pickle
from . import objects_directory


# сохранение в JSON
def save_as_json(directory, output_file):
    objects = objects_directory.get_objects(directory)
    with open(output_file, 'w') as f:
        json.dump(objects, f)


# сохранение в CSV
def save_as_csv(directory, output_file):
    objects = objects_directory.get_objects(directory)
    with open(output_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["name", "type", "parent", "size"])
        writer.writeheader()
        writer.writerows(objects)


# сохранение в PICKLE
def save_as_pickle(directory, output_file):
    objects = objects_directory.get_objects(directory)
    with open(output_file, 'wb') as f:
        pickle.dump(objects, f)