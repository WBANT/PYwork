def palindrome(n):
    n = n.lower()
    if n == n[::-1]:
        print("It is a palindrome")
    else:
        print("It is not a palindrome")
#test
palindrome("rotor")
