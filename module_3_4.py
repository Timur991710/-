def single_root_words(root_word, *other_words ):
    same_words = []
    other = list(other_words)
    for i in range(len(other)):
        if root_word.lower() in other[i].lower() or other[i].lower() in root_word.lower():
            same_words.append(other[i]) 
    return (same_words)


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)