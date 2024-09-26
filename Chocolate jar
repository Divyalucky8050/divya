def chocolates_for_A(N, jars):
    total_chocolates = 0
    for jar in jars:
        total_chocolates += jar // 3  # A gets every 3rd chocolate
        if jar % 3 == 1:  # If remaining chocolates are 1, A gets it
            total_chocolates += 1
    return total_chocolates

# Input Format
N = int(input())  # Number of jars
jars = list(map(int, input().split()))  # Quantity of chocolates in each jar

