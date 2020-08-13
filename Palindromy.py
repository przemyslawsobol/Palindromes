def if_palindrome(s):
    i = 0
    j = len(s) - 1

    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

slowo = input("Wprowadź słowo: ")
print(slowo)
print(if_palindrome(slowo))

