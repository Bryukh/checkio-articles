Hi, CiO friends!

Early I told about a creative writing mission ["I love Python"][article-link].
And today I will look at the second this kind mission -- ["The best number ever"][mission-link].

The mission is simple. Write a function that return any number. But try to describe why is
your number the best. For example, Shaldon Cooper thinks that 73 is the best number ever and
he can explain it.

Let's look that CheckiO players would say about their best numbers.

And [@Amachua](http://www.checkio.org/user/Amachua/) opens our chart with his
["Dictionary"](http://www.checkio.org/mission/the-best-number-ever/publications/Amachua/python-3/second/share/2f3a43ae082fca8058a5f5ac64c32f04/).
He collected an interesting set of names and peoples. But this solution is still too far
to completion, so propose your ideas to the author in comments and maybe later we will see
"The Full Dictionary of the best numbers" [@Amachua](http://www.checkio.org/user/Amachua/).

The next [@Faibbus](http://www.checkio.org/user/Faibbus/) will introduce
for us [The Most Amazing, Ancient, and Singular Number **Wau**](http://www.checkio.org/mission/the-best-number-ever/publications/Faibbus/python-27/first-wau/share/4090c596b29e005051ef955117e868e2/).

```
def checkio( *data):
    from math import sqrt, cos, pi
    from random import randrange, seed
    seed("Wau is the best number ever !")

    Wau = 42. / ord('*')  # divide 42 by anything...

    assert Wau == int(Wau), "Your number isn't an integer"

    for i in xrange(1337):
        assert Wau == (Wau**i+Wau)/(sqrt(Wau)-cos(pi*Wau**i)) , "Your number isn't great enough... (%i)"%i

    for i in xrange(13**2):
        assert not (randrange(1337**42)-int(pi**i))%Wau , "Your number lacks randomness... (%i)"%i

    gold_ratio = (sqrt(5) - 1)/2

    n=randrange(0xD15EA5E/0xFEA12)
    for i in xrange(0xB4B3):
        n = Wau /(Wau + n)

    assert abs(n - gold_ratio) < 1e-6 , "Your number doesn't prettify anything... (%f) (%f) (%f)"%(n-gold_ratio, n, gold_ratio)

    """\
    But wait, there's even more,

        Wau: The Most Amazing, Ancient, and Singular Number
        see https://www.youtube.com/watch?v=GFLkou8NvJo
    """
    return int(Wau)
```

[@grigoriytretyakov](http://www.checkio.org/user/grigoriytretyakov/) written
an essay with variable names to prove about ["16 is the best number ever"](http://www.checkio.org/mission/the-best-number-ever/publications/grigoriytretyakov/python-3/first-on-the-best-number-ever/share/ae88f82a0d8d286394d2cf4372af524d/).

```
def checkio():
    i = 16
    in_hex_has_only_1_and_0 = not bool(set(hex(i)[2:]) - set('01'))
    oct_twice_bigger_than_hex_in_10_radix = int(oct(i)[2:]) / int(hex(i)[2:]) == 2.0
    convert_to_hex_to_str_give_two_in_bin = int(hex(i)[2:], 2)
    count_of_0_in_4_times = bin(i)[2:].count('0') / hex(i)[2:].count('0')
    and_2_in_power_4_give_stil_16 = 2 ** count_of_0_in_4_times
​
    best_number = (
        in_hex_has_only_1_and_0 and
        oct_twice_bigger_than_hex_in_10_radix and
        convert_to_hex_to_str_give_two_in_bin and
        count_of_0_in_4_times == 4 and
        and_2_in_power_4_give_stil_16 == 16
    )
​
    if best_number:
        return i
```

If you would like to read a tale for your kids, then you can take [@Juge_Ti's](http://www.checkio.org/user/Juge_Ti/) ["Secret Magic Number" short novel](http://www.checkio.org/mission/the-best-number-ever/publications/Juge_Ti/python-3/secret-magic-number/share/094f44e1f59cd2188ecaa1539f9974ca/). I don't want to spoiler, so you need to run this
if you need to know the secret number.

[@HonzaKral](http://www.checkio.org/user/HonzaKral/) proved Sheldon's version ["Inspired by BrainF**k"](http://www.checkio.org/mission/the-best-number-ever/publications/HonzaKral/python-3/inspired-by-brainfk/share/5b57ad0090c74d6dca5a3ca6b998d17f/)

```
OPS = {
    '0': lambda _: 0,
    '+': lambda buf: buf + 1,
    '<': lambda buf: buf * 10
}
​
def bf(it):
    buf = None
    for i in it:
        buf = OPS[i](buf)
    return buf

def checkio():
    'And the best number ever is...'
    return bf("0+++++++<+++")
```

And for dessert funny solution from [@StefanPochmann]http://www.checkio.org/user/StefanPochmann/)
["I'm sure you'll agree"](http://www.checkio.org/mission/the-best-number-ever/publications/StefanPochmann/python-3/im-sure-youll-agree/share/9d766dd139071ba8d493f54de6200fc7/).

```
checkio=lambda:int('https://www.youtube.com/watch?v=dQw4w9WgXcQ'.split('=')[1], 36)
```

That's all folks. Tell us about your best numbers.
