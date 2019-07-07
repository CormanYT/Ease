import re

string = re.compile("He said '(.*)'")
inputs=[
"He said 'fat'",
"He said 'fart'",
"He said 'screw you'",
"He said 'you bananas!'"
]
for item in inputs:
    print("New Item.")
    for match in string.findall(item):
        print(match)
        print()
    print()
