# Minimal script to periodically run this example to see if it still works.
import subprocess

print('test: no matches for left author')
exit_code, output = subprocess.getstatusoutput('python find_papers.py "bogus author with no matches" "dan s weld"')
print(output)
assert exit_code != 0
print()

print('test: o etzioni is ambiguous, script exits early')
exit_code, output = subprocess.getstatusoutput('python find_papers.py "e etzioni" "dan s weld"')
print(output)
assert exit_code != 0
assert 'Multiple authors matched' in output
print()

print('test: o etzioni disambiguated by providing specific id')
exit_code, output = subprocess.getstatusoutput('python find_papers.py 1741101 "dan s weld"')
print(output)
assert exit_code == 0
assert '2023 The Semantic Scholar Open Data Platform' in output
print()
