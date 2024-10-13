import sys
import json

class WeaponAnalyzer:
    def __init__(self, path: str):
        self.dataPath = path
        print(self.dataPath, 'test')

    #def calculateTTK() --> float:

    #def analyze(str: dataPath)--> None:

if __name__ == "__main__":
    args = sys.argv
    if len(args)<2:
        print("No data path given.")
    else:
        analyzer = WeaponAnalyzer(args[1])