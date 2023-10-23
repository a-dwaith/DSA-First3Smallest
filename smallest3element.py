def first3largest(arr,n):
    first = second = third = max(arr)
    if n < 3:
        print("Invalid")
        return -1
    for i in arr:
        if i < first:
            third = second
            second = first
            first = i
        elif i<second and i != first:
            third = second
            second = i
        elif i<third and i!= second and i != first:
            third =i
    print(f"First = {first}\nSecond = {second}\nThird = {third}")
arr = [10,20,30,40,50]
n = len(arr)
first3largest(arr,n)
