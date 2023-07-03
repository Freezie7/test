def zero(lists):
    for i in lists:
        if i == 0:
            lists.remove(i)
            lists.append(0)
    return lists
lists = [0, 5, 4, 0, 0, 7]
print(zero(lists))