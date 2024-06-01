def merge_the_tools(string, k):
    length= len(string)

    def help(items):
        seen = set()
        for i in items:
            if i not in seen:
                yield i
                seen.add(i)

    while string:
        word = string[0:k]
        string = string[k:]
        
        print (''.join(help(word)))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)