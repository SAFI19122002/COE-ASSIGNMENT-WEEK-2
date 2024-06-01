def average(arr):
    distinct_heights = set(arr)
    average_height = sum(distinct_heights) / len(distinct_heights)
    return round(average_height, 3)

if __name__ == "__main__":
    inpu = int(input().strip())
    data = set(map(int, input().strip().split()))
    result = average(data)
print(result)