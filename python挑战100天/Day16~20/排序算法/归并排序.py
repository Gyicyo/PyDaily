
data = [3, 6, 2, 1, 7, 5, 4]

def merge(items1 , items2 ,comp):
    items = []
    index1,index2 = 0,0
    while index1 < len(items1) and index2 < len(items2):
        if (comp(items1[index1],items2[index2])):
            items.append(items1[index1])
            index1 += 1
        else:
            items.append(items2[index2])
            index2 += 1
    items += items1[index1:]
    items += items2[index2:]
    return items

def merge_sort(items,comp):
    if len(items) < 2:
        return items

    mid = len(items) // 2
    left = merge_sort(items[:mid],comp)
    right = merge_sort(items[mid:],comp)
    return merge(left,right,comp)
