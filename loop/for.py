
# The for loop in Python is used to iterate over a sequence (such as a list, tuple, dictionary, set, or string) and execute a block of code for each item in the sequence.
a=[1, 2,3,4]
for i in a:
    print(i)

# The range() function generates a sequence of numbers, which is often used with for loops.
for i in range(65,70):
    print(chr(i))
    if i==68:
        break
        # it stops the loop 
for i in range(10):
    if i%2==0:
        continue
    # continue skips the code for current iteration
    print(i)
# neated loop
for i in range(10):
    if i%2==0:
        continue
    for j in range(10):
        if j%2!=0:
            continue
        print(f"{i} {j}")