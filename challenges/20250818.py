# Daily Coding Problem: Problem #1 [Easy]

# Good morning! Here's your coding interview problem for today.
# This problem was recently asked by Google.

# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# Bonus: Can you do this in one pass?

k = 17

numSets = [
    [10, 15, 3, 7],
    [8, 14, 1, 2],
    [1, 13, 16, 4]
]

# Attempt 1
# Not necessarily efficient since it's O(n^2)
def sumCheck(numSet, k):
    res = False

    for i in range(len(numSet)):
        for j in range(len(numSet)):
            if (numSet[i] + numSet[j] == k):
                res = True
    return res

# Main
def main(sets):
    for i in sets:
        res = sumCheck(i, k)
        print(res)

main(numSets)

### Ideal solution

# Below is actually the ideal solution, namely because it's O(n).
# This is also how the Bonus challenge is achieved, since we're only iterating through the numSet once.
# Wasn't familiar with the set() capability in Python! 
# I should dedicate a week or so purely learning the capabilities of Python I'm unfamiliar with, especially since most of my experience is from OOP.
# 
# Anyway assuming we have a set of [10, 15, 3, 7]
# Then 7 will be the number in the set that returns True.
# Why?
# Since a set() is an unordered unique list, we store our set's numbers that don't have a potential complement that could eventually add to k
# So in this case, 17 - 10 = 7, which would be the necessary compliment to find to add to 17
# When we reach 7, and we run 17 - 7, we get 10, which is a compliment in the list we were looking for that adds to k!

# def idealSumCheck(numSet, k):
#     seen = set()
#     res = False
#     for x in numSet:
#         if (k - x in seen):
#             res = True
#         seen.add(x)
#     return res