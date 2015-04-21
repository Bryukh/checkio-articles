Hi, CiO friends!

On CheckiO we have various missions. Sometimes you just need to solve input-output function.
Sometimes it's codeGolf. Sometimes you will play a game with score. 
But the couple of missions are different. These are Creative or as we call them "code essay" missions.
In this kind of tasks you don't need to solve anything -- one test and any or a given answer.
But you can write you thoughts about the given problem in code (or in code comments).
And today we will look at ["I Love Python" mission][iluvpython].

## Description

This mission is simple to solve.
You are given a function called "i_love_python" which will only return the phrase - "I love Python!".
Let's write an essay in python code which will explain why you love python.

For this mission players get points only when other players vote for their specific solution.

## Code essays

The most number of solutions are written as comment novels or something brain twisted.
I will try to choose the most interesting essays, but sorry if I skipped some other creative solutions.
Feel free to put links or solutions in comments.

First of all i think i should post ["Magnum opus" essay][veky_solution] 
by our top level and one of the most famous CheckiO player -- [@veky](http://www.checkio.org/user/veky/).
He is one of the smartest person who I know and this is not eyewash, I really think so.
And this is the great solution because here function are weaved in the good essay. 

```python
(lambda _:globals().__setitem__(_.lower().translate(dict(enumerate(( '_'
,None),1<<5))),lambda:_))("""\
In my wildest dreams, I never imagined I'd have to write _essays_ here
on CheckiO. Yes, I know: who's talking? Really, I've written many mind-boggling
things here already, and I have puzzled many folks reading my solutions.
It's only fair that I puzzle myself now. :-\
So, what to write? You have already seen enough to realize that I consider
Python one of the most excellent inventions our civilization has ever made, not
only in the tier of programming languages. It still puzzles you: why one would
think so? Puzzling is good, because in this jaded culture, it is one of the
rare ways ideas can still be learned. Of course, my essay won't magically
enlighten you. But neither will Zen of Python by itself. Those are only small
chunks of an infinitely rich mosaic that's waiting for you to discover it on
your terms...
While you are trying to "digest" this essay, and wondering if it is an
essay at all, think: we must know, we will know. Good luck!"""[::73])
```

Next is short and simple. but funny ["Clearly"][gyahun_dash_solution] by [@gyahun_dash](http://www.checkio.org/user/gyahun_dash/)
True love does not need reasons and nothing impossible if no complaints.

```
def i_love_python(complaints='', impossibles={}, reasons=None, love=True):
    return 'I love Python!'
```

[@ciel]() has written ["Brainf\*\*ck" solution][] and yes it's BF with classes.

```python
class BF:
    buffer=[0]*9999
    ptr=0
    def execute(self,s):
        ret=''
        i=0
        while i<len(s):
            if s[i]=='>': self.ptr+=1
            elif s[i]=='<': self.ptr-=1
            elif s[i]=='+': self.buffer[self.ptr]+=1
            elif s[i]=='-': self.buffer[self.ptr]-=1
            elif s[i]=='.': ret+=chr(self.buffer[self.ptr])
            elif s[i]==',': pass #getchar
            elif s[i]=='[':
                if self.buffer[self.ptr]: ret+=self.execute(s[i+1:])
                marker=1
                while marker:
                    if s[i+1]=='[': marker+=1
                    if s[i+1]==']': marker-=1
                    i+=1
            elif s[i]==']':
                if self.buffer[self.ptr]: i=-1
                else: return ret
            i+=1
        return ret
​
i_love_python=lambda:BF().execute('++++++++[>>+>++>+++>++++>+++++>++++++>+++++++>++++++++>+++++++++>++++++++++>+++++++++++>++++++++++++>+++++++++++++>++++++++++++++>+++++++++++++++>++++++++++++++++>+++++++++++++++++>++++++++++++++++++>+++++++++++++++++++>++++++++++++++++++++>+++++++++++++++++++++>++++++++++++++++++++++>+++++++++++++++++++++++>++++++++++++++++++++++++>+++++++++++++++++++++++++>++++++++++++++++++++++++++>+++++++++++++++++++++++++++>++++++++++++++++++++++++++++>+++++++++++++++++++++++++++++>++++++++++++++++++++++++++++++>+++++++++++++++++++++++++++++++<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<-]>>>>>>>>>>+.<<<<<.>>>>>>>>>++++.+++.>++++++.<<+++++.<<<<<<<<.>>>>>>.>>>>>+.<--.<-------.+++++++.-.<<<<<<<<<+.')
​```

exPHP developer biography in [@profuel's](http://www.checkio.org/user/profuel/) ["First" solution][profuel_solution].

```python
def i_love_python():
    programming_years = 0
    while programming_years < 5:
        I_was_bored_PHP_developer = True
        programming_years+= 1
    if programming_years>=5:
        I_got_into_python_and_DJango_environment = True
        it_changed_my_programming_attitude_completely = True
        
        if type("I get into strange PHP unlike situation"):
            I_feel_like_I_hate_python_and_getting_back_to_basic_documentation = True
        
    return "I love Python!"
```

## Comment novels

Many players wrote their thoughts as comment lines in code.
Some stories are interesting and I think it will not take too many time to read them.
I will put some of them just with quotes.

[@reviewboy](http://www.checkio.org/user/reviewboy/) with [the story][reviewboy_story] which begin by TRS-80.

> Why do I love Python? It's restored my enthusiasm for coding.

[@Ch0bits](http://www.checkio.org/user/Ch0bits/) with ["Philosophic principles is main reason"][Ch0bits_story].

> Although I don't use Python directly for my work. It's just a hobby.

[@abe.dillon](http://www.checkio.org/user/abe.dillon/) with [readability essay][abe_dillon_story].

> Well written Python code comes the closest to reading like english

[@smilicic](http://www.checkio.org/user/smilicic/) about [his path to Python][smilicic_story].

> ...I love Python because it's the best language
 I've tried for expressing exact mathematical thoughts without much bureaucracy.

And that is just small extract from many-many stories and code puzzles.
I think you can find other interesting solutions and share them in comments here.

That's all folks. Goodbye, see you next friday.

[iluvpython]: http://www.checkio.org/mission/i-love-python/share/43c946197f632388709d17d8b9714f72/
[veky_solution]: http://www.checkio.org/mission/i-love-python/publications/veky/python-3/magnum-opus/share/47e1808a004aeec610a39acc01808e8a/
[gyahun_dash_solution]: http://www.checkio.org/mission/i-love-python/publications/gyahun_dash/python-3/clearly/share/8479e92bf678d675a6925a13a423a33d/
[ciel_solution]: http://www.checkio.org/mission/i-love-python/publications/ciel/python-3/brainfk/share/e192da78eb8590b7407ce06f121167ae/
[profuel_solution]: http://www.checkio.org/mission/i-love-python/publications/profuel/python-27/first/share/d3c150951399cf6f90c7fa1102b30132/

[reviewboy_story]: http://www.checkio.org/mission/i-love-python/publications/reviewboy/python-27/first/share/c18f6e42bf399dda1d8d32c3fcece53b/
[Ch0bits_story]: http://www.checkio.org/mission/i-love-python/publications/Ch0bits/python-3/philosophic-principles-is-main-reason/share/d742c042640d7bcaf5e6b576df997007/
[abe_dillon_story]: http://www.checkio.org/mission/i-love-python/publications/abe.dillon/python-3/first/share/bd5ffbb462efa1317005229410d3d79b/
[smilicic_story]: http://www.checkio.org/mission/i-love-python/publications/smilicic/python-3/first/share/65fcbf05ff341549a47e42a438c3f6f1/
