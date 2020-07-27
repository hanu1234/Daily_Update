import pexpect
import sys

# Create the child process
child = pexpect.spawn("telnet 10.234.106.231  7002")

# expect(pattern, timeout=-1, searchwindowsize=-1, async_=False, **kw)
# expect will seeks through the stream until a pattern matched

# It will return the matched pattern indexing
try:
    spawn_out = child.expect(['login:', 'password:', 'yes/no', '#'], )
    if spawn_out == 0:
        # do something
        pass
    if spawn_out == 1:
        # do something
        pass
except pexpect.EOF:
    # do_some_other_thing()
    pass
except pexpect.TIMEOUT:
    # do_something_completely_different()
    pass


child.send("ls -ltrh")
'''Sends string ``s`` to the child process, returning the number of
        bytes written. If a logfile is specified, a copy is written to that
        log.
'''

child.sendline("ls -ltrh")
'''
Wraps send(), sending string ``s`` to child process, with
 ``os.linesep`` automatically appended.
'''

child.expect('#')
child.sendline('ps -a')
child.expect('#')


child.read()
child.readlines()
child.read_nonblocking()


# Example to log to stdout
child = pexpect.spawn('some_command', encoding='utf-8')
child.logfile = sys.stdout


# Reading the output
child.sendline('ls')
child.expect('#')
child.read_nonblocking(size=5000, timeout=30)






