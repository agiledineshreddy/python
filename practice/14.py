def minion_game(string):
    # your code goes here
    vowel='aeiouAEIOU'
    a=[]
    b=[]
    for i in string:
        if i in vowel:
            a.append(i)

        elif i not in vowel:
            b.append(i)
    print(a)
    print(b)
    for i in a:
        pass

if __name__ == '__main__':
    s = input()
    minion_game(s)