import linkedList


list1 = linkedList.LinkedList([1, 2, 98, 4, 5, 67, 8, 23, 69, 900])
print("Printing initial LinkedList:")
print(list1.print_list())
print("--------------------")

print("Using the size method, what is the total number of nodes?")
print(list1.size)
print("--------------------")

print("Using the head method, what is the current head?")
print(list1.head.value)
print("--------------------")

print("Using the tail method, what is the current tail?")
print(list1.tail.value)
print("--------------------")

print("Does the list contain 23? (Using Contain method)")
print(list1.contains(23))
print("--------------------")

(list1.append(76))
print("Append 76 to the list:")
print(list1.print_list())
print("--------------------")

(list1.prepend(2134))
print("Prepend 2134 to the list:")
print(list1.print_list())
print("--------------------")

(list1.pop())
print("Remove 76 from the LinkedList:")
print(list1.print_list())
print("--------------------")

print("Find the index of 8: (Using Index Method)")
print("In node number", list1.find(8))
print("--------------------")

print("What node is at index 6? (Using index method)")
indexNode = list1.index(6)
print(indexNode.value)
print("--------------------")


