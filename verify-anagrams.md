Hi, CiO friends!

Today I'm going to try a little experiment, today you will not see a random CheckiO player's solutions.
Today, we will examine one simple mission: ["Verify Anagrams"][mission].

An anagram is a type of word play, the result of rearranging the letters of a word or phrase to produce a new word or phrase, using all the original letters exactly once. Two words are anagrams to each other if we can get one from another by rearranging the letters.
You are given two words or a phrase. Try to verify are they anagrams or not.

## Count letters

We need to compare two words or phrases. First we will need to "sanitize" them by
choosin only the letters and change them to lowercase. This part's not too important, but we can
convert them into a list during this step. Let's do that in a separate function.

```
def sanitize(text):
    return [ch.lower() for ch in text if ch.isalpha()]
```

Maybe you can economize memory with a generator:

```
def sanitize(text):
    yield from (ch.lower() for ch in text.lower() if ch.isalpha())
```

Or how about a more functional style:

```
sanitize = lambda t: map(str.lower, filter(str.isalpha, text))
```

Next we need to count each letter in the text. If the quantities for the words are same, then
they are anagrams. Let's suppose we use only letters from the latin alphabet, in that case we can use a list for 26 elements.

```
def count_letters(text):
    counter = [0] * 26
    for ch in text:
        counter[ord(ch) - ord("a")] += 1
    return counter
```

Honestly it looks kinda like C-code, not Python. On top oif this. we aren't ready for non latin letters.
Maybe we should use a dictionary:

```
def count_letters(text):
    counter = {}
    for ch in text:
        counter[ch] = counter.get(ch, 0) + 1
    return counter
```

This is better, but how about "python batteries"? [Counter](https://docs.python.org/2/library/collections.html#collections.Counter) can help us.

```
from collections import Counter

def count_letters(text):
    return Counter(text)
```

Hm, I think with Counter we don't need the "count_letters" function anymore:

```
from collections import Counter

def sanitize(text):
    yield from (ch.lower() for ch in text.lower() if ch.isalpha())

def verify_anagrams(first, second):
    return Counter(sanitize(first)) == Counter(sanitize(second))
```

## Sorted

So, when I solved this mission for the first time, I didn't use a counter.
Instead I converted the words in an "initial" or "starting" form.
Of course I could talk all about sorted forms. If we sort strings and compare then it's the same as
counting the elements, and because the text contains only letters and whitespaces we can use this trick
(thanks [@StefanPochmann](http://www.checkio.org/user/StefanPochmann/):

```
def verify_anagrams(first, second):
    return "".join(sorted(first.lower())).strip() == "".join(sorted(second.lower())).strip()
```

As you can see we can transform it in one-liner- just 'causs.

```
verify_anagrams=lambda f,s,p=lambda x: "".join(sorted(x.lower())).strip():p(f)==p(s)
```

That's all for anagrams. If you have a more interesting way to solve this mission, feel free to post it in comments.

_Valentin Bryukhanov aka Bryukh_

[mission]: http://www.checkio.org/mission/verify-anagrams/share/80a6c1510bf892c6b3789caa9e4f3805/
