# Minimal script to periodically run this example to see if it still works.
import re
import subprocess

# The script takes two inputs, first a keyword search, then a paper selection.
output = subprocess.getoutput('''
python find_papers.py << EOL
author name disambiguation in papers
5
EOL''')
print(output)

# We are just spot checking for a few things in a successful output sequence.
assert re.search('Found \\d+ results', output)
assert re.search('recommendations based on', output)
