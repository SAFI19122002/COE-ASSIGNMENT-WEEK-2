def print_rangoli(size):
    alphas= "abcdefghijklmnopqrstuvwxyz"
    total_size = ((4*size)-3)
    for i in range(1, size+1):
        alphas_string = ""
        for j in range(i):
            letter = alphas[size-i+j]
            alphas_string = alphas_string.center((2*j+1), letter)
        alphas_string_hiphen = "-".join(alphas_string)
        print(alphas_string_hiphen.center(total_size, "-"))                 
    for i in range(size-1, 0, -1):        
        alphas_string = ""
        for j in range(i):                
            letter = alphas[size-i+j]
            alphas_string = alphas_string.center((2*j+1), letter)
        alphas_string_hiphen = "-".join(alphas_string)
        print(alphas_string_hiphen.center(total_size, "-"))          
 
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)