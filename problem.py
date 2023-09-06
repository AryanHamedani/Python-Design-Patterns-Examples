import sys
import syslog

# The initial class.


class Logger(object):
    def __init__(self, file):
        self.file = file

    def log(self, message):
        self.file.write(message + "\n")
        self.file.flush()


# Two more classes, that send messages elsewhere.


class SocketLogger(Logger):
    def __init__(self, sock):
        self.sock = sock

    def log(self, message):
        self.sock.sendall((message + "\n").encode("ascii"))


class SyslogLogger(Logger):
    def __init__(self, priority):
        self.priority = priority

    def log(self, message):
        syslog.syslog(self.priority, message)


"""
The problem arises when this first axis of design is joined by another.
Let’s imagine that log messages now need to be filtered — 
some users only want to see messages with the word “Error” in them,
and a developer responds with a new subclass of Logger:
"""
# New design direction: filtering messages.

class FilteredLogger(Logger):
    def __init__(self, pattern, file):
        self.pattern = pattern
        super().__init__(file)

    def log(self, message):
        if self.pattern in message:
            super().log(message)

# It works.

f = FilteredLogger('Error', sys.stdout)
f.log('Ignored: this is not important')
f.log('Error: but you want to see this')

"""
The trap has now been laid,
and will be sprung the moment the application needs to filter messages
but write them to a socket instead of a file.
None of the existing classes covers that case.
If the developer plows on ahead with subclassing and creates a FilteredSocketLogger
that combines the features of both classes, then the subclass explosion is underway.
Maybe the programmer will get lucky and no further combinations will be needed.
But in the general case the application will wind up with 3×2=6 classes:
Logger            FilteredLogger
SocketLogger      FilteredSocketLogger
SyslogLogger      FilteredSyslogLogger

The total number of classes will increase geometrically if m and n both continue to grow.
This is the “proliferation of classes” and “explosion of subclasses”
that the Gang of Four want to avoid.

The solution is to recognize that a class responsible
for both filtering messages and logging messages is too complicated.
In modern Object Oriented practice,
it would be accused of violating the “Single Responsibility Principle.”

But how can we distribute the two features of message,
filtering and message output across different classes?
"""