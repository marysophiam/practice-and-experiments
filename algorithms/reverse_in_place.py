def reverse_in_place(str):

    li = []
    li.extend(str)
    size = len(li)

    for i in range(0, size/2):
        li[i], li[size-1-i] = li[size-1-i], li[i]

    reversed = ''.join(li)

    print reversed
    return reversed


# reverse_in_place('Mary Mealiffe')
