**what is Logger**
- A logger is like an entity you can create and configure to log different type and format of messages.
- You can configure a logger that prints to the console and another logger that sends the logs to a file, has a different logging level and is specific to a given module. 

**5 Levels of logging**
- DEBUG: Detailed information, for diagnosing problems. Value=10.
- INFO: Confirm things are working as expected. Value=20.
- WARNING: Something unexpected happened, or indicative of some problem. But the software is still working as expected. Value=30.
- ERROR: More serious problem, the software is not able to perform some function. Value=40
- CRITICAL: A serious error, the program itself may be unable to continue running. Value=50

- if you set the log level=logging.WARNING that means only message from logging.warning() and higher level will get logged
