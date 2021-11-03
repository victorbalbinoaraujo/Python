def is_palindrome(s):
    return 'É um palíndromo.' if s.lower() == s[::-1].lower() else 'Não é um palíndromo.'

words = ['Afeganistão', 'Arara', 'Jabuticaba', 'Reviver']

for w in words:
    print(is_palindrome(w))