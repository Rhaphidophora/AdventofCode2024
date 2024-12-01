def distance():
    l = len(list1)
    for i in range(l-1):
        for j in range(l-i-1):
                if list1[j] > list1[j+1]:
                    list1[j], list1[j+1] = list1[j+1], list1[j]
 
    for i in range(l-2):
        for j in range(l-i-1):
            if list2[j] > list2[j+1]:
                list2[j], list2[j+1] = list2[j+1], list2[j]

    distance = 0
    for i in range(l):
        distance += abs(list1[i] - list2[i])

    return distance


def similarity():
    similarity_score = 0
    for element in list1:
        similarity_score += list2.count(element)*element

    return similarity_score


#testing correctness of code            
list1 = [3,4,2,1,3,3]
list2 = [4,3,5,3,9,3]

assert distance() == 11
assert similarity() == 31


list1 = []
list2= []

#part 1 & 2
with open("1.txt") as file:
    for line in file:
        list1.append(int(line.split()[0]))
        list2.append(int(line.split()[1]))

    print(distance())
    print(similarity())


