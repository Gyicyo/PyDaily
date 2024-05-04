
data = [3, 6, 2, 1, 7, 5, 4]

def jiweijiu_sort(data,reverse=False):
    comp = lambda x,y: x < y if reverse else x > y

    for i in range(int(len(data)/2)):
        swapped = False
        for j in range(i,len(data) - 1 - i):
            if (comp(data[j],data[j+1])):
                data[j],data[j+1] = data[j+1],data[j]
                swapped = True

        if swapped:
            swapped = False
        else:
            break

        for j in range(len(data) - 2 - i, i, -1):
            if (comp(data[j-1],data[j])):
                data[j],data[j-1] = data[j-1],data[j]
                swapped = True
        if not swapped:
            break
    return data

print(jiweijiu_sort(data,reverse=True))
