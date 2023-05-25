# Minimal script to periodically run this example to see if it still works.
import subprocess

output = subprocess.getoutput('python simple.py -d papers 649def34f8be52c8b66281af98ae884c09aef38b')
assert "Downloaded '649def34f8be52c8b66281af98ae884c09aef38b' to 'papers/649def34f8be52c8b66281af98ae884c09aef38b.pdf'" in output

output = subprocess.getoutput('python parallel.py -d papers 649def34f8be52c8b66281af98ae884c09aef38b')
assert "Downloaded '649def34f8be52c8b66281af98ae884c09aef38b' to 'papers/649def34f8be52c8b66281af98ae884c09aef38b.pdf'" in output
