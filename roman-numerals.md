# Roman Numerals

Republic, Julius Caesar and  Colosseum. Yes, I'm talking about Ancient Rome.
Couple days ago I've read Conn Iggulden's book about Caesar inherit - Octavian
and remember about Checkio Mission "Roman Numerals". So let's look at that today. 

Roman numerals come from the ancient Roman numbering system.
They are based on specific letters of the alphabet which are combined to signify the sum 
(or, in some cases, the difference) of their values. The first ten Roman numerals are:

`I, II, III, IV, V, VI, VII, VIII, IX, and X.`

The Roman numeral system is decimal based but not directly positional and does not include a zero.
Roman numerals are based on combinations of these seven symbols:

![Roman-numerals](http://checkio.s3.amazonaws.com/blog/share/roman-numeral-example.svg)

## Simple Solution

We can single out "elemental" numbers and break the given number at these elements top down.
Here is those "elements" for the roman numerals:
 
```
"M" 1000, "CM" 900,
"D"  500, "CD" 400,
"C"  100, "XC"  90,
"L"   50, "XL"  40,
"X"   10, "IX"   9,
"V"    5, "IV"   4,
"I"    1
```

Next we try to subtract these numbers from the given until we can. And connect characters
from left to right. The result is our number in roman form.

```
ELEMENTS = (("M", 1000), ("CM", 900), ("D", 500), ("CD", 400),
            ("C", 100), ("XC", 90), ("L", 50), ("XL", 40),
            ("X", 10), ("IX", 9), ("V", 5), ("IV", 4), ("I", 1))


def checkio(number):
    result = ""
    for roman, n in ELEMENTS:
        if n <= number:
            result += roman * (number // n)
            number %= n
    return result
```

## "Clear" Solutions

In "Clear" category [@JulianNicholls's][JulianNicholls] ["First" solution][JulianNicholls-solution]
has many players votes and uses simple clear algorithm.

The next is [Mark Pilgrim's realisation][macfreek-solution] was written by [@macfreek][macfreek].
This solution is like was described early but with comments and other "production" features.

## "Creative" solutions (just for fun)

How about [veeeery long one-liner][ciel-solution] from [@ciel][ciel]?

```
checkio=lambda data: ['','M','MM','MMM'][data//1000]+['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM'][data//100%10]+['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC'][data//10%10]+['','I','II','III','IV','V','VI','VII','VIII','IX'][data%10]
​```

Or ["Recursive, short, weird but works! :)"][hrvoje-solution] by [@hrvoje][hrvoje].

```
def checkio(data):
    s = lambda b,z: '' if not z else str(s(b%z[0][0], z[1:])) + (b//z[0][0])*z[0][1]    
    return s(data, [(1000, 'M'), (900, 'MC'), (500, 'D'), (400, 'DC'), (100, 'C'), (90, 'CX'), (50, 'L'), (40, 'LX'), (10, 'X'), (9, 'XI'), (5, 'V'), (4, 'VI'), (1, 'I')])[::-1]
```

And [puzzler "dict FTW"][veky-solution] from [@veky][veky] instead weekend crossword for you.

```
def checkio(x):
    a,r="",{}
    for i in range(3):
        p,(j,c,d)=10**i,"IVXLCDM"[2*i:][:3]
        r.update({p:j,5*p:c,4*p:j+c,9*p:j+d,10*p:d})
    for k in reversed(sorted(r)):
        a+=x//k*r[k]
        x%=k
    return a
```

That's all folks. Maybe you would to review some CiO mission?

<!--------------------------------------------------------------------------------------------------------------------->

[roman-numerals]: http://www.checkio.org/mission/roman-numerals/share/bc3e30309299b0bae4de1abfe865b391/

[JulianNicholls]: http://www.checkio.org/user/JulianNicholls/
[macfreek]: http://www.checkio.org/user/macfreek/
[ciel]: http://www.checkio.org/user/ciel/
[hrvoje]: http://www.checkio.org/user/hrvoje/
[veky]: http://www.checkio.org/user/veky/

[JulianNicholls-solution]: http://www.checkio.org/mission/roman-numerals/publications/JulianNicholls/python-3/first/share/32d77904208759d1fdbda5e915ac5e03/
[macfreek-solution]: http://www.checkio.org/mission/roman-numerals/publications/macfreek/python-3/mark-pilgrims-library/share/cf938a8d7047aa73017af3e9286e4e10/
[ciel-solution]: http://www.checkio.org/mission/roman-numerals/publications/ciel/python-3/second/share/c5ae14877855e94a941c90320880d179/
[hrvoje-solution]: http://www.checkio.org/mission/roman-numerals/publications/hrvoje/python-27/recursive-short-weird-but-works/share/32cea072123936826684609a547c07fd/
[veky-solution]: http://www.checkio.org/mission/roman-numerals/publications/veky/python-27/dict-ftw/share/751f02120f45aa26f2a5628ca3d4bd70/