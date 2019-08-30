import numpy as np
import random
from itertools import permutations


def generate_input_file(filename, N):
    """ This method will generate the file having mobile details """
    with open(filename, "w") as fp:
        for i in range(N):
            fp.writelines("{} / {} / {}\n".format(i + 1, random.randint(1, 10), random.randint(1, 10)))


def read_input(filename):
    """ This method will read the given file and will return the Information in a List of Tuples """
    info = []
    with open(filename, "r") as fp:
        for line in fp.readlines():
            if line.strip() is not None:
                value = list(map(lambda x: int(x.strip()), line.split("/")))
                info.append(tuple(value))
    # Return the values
    return info


def display(mobiles_info):
    """ Print the Manufacturing Information"""
    num_mobiles = len(mobiles_info)
    if num_mobiles > 0:
        row_format = "| {:^14}" * 3
        print("-" * 50)
        print(row_format.format("Mobile(i)", "PMi(minutes)", "AMi(minutes)") + " |")
        print("-" * 50)
        for i, mobile in enumerate(mobiles_info):
            print(row_format.format(mobile[0], mobile[1], mobile[2]) + " |")
        print("-" * 50)
        print("")


def merge(items):
    mid = len(items) // 2


def merge_sort(items):
    print("Starting Merge sort")
    if len(items) > 2:
        mid = len(items) // 2
        merge_sort(items[0:mid])
        merge_sort(items[mid:])


def calc_prod_time(mobiles_info):
    production_seq = ", ".join(list(map(lambda x: str(x[0]), mobiles_info)))
    pm_queue = np.cumsum(list(map(lambda x: x[1], mobiles_info)))
    am_queue = np.cumsum([1] + list(map(lambda x: x[2], mobiles_info)))
    # print(np.cumsum(np.ones(10, dtype=int)))
    # print(pm_queue)
    # print(am_queue)
    # First manufacturing will cause assembling time stalled
    idle_time = pm_queue[0]
    for i in range(len(am_queue) - 1):
        if am_queue[i] < pm_queue[i]:
            diff = pm_queue[i] - am_queue[i]
            idle_time += diff
            am_queue[i:] = am_queue[i:] + diff
    return production_seq, am_queue[-1], idle_time
    # print(am_queue)


def all_prod_time():
    """ Check for all the possible Mobile manufacturing sequence
        We can assert it is less when Manufacturing time is in Ascending Order
    """
    for manuf_info in permutations(manuf_input):
        production_seq, total_prod_time, idle_am_tim = calc_prod_time(manuf_info)
        print("Mobiles production sequence : {}".format(production_seq))
        print("Production time for all mobiles is {}".format(total_prod_time))
        print("Idle Time of Assembly unit : {} min".format(idle_am_tim))
        print("")


def greedy_output(manuf_input):
    """ Greedy Algorithm to select the mobiles to minimize total production time
        Sort the Manufacturing input based on Manufacturing time
    """
    # Sort the input based on Manufacturing time
    manuf_input.sort(key=lambda x: x[1])
    production_seq, total_prod_time, idle_am_tim = calc_prod_time(manuf_input)
    print("Mobiles should be produced in the order: {}.".format(production_seq))
    print("Total production time for all mobiles is: {}.".format(total_prod_time))
    print("Idle Time of Assembly unit: {}.".format(idle_am_tim))
    print("")


input_file = "inputPS1.txt"

# Generate the Input file having 10 Mobile details
# generate_input_file(input_file, 12)

manuf_input = read_input(input_file)
display(manuf_input)

# Check all the possible Production time with Manufacturing Input
# all_prod_time()

greedy_output(manuf_input)
