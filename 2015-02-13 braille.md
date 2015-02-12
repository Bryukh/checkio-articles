# Braille Translator Overview

Hi, CiO friends.

Today I would like delve into the [Braille system][wikipedia_link].
Braille is a tactile writing system used by the blind and the visually impaired.
It is traditionally written with embossed paper.

In the ["English to Braille Translator"][mission_link] Checkio mission, you are challenged to write a translator
to convert a chunk of english text into Braille. For this we will use the 6-dot based Braille alphabet.

<img src="https://checkio.s3.amazonaws.com/task/media/7c2d8e23738a453fa7e1cf752c95fb04/alphabet.svg"
    width="300px", style="display: block; margin-left: auto;margin-right: auto;">
    
Your script which you will write for this mission would be useful when parsing braille text and formatting it for printing,
or it could be used to translate existing text into braille for others. Let's take a look at how some CiO players did that.

First off, we cannot skip [veky][veky_profile] with his [Visual][veky_visual] solution. 
Try to comprehend this code without assistance before you even look at the comments where you'll find veky explains his magic.
Just as a hint: "The secret is R. :-)".

```
R = " a,b*k*l*cif*msp*e-h*o!r*djg*ntq$***_u?v*****x****.**z******#yw*"
```

Honestly, it really does look like magic, but when you get into it, you like this kind of thing.

If the previous solution was too magical for you, then take a look at [vinc's][vinc_profile] [solution][vinc_translator].
Vinc uses some predefined data and then weaves the results in.
This solution can be a simpler method for some of our python newbies.

And if you like function decomposition, camelCase and formatted comments, 
then [jcg's][jcg_profile] solution, ["First",][jcg_first] will be right up your alley.

You can learn how to write code like you'd see in a science article in [Blastus'][Blastus_profile] ["First" solution][Blastus_first].
All the fragments are placed on shelves and inside are many, many 'for' loops.

I think these solutions'll give you some nice weekend reading. Don't forget to upvote interesting solutions, the authors will be pleased!

Feel free ask any questions in the comments if you find something is not clear in a solution, or ask the advisers if you have problems with some mission. The CheckiO community is always friendly and will gladly help you.


<!--------------------------------------------------------------------------------------------------------------------->


<!--General Links-->

[mission_link]: http://www.checkio.org/mission/braille-translator/share/e1038fe9b92f4365bbadfa3ac12a883f/ "Mission Share Link"
[wikipedia_link]: https://en.wikipedia.org/wiki/Braille
[image_link]: https://checkio.s3.amazonaws.com/task/media/7c2d8e23738a453fa7e1cf752c95fb04/alphabet.svg

[veky_visual]: http://www.checkio.org/mission/braille-translator/publications/veky/python-3/visual/share/1aec185754570ac9e6ff23d04f4f9910/
[vinc_translator]: http://www.checkio.org/mission/braille-translator/publications/vinc/python-3/english-to-braille-translator/share/1d35511df29594b5165324a796c754d8/
[jcg_first]: http://www.checkio.org/mission/braille-translator/publications/jcg/python-3/first/share/f8cc0d47e2c6e45bfaaa296e7a0cd7db/
[Blastus_first]: http://www.checkio.org/mission/braille-translator/publications/Blastus/python-3/first/share/550f7d6007f34b67a19139cf5ca75cbb/


[veky_profile]: http://www.checkio.org/user/veky/
[vinc_profile]: http://www.checkio.org/user/vinc/
[jcg_profile]: http://www.checkio.org/user/jcg/
[Blastus_profile]: http://www.checkio.org/user/Blastus/
