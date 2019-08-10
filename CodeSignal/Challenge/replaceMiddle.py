def replaceMiddle(arr):
    if len(arr)%2 != 0:
        return arr
    else:
        arr.insert(int(len(arr)/2),
                   (int(arr[int(len(arr)/2) - 1] + arr[int(len(arr)/2)])))
        print(arr)
        arr.remove(arr[int(len(arr)/2)+1])
        print(arr)
        arr.remove(arr[int(len(arr)/2)-1])
        return arr

arr = [1, 2, 3, 5, 6, 8, 9, 5]
result = [45, 23, 12, 45, 453, -234, -45]
print(arr)
print(replaceMiddle(arr))
print(result)
