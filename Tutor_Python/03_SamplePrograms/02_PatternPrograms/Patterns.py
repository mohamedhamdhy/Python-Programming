# Pattern 1: Print numbers in increasing order
rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print("")

# Pattern 2: Print characters in alphabetical order
rows = 70
for i in range(65, rows):
    for j in range(65, i + 1):
        print(chr(j), end=" ")
    print("")

# Pattern 3: Print asterisks in increasing order
for i in range(5):
    for j in range(i + 1):
        print("*", end=" ")
    print("")

# Pattern 4: Print a number triangle
rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(i, end=" ")
    print("")

# Pattern 5: Print characters in alphabetical order (another version)
rows = 70
for i in range(65, rows):
    for j in range(65, i + 1):
        print(chr(i), end=" ")
    print("")

# Pattern 6: Print pyramid of stars
n = 5
k = 8
for i in range(0, n):
    for j in range(0, k):
        print(end=" ")
    k -= 2
    for j in range(0, i + 1):
        print("* ", end="")
    print()

# Pattern 7: Print pyramid of numbers
n = 5
k = 2 * n - 2
for i in range(0, n):
    for j in range(0, k):
        print(end=" ")
    k -= 1
    x = 1    
    for j in range(0, i + 1):
        print(x, end=" ")
        x += 1
    print()

# Pattern 8: Print a number triangle in reverse
r = 5
for i in range(r, 0, -1):
    for j in range(1, i):
        print(end=" ")
    for k in range(i, r + 1):
        print(k, end=" ")
    print(" ")

# Pattern 9: Print alphabet pyramid
n = 5
k = 2 * n - 2
for i in range(0, n):
    for j in range(0, k):
        print(end=" ")
    k -= 1
    x = 65
    for j in range(0, i + 1):
        ch = chr(x)
        print(ch, end=" ")
        x += 1
    print("\r")
k = n - 2

# Pattern 10: Print inverted alphabet pyramid
alp = 65
r = 5
for i in range(r, 0, -1):
    for j in range(1, i):
        print(end=" ")
    for k in range(i, 6):
        print(chr(alp + k - 1), end=" ")
    print(" ")

# Pattern 11: Print star pattern with increasing zeros
r = 5
for i in range(1, r + 1):
    for j in range(1, r - i + 1):
        print(" ", end="")
    for j in range(0, i):
        if j == 0 or i == 0:
            c = 1
        else:
            c = c * (i - j) // j
        print(c, end=" ")
    print()

