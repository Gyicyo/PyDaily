def quick_sort(items,reverse=False):
    comp = lambda x,y: x>y if reverse else x<y
    items = list(items)[:]
    if len(items)<=1:
        return items
    _quick_sort(items,0,len(items)-1,comp)
    return items

def _quick_sort(items,left,right,comp):
    if left < right:
        pivot = partition(items,left,right,comp)
        _quick_sort(items,left,pivot-1,comp)
        _quick_sort(items,pivot+1,right,comp)

def partition(items,left,right,comp):
    pivot = items[right]
    while (left < right):
        while (left < right and (comp(items[left],pivot))):
            left += 1

        while (left < right and (comp(pivot,items[right]))):
            right -= 1
        swap(items,left,right)
    return left


def swap(items,i,j):
    items[i],items[j] = items[j],items[i]

a = [3,5,9,1,6,8,12,4]
print(quick_sort(a))