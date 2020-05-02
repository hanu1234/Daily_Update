import re
msg = "There were no PIN authentication events between 2020-04-23 04:34 and 2020-04-24 04:34"

pattern = re.compile(r'PIN authentication events between (\d+-\d+-\d+\W\d+:\d+) and (\d+-\d+-\d+\W\d+:\d+)')

events = re.search(pattern, msg)
print(events.group())


