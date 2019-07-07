"""The most important part, Simple Chat depends on the more advanced util for its
simplistic mode."""

import util

#The code

class SimpleChat:
    def __init__(self):
        self.chat = util.Chat()
    def addResponse(self, one, two):
        self.chat.addResponse(one,
[ ["True", globals(), two, "" ] ])
    def respond(self, thing):
        return self.chat.respond(thing)
    def converse(self):
        return self.chat.converse()
