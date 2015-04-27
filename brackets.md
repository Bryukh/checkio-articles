Hi!

When you open "Electronic Station" the first mission that meets you is
["Brackets"][brackets]. This is a simple, but interesting and useful mission.
"Brackets" can be solved by various methods and algorithms and CiO players shown
many interesting solutions for that.

## Description

You are given an expression with numbers, brackets and operators.
For this task only the brackets matter.
Brackets come in three flavors: "{}" "()" or "[]".
Brackets are used to determine scope or to restrict some expression.
If a bracket is open, then it must be closed with a closing bracket of the same type.
The scope of a bracket must not intersected by another bracket.
In this task you should make a decision, whether to correct an expression or
not based on the brackets. Do not worry about operators and operands.

## Stack Solution

I've solved this mission with a [stack][wiki-stack].
Iterate a given text symbol by symbol.
- if a character is not a bracket then skip it;
- if a character is an opened bracket then put in the stack;
- if a character is a closed bracket, then try to take the top element of the stack
and check whether they form a pair of identical brackets: "()", "[]" or "{}".

If we try to take an element from the stack and it's an empty or after checking
all symbols the stack is not an empty, then our expression is wrong.

```python
def checkio(data):
    stack = []  # Yes, we can use deque
    pairs = {'(': ')', '[': ']', '{': '}'}
    for token in data:
        if token in pairs.keys():
            stack.append(token)
        elif token in pairs.values():
            if stack and token == pairs[stack[-1]]:
                stack.pop()
            else:
                return False
    return not bool(stack)
```

You can examine this code execution with [Pythontutor service][pytutor]

## Stackless Solution

