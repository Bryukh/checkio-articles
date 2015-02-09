Pangram Review
==============

Hello, CiO People!

Today I would examine the fresh CheckiO mission ["Pangram"][p].
This mission was based on an idea by [Sim0000][Sim0000_profile],
which had added to a recent forum [post][forum_post].
You can propose your own ideas there too and we will try to make them happen.

a [pangram][wikipedia] is a sentence which uses every letter of the alphabet at least once.
In this mission you need to check text and verify if the given sentence is a pangram for the English alphabet or not.

There are many methods which can be employed to solve this problem. 
As we can see, it's easy to write a solution with a time complexity of O(N), 
you just use hash table data types to solve the problem. 
However, we will not stop at this and will looking for more interesting solutions which were made by CheckiO players.

## Clear

The first solution we'll look at is titled ["First"][dagger126_first]
and was created by [dagger126](http://www.checkio.org/user/dagger126/) with a simple and obvious solution. 
There's a good usage of the built-in set data type.
 

    from string import ascii_lowercase​
    ​
    def check_pangram(text):
        return set(ascii_lowercase).issubset(set(text.lower()))


Here's an alternate method by [DmitriyS][DmitriyS_profile] titled 
["all() + string.ascii_lowercase"][DmitriyS_first]
As we can see from the title, this uses the "all" function with comprehension. 
It iterates all of the letters in the alphabet and check if they are in the given text.

```
def check_pangram(text):
    text = text.lower()
    return all(c in text for c in string.ascii_lowercase)
```

We have another ["First"][saklar13_first]
by [saklar13][saklar13_profile] this time. 
This solution presents a nice way to solve our problem without using the alphabet, 
but with rather the *str.isalpha* method.

```
check_pangram = lambda text: len({x for x in text.lower() if x.isalpha()}) == 26
```

## Creative

At the top of the creative category, we have the ["65" solution][DiZ_65]
by [DiZ][DiZ_profile]. Looks like a code golf solution with double meaning using "65"! ;-)

```
check_pangram=lambda t:set(map(chr,range(65,91)))<=set(t.upper())
```

["Not Very Clean but works"][schanjr_not_clean]
by [schanjr][schanjr_profile] is "the most complicated solution of the task" as the community member
[veky][veky_profile](http://www.checkio.org/user/veky/) puts it.
But this solution has made it in the "Creative" category, 
so I'm sure schanjr made something special. 
The solution has 20 strings, but this line should be especially noted:

```
...
if all(x is x>=2 for x in count.itervalues()):
...
```

[This comment][veky_not_clean_comment]
about using if-else for returns can be useful for newbies. In it, Veky explains the best practices.

If we would make an award for "the most complicated solution for a task", then I would nominate 
["First | Naive"][bundgaard_first]
by [bundgaard][bundgaard_profile].

## And

We often meet solutions which are written with Python but are not "in" Python - 
sometimes they use a LISP or Java style of coding for example. 
When I first started to learn Pythonm for example, I wrote C-code with Python syntax. Python gurus often found this style of code funny to read.

So, how about trying to write a "Pangram" solution with Python, but not in the Python style? Could you do it?

<!--------------------------------------------------------------------------------------------------------------------->

<!--General Links-->

[p]: http://www.checkio.org/mission/pangram/share/6d2c66db9c7d72144d48c01ae323e868/ "Pangram Share Link"
[forum_post]: http://www.checkio.org/forum/post/2977/mission-ideas/#comment-23718
[wikipedia]: https://en.wikipedia.org/wiki/Pangram

<!--Solution Links-->

[bundgaard_first]: http://www.checkio.org/mission/pangram/publications/bundgaard/python-3/first-naive/share/6b77e9e39c53e380163d0d101e1d1d47/
[DmitriyS_first]: http://www.checkio.org/mission/pangram/publications/DmitriyS/python-27/first/share/23bc0848d1244cf8fc056d46cf3a7a84/
[saklar13_first]: http://www.checkio.org/mission/pangram/publications/saklar13/python-3/first/share/79f383a0c08e1dac30dcf1ab8463d852/
[dagger126_first]: http://www.checkio.org/mission/pangram/publications/dagger126/python-3/first/share/2a462ede1eda10f6c3077357ec642a92/)
[DiZ_65]: http://www.checkio.org/mission/pangram/publications/DiZ/python-3/65/share/fab58c78c42b3e1d93e6e3b58a1dc1f4/
[schanjr_not_clean]: http://www.checkio.org/mission/pangram/publications/schanjr/python-27/not-very-clean-but-works/share/de57ea9d78879a7358b8dc5ef516402a/

<!--Profile Links-->
[Sim0000_profile]: http://www.checkio.org/user/Sim0000/
[saklar13_profile]: http://www.checkio.org/user/saklar13/
[DmitriyS_profile]: http://www.checkio.org/user/DmitriyS/
[DiZ_profile]: http://www.checkio.org/user/DiZ/
[schanjr_profile]: http://www.checkio.org/user/schanjr/
[bundgaard_profile]: http://www.checkio.org/user/bundgaard/
[veky_profile]: http://www.checkio.org/user/veky/

<!--Comment Links-->

[veky_not_clean_comment]: http://www.checkio.org/mission/pangram/publications/schanjr/python-27/not-very-clean-but-works/share/de57ea9d78879a7358b8dc5ef516402a/#comment-24174
