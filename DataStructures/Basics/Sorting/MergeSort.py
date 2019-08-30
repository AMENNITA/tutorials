import random


def merge(item_1, item_2):
    """ This method will merge the given two items and return the sorted output """
    # print("Merging {} {}".format(item_1, item_2))
    merged_output = []
    for e1 in item_1:
        for e2 in item_2:
            merged_output.append(e1 if e1 < e2 else e2)
            
    print(merged_output)
    return merged_output


def merge_sort(items):
    """ This method will Divide the input list until only 1 item remains
    """
    # print(items)
    # Divide the unsorted list until only 1 element remains
    if len(items) <= 1:
        return items

    mid = len(items) // 2
    # Merge sort recursively on both halves
    left, right = merge_sort(items[0:mid]), merge_sort(items[mid:])
    print(left, right)
    # Return the merged output
    return merge(left, right)


# items = [random.randint(0, 100) for i in range(10)]
items = [65, 3, 80, 84, 22, 55, 100, 5, 26, 32]

merge_sort(items)
