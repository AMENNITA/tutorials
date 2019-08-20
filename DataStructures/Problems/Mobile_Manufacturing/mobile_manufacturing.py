from random import randint


def generate_input_file(filename, N):
    """ This method will generate the file having mobile details """
    with open(filename, "w") as fp:
        for i in range(N):
            fp.writelines("{} / {} / {}\n".format(i + 1, randint(1, 10), randint(1, 30)))


def read_input(filename):
    """ This method will read the given file and will return the Information in a List of Tuples """
    info = []
    with open(filename, "r") as fp:
        for i, line in enumerate(fp.readlines()):
            value = list(map(lambda x: int(x.strip()), line.split("/")))
            # print(value)
            info.append(tuple(value))
    # Return the values
    return info


input_file = "inputPS1.txt"

# Generate the Input file having 10 Mobile details
# generate_input_file(input_file, 10)


timings = read_input(input_file)

# print(timings)

for i in timings:
    print("Mobile # {} : Manufacturing : {} Assembly {}".format(i[0], i[1], i[2]))
