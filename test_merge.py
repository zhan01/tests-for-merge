def merge(left, right, lst):
    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            lst[k] = left[i]
            i = i + 1
        else:
            lst[k] = right[j]
            j = j + 1

        k = k + 1

    while i < len(left):
        lst[k] = left[i]
        i = i + 1
        k = k + 1

    while j < len(right):
        lst[k] = right[j]
        j = j + 1
        k = k + 1

    
def merge_sort(lst):
    if len(lst) < 2:
        return lst

    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]

    merge_sort(left)
    merge_sort(right)

    merge(left, right, lst)

lst = [10, 8, 9, 15, 22, 7, 6, 5, 2, 26]
left = [8, 9, 10, 15, 22]
right = [2, 5, 6, 7, 26]
merge(left, right, lst)
print("test 1" , lst)
assert lst == [2, 5, 6, 7, 8, 9, 10, 15, 22, 26]

lst = [10, 8, 9, 15, 7, 6, 5, 2]
left = [8, 9, 10, 15]
right = [2, 5, 6, 7]
merge(left, right, lst)
print("test 2" ,lst)
assert lst == [2, 5, 6, 7, 8, 9, 10, 15]

lst = [10, 8, 15, 7, 6, 5]
left = [8, 10, 15]
right = [5, 6, 7]
merge(left, right, lst)
print("test 3" ,lst)
assert lst == [5, 6, 7, 8, 10, 15]

lst = [10, 8, 15, 7, 6]
left = [8, 10, 15]
right = [6, 7]
merge(left, right, lst)
print("test 4" ,lst)
assert lst == [6, 7, 8, 10, 15]

lst = [10, 8, 15]
left = [8, 10]
right = [15]
merge(left, right, lst)
print("test 5" ,lst)
assert lst == [8, 10, 15]