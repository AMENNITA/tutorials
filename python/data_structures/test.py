from LinkedList import DoubleLinkedList

# Main program starts here
# single_list = LinkedList()
# single_list.insert(1)
# single_list.insert(2)
# single_list.insert(20)
# single_list.insert(24)
# single_list.insert(34)
#
# print(single_list)
# print(single_list.get(2))
#
# single_list.remove("1")
# print("Size of List {}".format(single_list.get_size()))
# single_list.insert(50)
# print("Size of List {}".format(single_list.get_size()))
# print(single_list)

doubleList = DoubleLinkedList()
doubleList.insert(10)
doubleList.insert(11)
doubleList.insert(12)
doubleList.insert(14)
doubleList.insert(16)

print(doubleList)
doubleList.remove(5)
print(doubleList)
doubleList.remove(1)
print(doubleList)
