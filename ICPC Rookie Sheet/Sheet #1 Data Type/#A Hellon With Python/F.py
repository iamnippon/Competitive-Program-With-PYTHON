#Question F
#Link: https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/F

#Solution:
a, b = map(int, input().split())
number1 = str(a)[-1]  # Get the last digit of a
number2 = str(b)[-1]
sum_of_last_digits = int(number1) + int(number2)  # Sum the last digits
print(sum_of_last_digits) # Print the result