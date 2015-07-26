README
======
tri-state-area is a simple changelog analysis tool designed for to analyze
changelogs for my software development & evolution (checkmate theists)
assignment. It works very simple with an interactive UI, using keywords
to categorize the change made in the changelog. It can however be used for
many other purposes.

Usage 
=====
```
usage: main.py [-h] -f FILE -o OUTPUT -i IMPLICATION -r RESTRAIN [-v]

Changelog analysis tool.

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Changelog file
  -o OUTPUT, --output OUTPUT
                        Output file
  -i IMPLICATION, --implication IMPLICATION
                        Implication table file
  -r RESTRAIN, --restrain RESTRAIN
                        Changelog identification character
  -v, --verbose         Verbose logging
```

Where restrains are required to identify the lines denoting change in a changelog file, such as a `*` denoting a list of changes.
Example:
```
Version 6.9
This release makes no sense!
* Core | Deleted / directory on UNIX environments
* UI | Makes it look like one of your French maids
* Extra | Please the English for trying to satisfy the French
```

Formats 
=======
File: `changelog`

Implication File:
```
keyword0 category0
keyword1 category1
keyword2 category1
...
```
