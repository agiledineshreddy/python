def print_formatted(number):
    # your code goes here
    width=len(bin(number))-2
    n = []
    for i in range(1, number+1):
        deci=str(i)
        octa=oct(i)[:2]
        hexa=hex(i)[:2]
        bina=bin(i)[:2]
        formatted_line = f"{deci.rjust(width)} {octa.rjust(width)} {hexa.rjust(width)} {bina.rjust(width)}"
        n.append(formatted_line)
    
    return n

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)