a, b, c = map(int, input().split())
arr = [a, b, c]
print(sum(arr))
print(int(sum(arr)/len(arr)))
print(sum(arr) - int(sum(arr)/len(arr)))