# Pattern 12: Print Pascal's triangle with characters
alp = 65
r = 5
for i in range(1, r + 1):
    for j in range(r, i, -1):
        print(end=" ")
    t = int(1)
    for k in range(1, i + 1):
        print(chr(alp - 1 + t), end=" ")
        t = int(t * (i - k) // k)
    print(" ")

# Pattern 13: Print increasing numbers
rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print("")
for i in range(rows, 0, -1):
    for j in range(1, i):
        print("*", end=" ")    
    print("")

# Pattern 14: Print both increasing and decreasing numbers
rows = 69
for i in range(65, rows + 1):
    for j in range(65, i + 1):
        print(chr(j), end=" ")
    print("")
for i in range(rows, 65, -1):
    for j in range(65, i):
        print(chr(j), end=" ")    
    print("")

# Pattern 15: Print diamond pattern of stars
rows = 5
for i in range(1, rows + 1):
    for j in range(1, rows - i + 1):
        print(" ", end="")
    for j in range(0, i):
        print("*", end=" ")
    print("")
for i in range(rows - 1, 0, -1):
    for j in range(1, rows - i + 1):
        print(" ", end="")
    for j in range(0, i):
        print("*", end=" ")
    print("")

# Pattern 16: Print inverted triangle of numbers
n = 5
k = 2 * n - 2
for i in range(0, n - 1):
    for j in range(0, k):
        print(end=" ")
    k -= 2
    for j in range(0, i + 1):
        print("* ", end="")
    print(" ")
k = -1
for i in range(n - 1, -1, -1):
    for j in range(k, -1, -1):
        print(end=" ")
    k += 2
    for j in range(0, i + 1):
        print("* ", end="")
    print(" ")

# Pattern 17: Print increasing triangle of numbers
rows = 5
for i in range(rows, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")    
    print("")
for i in range(2, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print("")

# Pattern 18: Print decreasing triangle of numbers
rows = 6
for i in range(0, rows):
    for j in range(rows - 1, i, -1):
        print(j, end=" ")    
    print('')

# Pattern 19: Print reverse pattern of numbers
rows = 5
for i in range(rows, 0, -1):
    for j in range(rows, i - 1, -1):
        print(j, end=" ")
    print()

# Pattern 20: Print increasing triangle of numbers
cn = 1  
s = 2  
rows = 5  
for i in range(rows):  
    for j in range(1, s):  
        print(cn, end=' ')  
        cn += 1  
    print("")  
    s += 1  

# Pattern 21: Print inverted triangle of letters
rows = 70
for i in range(rows, 65, -1):
    for j in range(65, i):
        print(chr(j), end=" ")    
    print("")

# Pattern 22: Print inverted triangle of letters (another version)
rows = 70
for i in range(64, rows):
    for j in range(rows - 1, i, -1):
        print(chr(j), end=" ")    
    print('')

# Pattern 23: Print inverted triangle of letters (yet another version)
rows = 69
for i in range(rows, 64, -1):
    for j in range(rows, i - 1, -1):
        print(chr(j), end=" ")
    print()

# Pattern 24: Print a triangle of letters
n = 7
alpha = 65
for i in range(1, n):
    for j in range(1, i):
        print(chr(alpha), end=" ")
        alpha += 1
    print()

# Pattern 25: Print Pascal's triangle with numbers
rows = 5
c = 1
for i in range(1, rows + 1):
    for space in range(1, rows - i + 1):
        print(" ", end="")
    for j in range(0, i):
        if j == 0 or i == 0:
            c = 1
        else:
            c = c * (i - j) // j
        print(c, end=" ")
    print()

# Pattern 26: Print Pascal's triangle with characters
alp = 65
r = 5
for i in range(1, r + 1):
    for j in range(r - 1, i - 1, -1):
        print(end="  ")
    for k in range(i + 1):
        print(chr(alp + k), end=" ")
    for l in range(i - 1, -1, -1):
        print(chr(alp + l), end=" ")
    print()

# Pattern 27: Print numbers in a pattern
r = 5
for i in range(1, r + 1):
    for j in range(1, r - i + 2):
        print(j, end=" ")
    print()

# Pattern 28: Print star pattern with alternating characters
r = 5
for i in range(1, r + 1):
    for j in range(1, r - i + 1):
        print(" ", end="")
    for j in range(1, 2 * i):
        if j % 2 != 0:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Pattern 29: Print star pattern in alternating rows
rows = 5
for i in range(rows):
    if i % 2 == 0:
        print("* " * (i + 1))
    else:
        print(" " * (i + 1))

# Pattern 30: Print triangle of increasing stars
for i in range(5):
    print(" " * (5 - i - 1) + "*" * (i * 2 + 1))

# Pattern 31: Print alternating stars and spaces
rows = 5
for i in range(rows):
    for j in range(rows):
        if (i + j) % 2 == 0:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Pattern 32: Print reverse right-angled triangle of numbers
n = 5
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Pattern 33: Print a pyramid of numbers
n = 5
for i in range(n):
    print(' ' * (n - i - 1) + ' '.join(str(x) for x in range(1, i + 2)))

# Pattern 34: Print a diamond pattern
n = 5
for i in range(1, n + 1):
    print(' ' * (n - i) + '* ' * i)
for i in range(n - 1, 0, -1):
    print(' ' * (n - i) + '* ' * i)

# Pattern 35: Print numbers in an inverted pyramid
rows = 5
for i in range(rows, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Pattern 36: Print a hollow square pattern
n = 5
for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Pattern 37: Print right-angled triangle of stars
n = 5
for i in range(n):
    print('* ' * (i + 1))

# Pattern 38: Print an hourglass pattern of stars
rows = 5
for i in range(rows, 0, -1):
    print('* ' * i)
for i in range(2, rows + 1):
    print('* ' * i)

# Pattern 39: Print a zig-zag pattern
rows = 5
for i in range(rows):
    if i % 2 == 0:
        print('* ' * (rows - i))
    else:
        print(' ' * (2 * i - 1) + '*')

# Pattern 40: Print a diamond shape with numbers
n = 5
for i in range(1, n + 1):
    print(' ' * (n - i) + ' '.join(str(x) for x in range(1, i + 1)))
for i in range(n - 1, 0, -1):
    print(' ' * (n - i) + ' '.join(str(x) for x in range(1, i + 1)))
