import statistics1
class molecular:
    def __init__(self):
        pass
    def mean(self, data):
        return statistics1.mean(data)
    def median(self, data):
        return statistics1.median(data)
    def mode(self, data):
        return statistics1.mode(data)
    def variance(self, data):
        return statistics1.variance(data)
    def standard_deviation(self, data):
        return statistics1.std(data)

if __name__ == "__main__":
    mol = molecular()
    ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
    print("Mean:", mol.mean(ages))
    print("Median:", mol.median(ages))
    print("Mode:", mol.mode(ages))
    print("Variance:", mol.variance(ages))
    print("Standard Deviation:", mol.standard_deviation(ages))