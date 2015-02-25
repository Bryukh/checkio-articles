Hi!

In [the last overview][oneliners_p1] we looked at first ten missions from "Elementary" island.
Today we take the second part of this.

### [Count Inversions][count-inversions]

In this mission you need count the number of inversions in a sequence of numbers.

And we will open our chart with [@veky's][veky_profile] solution ["Gallery"][count-inversion-solution].
Here we see the interesting usage of double loop in comprehension.

```python
count_inversion = lambda s: sum(a > b for i, b in enumerate(s) for a in s[:i])
```

### [The end of other][end-of-other]

In this task, you are given a set of words in lower case. 
Check whether there is a pair of words, such that one word is the end of another (a suffix of another).

And again simple clear one-liner from [@Apua][Apua_profile] ["just one liner"][end-of-other-Apua].

```python
checkio=lambda S:any(a!=b and a.endswith(b) for a in S for b in S)
```

### [Days Between][days-diff]

How to find the difference in days between the given dates.

["oneliner"][days-diff-DiZ] by [@DiZ][DiZ_profile] with "import" variation that is designed specially to write one-liners ;-)

```python
days_diff=lambda f,t,d=__import__('datetime').date:abs(d(*f)-d(*t)).days
```

### [Pangram][pangram]

Check if a sentence is a pangram or not.

