import json
import os

class ProblemSetLoader:

    def load_problem_set(self, file_path):
        """Load the problem set from a given file path."""
        extension = os.path.splitext(file_path)[1]
        if extension == ".json":
            with open(file_path, 'r') as file:
                return json.load(file)
        elif extension == ".txt":
            # Implement a parser for text files if necessary
            pass
        elif extension == ".py":
            # Implement a parser for python files if necessary
            pass
        else:
            raise ValueError("Unsupported file type")
