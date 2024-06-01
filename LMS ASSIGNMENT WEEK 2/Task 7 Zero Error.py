def perform_integer_division(test_cases):
    results = []
    for case in test_cases:
        try:
            a, b = map(int, case.split())
            result = a // b
            results.append(result)
        except ZeroDivisionError as e:
            results.append("Error Code: " + str(e))
        except ValueError as e:
            results.append("Error Code: " + str(e))
    
    return results

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split("\n")
    
    T = int(data[0])
    test_cases = data[1:T+1]
    
    results = perform_integer_division(test_cases)
    for result in results:
        print(result)