And boring version of "import" in [@ciel's][ciel_profile] [solution][pangram-ciel]. 

```python
import string;check_pangram=lambda t:string.ascii_uppercase in str().join(sorted(list(set(t.upper()))))
```

### [Binary count][binary-count]

Convert a number to the binary format and count how many unities (1) are in the number spelling.

Short, simple, clear. In ["lambda" solution][binary-count-mastak] by [@mastak][mastak_profile].

```python
checkio = lambda n: bin(n).count('1')
```

### [Number Base][number-radix]

You are given a positive number as a string along with the radix for it. 
Your function should convert it into decimal form.

Yes, it's really obviously for Python. So let's look at [the short solution][number-radix-shiracamus] by [@shiracamus][shiracamus_profile]

```python
checkio=lambda s,r:int(('-1',s)[int(max(s),36)<r],r)
```

### [Common Words][common-words]

You are given two string with words separated by commas. Try to find what is common between these strings.

Yep, [@somnambulism][somnambulism_profile] didn't use sets in ["oneliner"][common-words-somnambulism].

```python
checkio = lambda a, b: ','.join([x for x in sorted(a.split(',')) if x in b.split(',')])
```

### [Absolute sorting][absolute-sorting]

An array (a tuple) has various numbers. You should sort it, but sort it by absolute value in ascending order.

And again ["Obvious"][absolute-sorting-nickie] solution by [@nickie][nickie_profile].

```python
checkio=lambda a:sorted(a,key=abs)
```

### [Building Base][building-base]

This is not a base mission and players should write a class with the given requirement.

Here I've not found a formal one-liner, but I think [this solition with the simple title "zzdgnczfgdmksjdgfjs"][building-base-samulih]
by [@samulih][samulih_profile] can be counted as one-liner.


```python
class Building:
    __repr__ = lambda s: '%s%s' % (s.__class__.__name__, s.d)
    def __init__(s, *args, methods=('area', 'volume', 'corners')):
        s.d, ns, we, r = (args + (10,))[:5], ('sou', 'nor'), ('we', 'ea'), (0, 1)
        s.__dict__.update({k: lambda n=n: ({'%sth-%sst' % (ns[i], we[j]):
        [s.d[0]+s.d[3]*i, s.d[1]+s.d[2]*j] for i in r for j in r}) if n>1 else
        s.d[2]*s.d[3]*s.d[4]**(n&1) for n, k in enumerate(methods)})
```

### [Friends][friends]

And again a mission where you need to write a class.

Yes, again non formal one-liner, but a set of one-liners in ["lambda" solution][friends-jcg] by [@jcg][jcg_profile]. 

```python
class Friends(set):
    __init__ = lambda self, connections: self.update(map(frozenset, connections))
    add = lambda self, connection: not(connection in self or super().add(frozenset(connection)))
    remove = lambda self, connection: connection in self and not super().discard(frozenset(connection))
    names = lambda self: set.union(*map(set,self))
    connected = lambda self, name: set().union(*filter(lambda x:name in x, self))-{name}
​```


### What next?

We finished our Elementary island with 20 missions in 29 strings (last two mission broke it).
If you have ideas for the next week solution overview -- feel free to write it us.
That's all folks for today. Bye!

<!--------------------------------------------------------------------------------------------------------------------->

[oneliners_p1]: http://www.checkio.org/blog/elementary-one-liners/

<!--Mission Links-->
[count-inversions]: http://www.checkio.org/mission/count-inversions/share/35d94b8ac5a1dfa2d66132b677fdc359/
[end-of-other]: http://www.checkio.org/mission/end-of-other/share/5cb25ebe00369db4496f434ec1c0e1a9/
[days-diff]: http://www.checkio.org/mission/days-diff/share/04f5391af9e2e53a180759136826fd8a/
[pangram]: http://www.checkio.org/mission/pangram/share/6d2c66db9c7d72144d48c01ae323e868/
[binary-count]: http://www.checkio.org/mission/binary-count/share/8819896d0c21b21019bb9bc4e85ca6ee/
[number-radix]: http://www.checkio.org/mission/number-radix/share/62fed2170357aa9592b96e4253df91ec/
[common-words]: http://www.checkio.org/mission/common-words/share/79b819e840b3432f103244e29f0dad33/
[absolute-sorting]: http://www.checkio.org/mission/absolute-sorting/share/ba39943ed65e59c43749301605f0b886/
[building-base]: http://www.checkio.org/mission/building-base/share/3de02090eb5fac4f0da0ced85f9f3f61/
[friends]: http://www.checkio.org/mission/friends/share/cc176bba8e683618f5dc27c961cdfe55/


<!--Users-->
[nickie_profile]: http://www.checkio.org/user/nickie/
[DiZ_profile]: http://www.checkio.org/user/DiZ/
[aggelgian_profile]: http://www.checkio.org/user/aggelgian/
[suic_profile]: http://www.checkio.org/user/suic/
[veky_profile]: http://www.checkio.org/user/veky/
[Tubis_profile]: http://www.checkio.org/user/Tubis/
[Uladzimir_profile]: http://www.checkio.org/user/Uladzimir/
[Sim0000_profile]: http://www.checkio.org/user/Sim0000/
[harold_666_profile]: http://www.checkio.org/user/harold_666/
[Amachua_profile]: http://www.checkio.org/user/Amachua/
[Apua_profile]: http://www.checkio.org/user/Apua/
[mastak_profile]: http://www.checkio.org/user/mastak/
[shiracamus_profile]: http://www.checkio.org/user/shiracamus/
[somnambulism_profile]: http://www.checkio.org/user/somnambulism/
[nickie_profile]: http://www.checkio.org/user/nickie/
[samulih_profile]: http://www.checkio.org/user/samulih/
[jcg_profile]: http://www.checkio.org/user/jcg/

<!--solutions-->
[count-inversion-solution]: http://www.checkio.org/mission/count-inversions/publications/veky/python-3/gallery/share/c7f7eb90b2f34e2f3d9e0bd29830e096/
[end-of-other-Apua]: http://www.checkio.org/mission/end-of-other/publications/Apua/python-3/just-one-liner/share/45a776635da6ae2e0c08e29ad198c1d1/
[days-diff-DiZ]: http://www.checkio.org/mission/days-diff/publications/DiZ/python-3/oneliner/share/12d5e216b08f2934f80f369cf78b9dfd/
[pangram-ciel]: http://www.checkio.org/mission/pangram/publications/ciel/python-3/one-liner-without-quotes/share/4f7637ffe8cf1a765f65d98121437dbf/
[binary-count-mastak]: http://www.checkio.org/mission/binary-count/publications/mastak/python-27/lambda/share/3397cd66a1417ecaf710011231066eb5/
[number-radix-shiracamus]: http://www.checkio.org/mission/number-radix/publications/shiracamus/python-3/second/share/2c6641d04406aa8fb97d5ba1b0e2c68e/
[common-words-somnambulism]: http://www.checkio.org/mission/common-words/publications/somnambulism/python-3/oneline/share/8a3881ace5334504d673f654783759a7/
[absolute-sorting-nickie]: http://www.checkio.org/mission/absolute-sorting/publications/nickie/python-3/obvious/share/c4da6225379a5654cd21fdf90f5ca0ea/
[building-base-samulih]: http://www.checkio.org/mission/building-base/publications/samulih/python-3/zzdgnczfgdmksjdgfjs/share/4b70ca1fdee5fd14a8877fab4f0561a9/
[friends-jcg]: http://www.checkio.org/mission/friends/publications/jcg/python-3/lambda/share/ce3d4ac1a0d3453c3abfc2ba9a52d705/