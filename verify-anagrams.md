Hi, CiO friends!

Today I let a little experiment for myself and you will not see CheckiO player solutions.
We will examine one simple mission ["Verify Anagrams"][mission].

An anagram is a type of word play, the result of rearranging the letters of a word or phrase to produce a new word or phrase, using all the original letters exactly once. Two words are anagrams to each other if we can get one from another by rearranging the letters.
You are given two words or phrase. Try to verify are they anagrams or not.

## Count letters

So we need to compare two words or phrases. First we need to "sanitize" them --
choose only letters and lowercase them. And it's not too important, but we can
convert it to a list in this step. Let's move it in the separate function.

```
def sanitize(text):
    return [ch.lower() for ch in text if ch.isalpha()]
```

or maybe you economize memory and would a generator:

```
def sanitize(text):
    yield from (ch.lower() for ch in text.lower() if ch.isalpha())
```

or more functional style:

```
sanitize = lambda t: map(str.lower, filter(str.isalpha, text))
```

Next we need to count each letter in the text and if the quantities for the words are same, then
they are anagrams. Let's suppose we use only latin alphabet. Then we can use a list for 26 elements.

```
def count_letters(text):
    counter = [0] * 26
    for ch in text:
        counter[ord(ch) - ord("a")] += 1
    return counter
```

Honestly it looks like C-code, not Python. And we don't ready for non latin letters.
Maybe we will use a dictionary.

```
def count_letters(text):
    counter = {}
    for ch in text:
        counter[ch] = counter.get(ch, 0) + 1
    return counter
```

Better, but how about "python batteries"? And [Counter](https://docs.python.org/2/library/collections.html#collections.Counter) can help us.

```
from collections import Counter

def count_letters(text):
    return Counter(text)
```

Hm, I think with Counter we don't need "count_letters" function and the solution is:

```
from collections import Counter

def sanitize(text):
    yield from (ch.lower() for ch in text.lower() if ch.isalpha())

def verify_anagrams(first, second):
    return Counter(sanitize(first)) == Counter(sanitize(second))
```

## Sorted

When I solved this mission the first time, I didn't use a counter.
Instead I converted words at "initial" or "start" form for permutations,
of course I tell about sorted form. If we sort strings and compare then it's the same as
count elements. And because a text contains only letters and whitespaces we can use a trick
(thanks [@StefanPochmann](http://www.checkio.org/user/StefanPochmann/) for the idea:

```
def verify_anagrams(first, second):
    return "".join(sorted(first.lower())).strip() == "".join(sorted(second.lower())).strip()
```

As you can see we can transform it in one-liner (just cause we can)

```
verify_anagrams=lambda f,s,p=lambda x: "".join(sorted(x.lower())).strip():p(f)==p(s)
```

That's all anagrams. If you have more interesting ways to solve this mission feel free to write it in comments.

_Valentin Bryukhanov aka Bryukh_

[mission]: http://www.checkio.org/mission/verify-anagrams/share/80a6c1510bf892c6b3789caa9e4f3805/
