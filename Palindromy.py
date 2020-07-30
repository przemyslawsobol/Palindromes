def if_palindrome(s):
    return s == s[::-1]

slowo = input("Wprowadź słowo: ")
print(slowo)
print(if_palindrome(slowo))

