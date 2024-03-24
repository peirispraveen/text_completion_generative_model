import random
from string import punctuation
from collections import defaultdict


class MarkovChain:
    def __init__(self):
        self.graph = defaultdict(list)

    def _tokenize(self, text):
        return (
            text.translate(str.maketrans("", "", punctuation + "1234567890"))
            .replace("\n", " ")
            .split(" ")
        )

    def train(self, text):
        tokens = self._tokenize(text)
        for i, token in enumerate(tokens):
            if len(tokens) - 1 == i:
                break
            self.graph[token].append(tokens[i + 1])

    def generate(self, prompt, length=10):

        current = self._tokenize(prompt)[-1]  # get the last token from the prompt
        # initialize the output
        output = prompt
        for i in range(length):

            options = self.graph.get(current, [])  # look up the options in the graph dictionary
            if not options:
                continue

            current = random.choice(options)  # use random.choice method to pick a current option

            output += f" {current}"  # add the random choice to the output string

        return output


text = """
Dear Slim, I wrote you, but you still ain't callin'
I left my cell, my pager and my home phone at the bottom
I sent two letters back in autumn, you must not've got 'em
There probably was a problem at the post office or somethin'
Sometimes I scribble addresses too sloppy when I jot 'em
But anyways, fuck it, what's been up, man? How's your daughter?
My girlfriend's pregnant too, I'm 'bout to be a father
If I have a daughter, guess what I'ma call her? I'ma name her Bonnie
I read about your Uncle Ronnie too, I'm sorry
I had a friend kill himself over some bitch who didn't want him
I know you probably hear this every day, but I'm your biggest fan
I even got the underground shit that you did with Skam
I got a room full of your posters and your pictures, man
I like the shit you did with Rawkus too, that shit was phat
Anyways, I hope you get this, man, hit me back
Just to chat, truly yours, your biggest fan, this is Stan

You might also like
Big Foot
Nicki Minaj
Big Foot (A Cappella)
Nicki Minaj
The Twelve Days of Christmas
Christmas Songs

My tea's gone cold, I'm wondering why I
Got out of bed at all
The morning rain clouds up my window
And I can't see at all
And even if I could, it'd all be grey
But your picture on my wall
It reminds me that it's not so bad, it's not so bad
Dear Slim, you still ain't called or wrote, I hope you have a chance
I ain't mad, I just think it's fucked up you don't answer fans
If you didn't want to talk to me outside your concert, you didn't have to
But you coulda signed an autograph for Matthew
That's my little brother, man, he's only six years old
We waited in the blisterin' cold for you, for four hours, and you just said, "no"
That's pretty shitty, man, you're like his fuckin' idol
He wants to be just like you, man, he likes you more than I do
I ain't that mad, though I just don't like bein' lied to
Remember when we met in Denver? You said if I'd write you, you would write back
See, I'm just like you in a way: I never knew my father neither
He used to always cheat on my mom and beat her
I can relate to what you're sayin' in your songs
So when I have a shitty day, I drift away and put 'em on
'Cause I don't really got shit else, so that shit helps when I'm depressed
I even got a tattoo with your name across the chest
Sometimes I even cut myself to see how much it bleeds
It's like adrenaline, the pain is such a sudden rush for me
See, everything you say is real, and I respect you 'cause you tell it
My girlfriend's jealous 'cause I talk about you 24/7
But she don't know you like I know you, Slim, no one does
She don't know what it was like for people like us growin' up
You gotta call me, man, I'll be the biggest fan you'll ever lose
Sincerely yours, Stan—P.S. We should be together too
"""


chain = MarkovChain()
chain.train(text)

sample = "I ain't"

result = chain.generate(sample)

print(result)
