if __name__ == '__main__':
    s = input("Enter a string: ")
    t = [cha for cha in s]  # Corrected variable name
    l = any(char.isalnum() for char in t)
    print(l)  # To print the result of the any() check
