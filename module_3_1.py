calls = 0
def  count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())

def is_contains(string, list_to):
    count_calls()
    return string.upper() in [i.upper() for i in list_to]

print(string_info('WerRden'))
print(string_info('Kaligulasetlite'))
print(is_contains('Werden', ['Werden', 'den', 'werta']))
print(is_contains('Wden', ['Werden', 'den', 'werta']))
print(is_contains('oRionLite', ['Werden', 'den', 'werta']))
print(calls)