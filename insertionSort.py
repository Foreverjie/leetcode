arr = [1, 5, 6, 2, 4, 9, 2]

for i in range(len(arr)):
    if i == 1:
        i = i + 1
        continue
    key = arr[i]
    j = i - 1
    while (j > 0 and arr[j] > key):
        if arr[j] > key:
            arr[j+1] = arr[j]
            j = j - 1
    arr[j+1] = key

print(arr)
