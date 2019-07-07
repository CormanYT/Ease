import random
import time
import re
import os, sys, inspect

#Go to parent directory

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

#Import things from parent directory

import strings.pairs as pair

#Go back to current directory

sys.path.insert(0, currentdir)

def _list(this):
    yes = []
    for key, value in this.items():
        yes.append((key, value))
    return yes

class Chat:
    def __init__(self):
        self.pairs = []
    def addResponse(self, *args):
        """
        one:

        One is simply all of the input responses. It will generate an output response based on the input responses in the respond method.

        two:

        Two is the second argument. It requires a dictionary of evaluated expressions and responses. It works like:

        this = {"5 == 2": ["Hello"]}
        "True": ["Hey"]}

        If the evaluated expression is "true", it will give that random response out of the list immediately. Otherwise, there are conditions. The
        evaluated expressions need to be booleans, of course. There is also an addon expression.

        this = {"(this - 2) < 4)": "Yes, it does."
        "else": ["No, it doesn't."]
        }

        The "else" evaluated expression will choose a response of the list if no other evaluated expression is true.

        Three:

        Three is the executed expression, if it is "-", "None", or "", it will be ignored.

        It is executed from the exec() function and should not be put in by user input.
        
        """
        self.pairs.append([args])
    def _wildcards(self, final, regex):
        check = True
        numb = 0
        this = []
        while check == True:
            numb += 1
            try:
                this.append(regex.group(numb))
            except (AttributeError, IndexError):
                check = False
        for count in range(len(this)):
            final = final.replace("%" + str(count + 1), this[count])
        return final
    def _evwildcards(self, final, regex):
        check = True
        numb = 0
        this = []
        while check == True:
            numb += 1
            try:
                this.append(regex.group(numb))
            except (AttributeError, IndexError):
                check = False
        for count in range(len(this)):
            final = final.replace("%" + str(count + 1), '"' + this[count] + '"')
        return final
    def respond(self, thing):
        """
        The respond method works like this. With all the responses in the list, it checks each response list.

        Each response list contains mainly two things:
        - The input values | Like for greetings, "Hi" or "Hello"
        - The filter/output list
        Each filter/output list contains:
        - The evaluated string ("It generates a certain response based on evaluating this string to a object.")
        - The output responses for each evaluation

        Evaluations are optional, so to make them optional you put the evaluated expression of "True".

        If all other evaluations fail, "else" can be used for a response if other evaluations fail.
        """
        response = None
        final = [False]
        for item in self.pairs:
            sents = item[0][0]
            for sent in sents:
                regex = re.compile(sent.lower())
                match = regex.match(thing.lower())
                if match:
                    responsed = item[0][1]
                    for thinger in responsed:
                        if thinger[0] != "else":
                            thiner = self._evwildcards(thinger[0], match)
                            if eval(thiner, thinger[1]) == True:
                                try:
                                    exec(thinger[3])
                                except:
                                    ""
                                response = random.choice(thinger[2])
                                regexer = match
                        else:
                            try:
                                exec(thinger[3])
                            except:
                                ""
                            response = random.choice(thinger[2])
                            regexer = match
        if response != None:
            response = self._wildcards(response, regexer)
            return response
        return
                    
    def converse(self):
        """Simple conversation.
Not recommended to use, but is usuable."""

        
        print('Type "exit chat" to exit the chat.')
        time.sleep(0.15)
        while True:
            this = input(">")
            if this == "exit chat":
                print("Conversation: End.")
                break
            else:
                print(self.respond(this))
"""
Example Code:

this = Chat()
mood = 2
this.addResponse(["Hi", "Hello", "Hey"],
[ ["mood == 2", globals(), ["Hi!", "Greetings!"]],
["else", globals(), ["Oh... Hi!"]]
], "")
this.converse()

"""
