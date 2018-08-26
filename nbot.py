# -*- coding: UTF-8 -*-
import os

os.system("clear")
G = '\033[32;1m'
R = '\033[31;1m'

print( R + "Nasir AI AutoReply Bot")
print( G + "Follow on Instagram @nasir.xoz")
print( G + "Contact on Facebook: fb.com/nasir.xo")


user = input( R + "Email:")
p = input("Password:")

from fbchat import log, Client


# Subclass fbchat.Client and override required methods
class EchoBot(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(thread_id, message_object.uid)
        self.markAsRead(thread_id)

        log.info("{} from {} in {}".format(message_object, thread_id, thread_type.name))

        # If you're not the author, echo
        if author_id != self.uid:
            self.send(message_object, thread_id=thread_id, thread_type=thread_type)

client = EchoBot( user , p )
client.listen()
