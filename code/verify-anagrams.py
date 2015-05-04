def count_letters1(text):
    counter = [0] * 26
    for ch in text:
        counter[ord(ch) - ord("a")] += 1
    return counter

def count_letters2(text):
    counter = {}
    for ch in text:
        counter[ch] = counter.get(ch, 0) + 1
    return counter

from collections import Counter

def count_letters3(text):
    return Counter(text)

print(count_letters3("sdasefsfasfd"))
print(count_letters3("sdasefsfasfd") == count_letters3("fasfdsdasefs"))


verify_anagrams=lambda f,s,p=lambda x: "".join(sorted(x.lower())).strip():p(f)==p(s)

assert isinstance(verify_anagrams("a", 'z'), bool), "Boolean!"
assert verify_anagrams("Programming", "Gram Ring Mop") == True, "Gram of code"
assert verify_anagrams("Hello", "Ole Oh") == False, "Hello! Ole Oh!"
assert verify_anagrams("Kyoto", "Tokyo") == True, "The global warming crisis of 3002"
