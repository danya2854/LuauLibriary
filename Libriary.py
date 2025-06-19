import math
from time import sleep as wait
from time import time_ns
from time import asctime
from requests import get
tonumber = float
tostring = str
string = str
pairs = range
typeof = type
true = True
false = False
class string():
    def len(text):
        """Returns the length of a string."""
        return len(text)
    #len = len
class task():
    def wait(seconds):
        """Yields the current thread without throttling."""
        return wait(seconds)
class os():
    def time():
        """Returns how many seconds have passed since the Unix epoch (1 January 1970, 00:00:00), under current UTC time."""
        return time_ns()
    def clock():
        """Returns elapsed time in seconds since an arbitrary baseline with sub-microsecond precision."""
        return asctime()
madeby = "Danechka"
class http():
    GetAsync = get
def lower(text):
    """Lower text"""
    return text.lower()
def upper(text):
    """Upper text"""
    return text.upper()
def warn(text):
    """Behaves similarly to print, except with more distinct formatting (yellow); intended for messages which describe potential problems."""
    print("\033[93m[Warn] "+ text)
def error(text):
    """Halts thread execution and throws an error."""
    print("\033[91m[Error] "+ text)
