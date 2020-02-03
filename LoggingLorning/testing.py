import logging
import logging.handlers

a = logging.getLogger('myapp')
a.setLevel(logging.DEBUG)   # set root's level

h = logging.handlers.RotatingFileHandler('foo.log')
h.setLevel(logging.DEBUG)
a.addHandler(h)

h2 = logging.handlers.RotatingFileHandler('foo2.log')
h2.setLevel(logging.WARNING)
a.addHandler(h2)

print(a.getEffectiveLevel())
a.debug('foo message')
a.warning('warning message')
