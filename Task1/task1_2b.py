def triangle(n):
    arr= ["F","M","D"]
    k = n - 1
    for i in range(0, n):

        for j in range(0, k):
            print(end=" ")
        k = k - 1
        for j in range(0, i+1):
            print(arr[j], end=" ")
        print("\r")
n = 3
triangle(n)