This mission can be solved without stack and only with string methods as
in [@blabaster's](http://www.checkio.org/user/blabaster/)
["Stackless" solution][blabaster-solution]

```python
def checkio(expression):
    s = ''.join(c for c in expression if c in '([{}])')
    while s:
        s0, s = s, s.replace('()', '').replace('[]', '').replace('{}', '')
        if s == s0:
            return False
    return True
```

As first here we "clear" a text and keep only brackets.
So a string like "{[(3+1)+2]+}+()" became to "{[()]}()".
Next we remove all pairs of brackets which are near each other like "()", "[]" or "{}".
If for some step we don't remove anything and the string is not an empty, then
the given text is wrong.
You can examine this code execution with [Pythontutor - "stackless"][pyt-stackless].

And short, less readable and recursive version of this algorithm in
[@coells's](http://www.checkio.org/user/coells/) [solution][coells-first].

```python
import re
EXPR = re.compile('\[\]|\(\)|\{\}|\d|[\+\-\*\/]')
checkio = lambda e, f = '': True if e == '' else False if e == f else checkio(EXPR.sub('', e), e)
```


## "Now They Have Two Problems"

By the way about regexp -- [@LuigiMoro](http://www.checkio.org/user/LuigiMoro/)
written [almost regexp solution][LuigiMoro-regexp].
He prepared three regexp expressions and if any of it's matching,
then the function returns False.
But before this checking we should check that quantity of opened brackets are equal
to closed for each kind.

```python
import re
​
pattern_1 = re.compile(".*\{[\w|\+|\-|\*|/|\s]+[\]|\)].*")
pattern_2 = re.compile(".*\[[\w|\+|\-|\*|/|\s]+[\}|\)].*")
pattern_3 = re.compile(".*\([\w|\+|\-|\*|/|\s]+[\}|\]].*")

def checkio(expression):​
    if (expression.count("{") != expression.count("}") or
        expression.count("[") != expression.count("]") or
        expression.count("(") != expression.count(")")) :
        return False

    return (pattern_1.match(expression) or pattern_2.match(expression) or pattern_3.match(expression)) is None
```

## Fython

I'm not sure why did [@astynax84](http://www.checkio.org/user/astynax84/)
placed "Fython" in [technically oneliner solution][astyx-fython].
Yes, this is a oneliner, but it's reintended for "readability".

```python
checkio = lambda s: reduce(lambda (f, stk), x:
    ((False, None) if not f else (
        (f, ({"[":"]", "{":"}", "(":")"}[x], stk))
        if x in "[({" else (
            (f, stk) if x not in "]})" else (
                (False, None)
                if stk is None or x != stk[0] else
                (True, stk[1])
            )
        )
    )), s, (True, None)) == (True, None)
```

And at this mind twisted solution I say goodbye -- That's all folks about brackets.

[brackets]: http://www.checkio.org/mission/brackets/share/440e9f6d6367b188e86fdf5797f7b087/
[wiki-stack]: http://en.wikipedia.org/wiki/Stack_(abstract_data_type)
[pytutor]: http://www.pythontutor.com/visualize.html#code=def+checkio(data)%3A%0A++++stack+%3D+%5B%5D++%23+Yes,+we+can+use+deque%0A++++pairs+%3D+%7B'('%3A+')',+'%5B'%3A+'%5D',+'%7B'%3A+'%7D'%7D%0A++++for+token+in+data%3A%0A++++++++if+token+in+pairs.keys()%3A%0A++++++++++++stack.append(token)%0A++++++++elif+token+in+pairs.values()%3A%0A++++++++++++if+stack+and+token+%3D%3D+pairs%5Bstack%5B-1%5D%5D%3A%0A++++++++++++++++stack.pop()%0A++++++++++++else%3A%0A++++++++++++++++return+False%0A++++return+not+bool(stack)%0A%0Aassert+checkio(%22((5%2B3)*2%2B1)%22)%0Aassert+checkio(%22%7B%5B(3%2B1)%2B2%5D%2B%7D%22)%0Aassert+not+checkio(%22(3%2B%7B1-1)%7D%22)%0Aassert+checkio(%22%5B1%2B1%5D%2B(2*2)-%7B3/3%7D%22)%0Aassert+not+checkio(%22((%7B%5B(((1)-2)%2B3)-3%5D/3%7D-3)%22)%0Aassert+checkio(%222%2B3%22)%0A&mode=display&origin=opt-frontend.js&cumulative=false&heapPrimitives=false&textReferences=false&py=2&rawInputLstJSON=%5B%5D&curInstr=0

[blabaster-solution]: http://www.checkio.org/mission/brackets/publications/blabaster/python-3/stackless/share/fea53ef208c6465eca10d06baa28fe0f/

[pyt-stackless]: http://www.pythontutor.com/visualize.html#code=def+checkio(expression)%3A%0A++++s+%3D+''.join(c+for+c+in+expression+if+c+in+'(%5B%7B%7D%5D)')%0A++++while+s%3A%0A++++++++s0,+s+%3D+s,+s.replace('()',+'').replace('%5B%5D',+'').replace('%7B%7D',+'')%0A++++++++if+s+%3D%3D+s0%3A%0A++++++++++++return+False%0A++++return+True%0A%0Aassert+checkio(%22((5%2B3)*2%2B1)%22)%0Aassert+checkio(%22%7B%5B(3%2B1)%2B2%5D%2B%7D%22)%0Aassert+not+checkio(%22(3%2B%7B1-1)%7D%22)%0Aassert+checkio(%22%5B1%2B1%5D%2B(2*2)-%7B3/3%7D%22)%0Aassert+not+checkio(%22((%7B%5B(((1)-2)%2B3)-3%5D/3%7D-3)%22)%0Aassert+checkio(%222%2B3%22)%0A&mode=display&origin=opt-frontend.js&cumulative=false&heapPrimitives=false&textReferences=false&py=3&rawInputLstJSON=%5B%5D&curInstr=0

[coells-first]: http://www.checkio.org/mission/brackets/publications/coells/python-3/first/share/8a512005e860e4fb3a36051c6db9942f/

[LuigiMoro-regexp]: http://www.checkio.org/mission/brackets/publications/LuigiMoro/python-3/first/share/474678e61ef8b66babbf9da48ab55f81/

[astyx-fython]: http://www.checkio.org/mission/brackets/publications/astynax84/python-27/third/share/06b6309b90c98e2afa0dff9b63d1565e/
