import re

def is_valid_regex(pattern):
    try:
        re.compile(pattern)
        return True
    except re.error:
        return False

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split("\n")
    
    T = int(data[0])
    test_cases = data[1:T+1]
    
    results = [is_valid_regex(pattern) for pattern in test_cases]
    
    for result in results:
        print(result)
