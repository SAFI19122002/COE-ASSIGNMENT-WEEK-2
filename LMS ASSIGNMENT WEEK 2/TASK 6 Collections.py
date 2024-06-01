from collections import Counter
def calculate_earnings(shoe_sizes, customer_requests):
    inventory = Counter(shoe_sizes)
    total_earnings = 0
    for size, price in customer_requests:
        if inventory[size] > 0:
            total_earnings += price
            inventory[size] -= 1          
    return total_earnings
if __name__ == "__main__":
    X = int(input())
    shoe_sizes = list(map(int, input().split()))
    N = int(input())
    customer_requests = []
    for _ in range(N):
        size, price = map(int, input().split())
        customer_requests.append((size, price))
    earnings = calculate_earnings(shoe_sizes, customer_requests)
    print(earnings)
