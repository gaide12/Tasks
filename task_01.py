def is_palindrome(string):
    string=str(string).lower()
    punct="!.,?();' -"
    for p in punct:
        if p in string:
            string=string.replace(p,"")
    return string==string[::-1]
print(is_palindrome('A man, a plan, a canal -- Panama,'))
print(is_palindrome("Madam, I'm Adam!"))
print(is_palindrome(333,))
print(is_palindrome(None,))
print(is_palindrome("Abracadabra",))


