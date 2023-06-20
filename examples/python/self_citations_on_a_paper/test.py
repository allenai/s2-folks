import re
import subprocess

output = subprocess.getoutput('python main.py CorpusID:3658586')
print(output)
# This author has built on their own work frequently so should be a stable test.
assert re.search('Vandenplas.*in citing paper', output)
assert re.search('Vandenplas.*in referenced paper', output)
