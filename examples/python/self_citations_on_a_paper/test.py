import subprocess

output = subprocess.getoutput('python main.py CorpusID:3658586')
print(output)
# This author has built on their own work frequently so should be a stable test.
assert 'T. Wenzl in citing paper' in output
assert 'T. Wenzl in referenced paper' in output
