# # # # # n=5
# # # # # factorial=1
# # # # # for i in range(1,n+1):
# # # # #     factorial=factorial*i
# # # # #     print(factorial)
# # # # # print(f"The factorial of {n} is {factorial}")
# # # # #
# # # # # n=10
# # # # # for i in range (1, n+1):
# # # # #     for j in range(i):
# # # # #         print("*", end="")
# # # # #     print()
# # # #
# # # # n=5
# # # # for i in range(1,n+1):
# # # #     for j in range(1, i+1):
# # # #         print(j*i, end=",")
# # # #     print()
# # # #
# # # # for i in range(1,n+1):
# # # #     for j in range(1, i+1):
# # # #         print(".", end="")
# # # #     print()
# # # #
# # # #-------------
# # # # Palindrome number check
# # # num= 1216
# # # original = num
# # # reverse_sum  = 0
# # # while num >0:
# # #     digit = num % 10
# # #     reverse_sum = reverse_sum * 10 + digit
# # #     num = num // 10
# # # if original == reverse_sum:
# # #     print(f"{original} is a palindrome")
# # # else:
# # #     print(f"{original} is not a palindrome")
# # # #-------------
# # # # Fibonacci series
# # # n=10
# # # a,b=0,1
# # # for i in range(n):
# # #     print(a, end=",")
# # #     a,b=b,a+b
# # # #-------------
# # # # Prime number check
# # # num=29
# # # is_prime=True
# # #
# # # #----------------
# # # # Armstrong number check
# # # num=153
# # # original=num
# # # sum=0
# # # n=len(str(num))
# # # while num>0:
# # #     digit=num%10
# # #     sum=sum+digit**n
# # #     num=num//1010
# # # if original==sum:
# # #     print(f"{original} is an armstrong number")
# # # else:
# # #     print(f"{original} is not an armstrong number")
# # # #----------------
# # # #leetcode easy problems
# # # #1.
# # # """Write a program that prints numbers from 1 to n.
# # #
# # # For multiples of 3, print "Fizz" instead of the number.
# # #
# # # For multiples of 5, print "Buzz".
# # #
# # # For multiples of both, print "FizzBuzz"."""
# # #
# # # n=15
# # # for i in range(1,n+1):
# # #     if i%3==0 and i%5==0:
# # #         print("FizzBuzz", end=",")
# # #     elif i%3==0:
# # #         print("Fizz", end=",")
# # #     elif i%5==0:
# # #         print("Buzz", end=",")
# # #     else:
# # #         print(i, end=",")
# #
# # #2.
# # """Reverse Integer:
# # Given an integer n, return it reversed.
# #
# # Example: 123 → 321, -456 → -654.
# #
# # Use a while loop (don’t convert to string)."""
# # n=123456789
# # reversed_sum=0
# #
# #
# #
# # while n>0 :
# #     it = 0
# #     last_digit= n%10
# #     reversed_sum= reversed_sum*10 + last_digit
# #     n= n//10
# # print(reversed_sum)
# #
# """Problem 2
# Print a Diamond Shape using *.
# For n=3:
#
#   *
#  * * *
# * * * * *
#  * * *
#   *"""
# # n=2
# # for i in range(n):
# #     print(" "*(n-i-1)+"* "*(i+1))
# # for i in range(n-1):
# #     print(" "*(i+1)+"* "*(n-i-1))
#
# n = 1674792
# count = 0
# temp = n
# while temp > 0:
#     digit = temp % 10
#     if digit != 0 and n % digit == 0:
#         count += 1
#     temp = temp // 10
# print(count)

