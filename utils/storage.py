import json
import os

class Storage:
    def save(self, filename, data):
        """Save data to a JSON file."""
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
        print(f"Data saved to {filename}.")

    def load(self, filename):
        """Load data from a JSON file."""
        try:
            with open(filename, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"No data found in {filename}.")
            return None