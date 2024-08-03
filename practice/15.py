def merge_the_tools(string, k):
    # Iterate over the string in chunks of size k
    for i in range(0, len(string), k):
        # Get the substring of length k
        substring = string[i:i + k]
        seen = set()
        result = []
        # Iterate over each character in the substring
        for ch in substring:
            if ch not in seen:
                seen.add(ch)
                result.append(ch)
        # Print the result as a string
        print(''.join(result))
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)