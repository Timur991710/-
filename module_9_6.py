def all_variants(text):
    for i in text:
        yield i
    coint = 1
    for i in text:
        if coint <= len(text) - 1:
            x = i + text[coint]
            coint += 1
            yield x
    yield text


a = all_variants("abc")
for i in a:
    print(i)