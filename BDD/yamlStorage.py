from tinydb import Storage
import yaml



class YAMLStorage(Storage):
    def __init__(self, filename):  # (1)
        self.filename = filename

    def read(self):
        try:
            with open(self.filename) as handle:
                try:
                    data = yaml.load(handle.read())  # (2)
                    return data
                except yaml.YAMLError:
                    return None  # (3)
        except FileNotFoundError:
            return None

    def write(self, data):
        with open(self.filename, 'w') as handle:
            yaml.dump(data, handle, default_flow_style=False)

    def close(self):  # (4)
        pass