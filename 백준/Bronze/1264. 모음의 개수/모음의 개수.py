vowel=['a','e','i','o','u']

while True:
    n=input()
    if n == '#':
        break
        
    vowel_count=0
    n = n.lower()
    for char in n:
        if char in vowel:
            vowel_count += 1
            
    print(vowel_count)