class Pizza:
    def __init__(self, rows, columns, min, max, mypizza):
        self.rows = rows
        self.columns = columns
        self.min = min
        self.max = max
        self.mypizza = mypizza

def read(path):
    mypizza = []
    with open(path) as file:
        data = file.readlines()
    rules = data[0].split()
    for row in data[1:]:
        mypizza.append(list(row)[:-1])
    return Pizza(rules[0], rules[1], rules[2], rules[3], mypizza)

if __name__ == '__main__':
    mypizza = read('/mnt/c/Users/nishant/Desktop/google-hash-code/dataset/a_example.in')
    print(mypizza.mypizza)
