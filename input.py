class Input():
    def __init__(self, file_name):
        self.file_name = file_name
        self.read_file();

    def read_file(self):
        """
        Read files & return array
        """
        docs = []

        with open(self.file_name) as f:
            for line in f:
                items = line.strip().split()
                docs.append(items)

        return docs 

