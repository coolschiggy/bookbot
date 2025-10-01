def word_count(text):
    return len(text.split())

def character_count(text):
    map = {}
    for char in text:
        low = char.lower()
        map[low] = 1 if low not in map else map[low] +1
    return map

def dict_to_list(dict):
    list = []
    for key, value in dict.items():
        list.append({"char": key, "num": value})
    
    def sortby(dict):
        return dict['num']
    list.sort(reverse=True, key=sortby)
    return list
