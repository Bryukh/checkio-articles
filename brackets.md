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




[brackets]: http://www.checkio.org/mission/brackets/share/440e9f6d6367b188e86fdf5797f7b087/
[wiki-stack]: http://en.wikipedia.org/wiki/Stack_(abstract_data_type)
[pytutor]: http://www.pythontutor.com/visualize.html#code=def+checkio(data)%3A%0A++++stack+%3D+%5B%5D++%23+Yes,+we+can+use+deque%0A++++pairs+%3D+%7B'('%3A+')',+'%5B'%3A+'%5D',+'%7B'%3A+'%7D'%7D%0A++++for+token+in+data%3A%0A++++++++if+token+in+pairs.keys()%3A%0A++++++++++++stack.append(token)%0A++++++++elif+token+in+pairs.values()%3A%0A++++++++++++if+stack+and+token+%3D%3D+pairs%5Bstack%5B-1%5D%5D%3A%0A++++++++++++++++stack.pop()%0A++++++++++++else%3A%0A++++++++++++++++return+False%0A++++return+not+bool(stack)%0A%0Aassert+checkio(%22((5%2B3)*2%2B1)%22)%0Aassert+checkio(%22%7B%5B(3%2B1)%2B2%5D%2B%7D%22)%0Aassert+not+checkio(%22(3%2B%7B1-1)%7D%22)%0Aassert+checkio(%22%5B1%2B1%5D%2B(2*2)-%7B3/3%7D%22)%0Aassert+not+checkio(%22((%7B%5B(((1)-2)%2B3)-3%5D/3%7D-3)%22)%0Aassert+checkio(%222%2B3%22)%0A&mode=display&origin=opt-frontend.js&cumulative=false&heapPrimitives=false&textReferences=false&py=2&rawInputLstJSON=%5B%5D&curInstr=0
