def is_palindrome(string):
    string=str(string).lower()
    punct="!.,?();' -"
    for p in punct:
        if p in string:
            string=string.replace(p,"")
    print(string==string[::-1])
is_palindrome("A man, a plan, a canal -- Panama") # => True
is_palindrome("Madam, I'm Adam!") # => True
is_palindrome(333) # => True
is_palindrome(None) # => False
is_palindrome("Abracadabra") # => False )


