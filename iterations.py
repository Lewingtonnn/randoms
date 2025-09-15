# n=5
# factorial=1
# for i in range(1,n+1):
#     factorial=factorial*i
#     print(factorial)
# print(f"The factorial of {n} is {factorial}")
#
# n=10
# for i in range (1, n+1):
#     for j in range(i):
#         print("*", end="")
#     print()

n=100
for i in range(1,n+1):
    for j in range(1, i+1):
        print(j*i, end=",")
    print()

