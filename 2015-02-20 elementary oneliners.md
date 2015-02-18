Hi!

As you may know we have a special island for our coding newbies -- ["Elementary"][elementary_island].
On this island we've created very simple missions which include hints to help solve them. 
So if you just have finished the TreeHouse or CodeAcademy courses, or you already know some python syntax,
then this island is absolutely for you.

But our more advanced players are having fun there too. For example, they are adding an extra challenge and writing 'one-liners'.
A one-liner is a program which takes just one line of code. 
For this weekly overview we will look at some of the interesting one-liners from our players.

### [Fizz-Buzz][fizz_buzz]

I think you all know about "Fizz Buzz" game by now, it's often used to teach children division.

And we're opening today's review with [@nickie's][nickie_profile] ["String arithmetic"][fizz_buzz_nickie] solution.
He is using `[:-1]` to cut some final whitespaces and if it's an empty string, converts the number.

```python
checkio=lambda n:("Fizz "*(1-n%3)+"Buzz "*(1-n%5))[:-1]or str(n)
```

### [Index Power][index_power]

Find the N-th power of the element in the array with the index N.

[@DiZ][DiZ_profile] has written a short [solution](index_power_DiZ) named "45". 
I think it's not a mystery to get the meaning of this solution's title.

```python
index_power=lambda a,n:-(len(a)<=n)or a[n]**n
```

### [Even The Last][even_last]

Take the sum of the elements with even indexes, then multiply this summed number and the final element of the array.

Here I took a look at [@aggelgian's][aggelgian_profile] [solution][even_last_aggelgian]. 
One small remark: "Clear" may not be the best category for this solution, but it sure is short and simple.
 
```python
checkio=lambda x: sum(x[::2])*x[-1] if x else 0
```

### [Monkey Typing](monkey_typing)

You are given text and a set of words. Find how many of the listed words are in the given text.

And [suic's][suic_solution] ["Another one-liner"][monkey_typing_suic] solution certainly has a functional style.

```python
count_words = lambda t, w: len(list(filter(t.lower().count, w)))
```

### [Secret Message][secret_message]

Gather all of the capital letters in one word together in the order that they appear in the text.

I think in this case [@veky's][veky_profile] ["filter" solution][secret_message_veky] is deffinitely placed in the "Clear" section correctly.
It's a simple and functional chunk of code in the PEP8 style.

```python
find_message = lambda text: ''.join(filter(str.isupper, text))
```

### [Three Words][three_words]

Check if the string contains three words (words contains only letters) in succession.

For this mission I will take [@Tubis's][Tubis_profile] [solution][three_words_tubis]. 
Yes, I know that's a fake account, and I know who is it. :-)

```python
checkio=lambda x:"www" in "".join('w' if w.isalpha() else 'd' for w in x.split())
```

### [The Most Numbers][most_numbers]

Find the difference between the maximum and minimum element from a number array.

Honestly for this mission we have many identical one-liners,
so I've taken [@Uladzimir's][Uladzimir_profile] [solution][most_numbers_Uladzimir] from the top of the list.

```python
checkio = lambda *args: max(args) - min(args) if args else 0
```

### [Boolean Algebra](boolean_algebra)

In this mission you should implement some boolean operations: conjunction, disjunction, implication, exclusive and equivalence.

This is not the shortest, but it's short enough ["64 chars"][boolean_algebra_Sim0000] by [@Sim0000][Sim0000_profile].

```python
boolean=lambda x,y,o:(x&y,x|y,x<=y,x^y,x==y)['oimxq'.find(o[1])]
```


### [Right to Left][right_left]

Just replace all the "right" words with the "left" and join them with commas.

For this we will look at [harold_666's][harold_666_profile] [solution][right_left_harold_666].
The "join" is funny here.

```python
left_join=lambda phrases: ''.join(list(''.join([i+',' for i in phrases]))[0:-1]).replace('right','left')
```
### [Digits Multiplication][digits_multiplication]

You are given a positive integer. Your function should calculate the product of the digits excluding all the zeros.

[Amachua][Amachua_profile] used "eval" for this mission in [his solution][digits_multiplication_Amachua].

```python
checkio = lambda n: eval("*".join(i for i in str(n) if i != '0'))
```

### To be continued...

This is only first half. In the next article we will take look at the second set of missions I dug up from the Elementary Island.


<!--------------------------------------------------------------------------------------------------------------------->

[elementary_island]: http://www.checkio.org/station/library/

<!--Mission Links-->
[fizz_buzz]: http://www.checkio.org/mission/fizz-buzz/share/a22c7465d4ecc1c7efad0113609f5697/
[index_power]: http://www.checkio.org/mission/index-power/share/6adc6eec6760ceb88833e2929de455e7/
[even_last]: http://www.checkio.org/mission/even-last/share/b1f3ac0442f6e0f5fb6bce42237a7275/
[monkey_typing]: http://www.checkio.org/mission/monkey-typing/share/18f3e365b0afbc53159c9e5a0f367246/
[secret_message]: http://www.checkio.org/mission/secret-message/share/4734114443b6d18a22f1ae2ebffcc2ec/
[three_words]: http://www.checkio.org/mission/three-words/share/3d3d08a8f6b6b20c3e915bfa7384fa7c/
[most_numbers]: http://www.checkio.org/mission/most-numbers/share/d52a7a08eed35bf390c78b501e69c152/
[boolean_algebra]: http://www.checkio.org/mission/boolean-algebra/share/efc4ce2e4b11276cd3a811075d70bf94/
[right_left]: http://www.checkio.org/mission/right-to-left/share/fdf0ee9eabb064af1ab5c2c9d78cc330/
[digits_multiplication]: http://www.checkio.org/mission/digits-multiplication/share/973c58b1aaaa73691f3388637048bb4b/


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

<!--solutions-->
[fizz_buzz_nickie]: http://www.checkio.org/mission/fizz-buzz/publications/nickie/python-3/string-arithmetic/share/5db4796565d5d5a78a7ff692f8a0f1d9/
[index_power_DiZ]: http://www.checkio.org/mission/index-power/publications/DiZ/python-3/45/share/31dc12bc71250606feedb9efb0d4c780/
[even_last_aggelgian]: http://www.checkio.org/mission/even-last/publications/aggelgian/python-3/first/share/a6e12bb48b6b23fe58da6e4b1ee57c7a/
[monkey_typing_suic]: http://www.checkio.org/mission/monkey-typing/publications/suic/python-3/another-one-liner/share/0decb5d0bfd4b377198125954d831adf/
[secret_message_veky]: http://www.checkio.org/mission/secret-message/publications/veky/python-3/filter/share/efd4e41ef30dcac9af99dcd6c84ae149/
[three_words_tubis]: http://www.checkio.org/mission/three-words/publications/Tubis/python-3/first/share/863c87edf8d31d3286afe2057388508b/
[most_numbers_Uladzimir]: http://www.checkio.org/mission/most-numbers/publications/Uladzimir/python-3/first/share/d87c9b5e0385ca0b0df9989536d76b1f/
[boolean_algebra_Sim0000]: http://www.checkio.org/mission/boolean-algebra/publications/Sim0000/python-3/64-chars/share/94aaf42f250a2e6db1782e769f6ca86b/
[right_left_harold_666]: http://www.checkio.org/mission/right-to-left/publications/harold_666/python-27/first/share/014f7a3d9bb0185f247bea10ec460984/
[digits_multiplication_Amachua]: http://www.checkio.org/mission/digits-multiplication/publications/Amachua/python-3/first/share/c5b1cdf4b14739c921797eccfcac3ed3/
