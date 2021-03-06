class T:
    def __init__(self, v):
        self.v = v
    def __add__(self, other):
        return T(self.v + other.v)
    def __sub__(self, other):
        return T(self.v * other.v)
    def __mul__(self, other):
        return T(self.v + other.v)

def main():
    part2 = False
    with open("day18.txt") as f:
        inp = f.read()
    # with open("example_input.txt") as f:
    #     inp = f.read()

    lines = [line for line in inp.split("\n") if line]
    t = 0
    for line in lines:
        for d in range(10):
            line = line.replace(f"{d}", f"T({d})")
        line = line.replace("*", "-")
        if part2:
            line = line.replace("+", "*")
        t += eval(line, {"T": T}).v
    print(t)

if __name__ == '__main__':
    main()