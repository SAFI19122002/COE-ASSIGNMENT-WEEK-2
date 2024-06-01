n = int(input().strip()) 
s = set(map(int, input().strip().split()))  
m = int(input().strip())
for _ in range(m):
    command = input().strip().split()
    if command[0] == "pop":
        try:
            s.pop()
        except KeyError:
            pass 
    elif command[0] == "remove":
        try:
            s.remove(int(command[1]))
        except KeyError:
            pass  
    elif command[0] == "discard":
        s.discard(int(command[1]))
print(sum(s))