def mostfrequent(n):
    return max(set(n), key=n.count)

print(mostfrequent([1,2,2,3,2,4,5,3,4,4]))
