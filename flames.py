def flames(name1, name2):
    name1 = name1.lower().replace(" ", "")
    name2 = name2.lower().replace(" ", "")

    # Remove common letters
    for ch in name1[:]:
        if ch in name2:
            name1 = name1.replace(ch, '', 1)
            name2 = name2.replace(ch, '', 1)

    count = len(name1 + name2)

    flames_list = ['F', 'L', 'A', 'M', 'E', 'S']
    while len(flames_list) > 1:
        index = (count % len(flames_list)) - 1
        if index >= 0:
            flames_list = flames_list[index+1:] + flames_list[:index]
        else:
            flames_list.pop()

    result = {
        'F': 'Friends',
        'L': 'Love',
        'A': 'Affection',
        'M': 'Marriage',
        'E': 'Enemies',
        'S': 'Siblings'
    }

    return result[flames_list[0]]

# Example usage
name1 = input()
name2 = input()
print("Relationship is:", flames(name1, name2))