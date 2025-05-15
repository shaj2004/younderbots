def removeduplicates(inputlist):
    result = []
    for item in inputlist:
        if item not in result:
            result.append(item)
    return result


mylist = [1, 2, 2, 3, 4, 3, 5]
newlist = removeduplicates(mylist)
print("List after removing duplicates:", newlist)
