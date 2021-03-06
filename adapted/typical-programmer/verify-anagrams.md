Всем привет!

Сегодня я позволю себе небольшой эксперимент и вы не увидите решений от пользователей CheckiO.
И изучать мы будем задачу ["Проверка Анаграмм"("Verify Anagrams")][mission].

Анаграмма - это игра со словами, когда в результате перестановки букв слова или фразы получаем другое слово или фразу. Два слова являются анаграммами, если мы возможно получить одно из другого переставляя
буквы местами. Даны два слова или фразы и ваша задача проверить являются ли они анаграммами.

## Считаем буквы

Итак, нам нужно сравнить две фразы. Для начала нам нужно их "обработать":
выбрать только буквы и перевести их в нижний регистр.
Также как на этом шаге мы можем преобразовать строку в массив.
Вынесем эту процедуру в отдельную функцию.
```
def sanitize(text):
    return [ch.lower() for ch in text if ch.isalpha()]
```

Или если вы бережете память и предпочитаете генераторы:

```
def sanitize(text):
    yield from (ch.lower() for ch in text.lower() if ch.isalpha())
```

Или любите функциональный стиль программирования:

```
sanitize = lambda t: map(str.lower, filter(str.isalpha, text))
```

Далее нам нужно сосчитать каждую букву в тексте и если количественные характеристики
проверяемых слов/фраз совпадают, то они анаграммы.
Предположим, что мы используем только английские буквы и тогда можем использовать массив
из 26 элементов для ведения счета.
```
def count_letters(text):
    counter = [0] * 26
    for ch in text:
        counter[ord(ch) - ord("a")] += 1
    return counter
```

Честно говоря, это выглядит, как код написанный на С, никак не Python.
Да и привязаны жестко к английскому алфавиту.
Давайте заменим список на словарь (dictionary).

```
def count_letters(text):
    counter = {}
    for ch in text:
        counter[ch] = counter.get(ch, 0) + 1
    return counter
```

Уже лучше, но известный слоган Python гласит - "Батарейки прилагаются".
И тип данных [Counter](https://docs.python.org/2/library/collections.html#collections.Counter)
дает возможность просто подсчитать буквы в тексте.

```
from collections import Counter

def count_letters(text):
    return Counter(text)
```

Думаю вы и сами видите, что наша отдельная функция "count_letters" уже не так уж и нужна и
итоговое решение можно записать:

```
from collections import Counter

def sanitize(text):
    yield from (ch.lower() for ch in text.lower() if ch.isalpha())

def verify_anagrams(first, second):
    return Counter(sanitize(first)) == Counter(sanitize(second))
```

## Сортируем все подряд

Когда я решал первый раз эту задачу, я не использовал счетчики.
Вместо этого я преобразовывал текст в этакий универсальный вид для перестановок.
Конечно я говорю об упорядоченном виде. Если мы отсортируем строки и сравним их, то
это по сути тоже самое что считать элементы массива. И так как в нашей задаче
текст содержит только буквы и пробелы, то можно использовать один трюк:

```
def verify_anagrams(first, second):
    return "".join(sorted(first.lower())).strip() == "".join(sorted(second.lower())).strip()
```

Как легко заметить, мы одним движением руки можем преобразовать эту функцию в однострочечник (забавы ради):

```
verify_anagrams=lambda f,s,p=lambda x: "".join(sorted(x.lower())).strip():p(f)==p(s)
```

Вот такая вот история об анаграммах. Если вы хотите рассказать о других методах решения данной задачи,
то пишите и делитесь своими мыслями в комментариях.

![CheckiO_Logo](http://upload.wikimedia.org/wikipedia/commons/4/41/CheckiO_Company_Logo.png)

[mission]: http://www.checkio.org/mission/verify-anagrams/share/80a6c1510bf892c6b3789caa9e4f3805/
