import yaml

class Loader:
    def __init__(self, file_path):
        self._file_path = file_path

    def load_yaml(self):
        result = {}
        with open(self._file_path, "r") as stream:
            try:
                result = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print("Error loading YAML file {file}: {error}".format(file=self.file_path, error=exc))
                exit(0)
        return result