# Shows how to download and inspect data in the sample datasets
# which are much smaller than the full datasets.
import json
import subprocess

subprocess.check_call("bash get_sample_files.sh", shell=True)

papers = [json.loads(l) for l in open("samples/papers/papers-sample.jsonl", "r").readlines()]
citations = [json.loads(l) for l in open("samples/citations/citations-sample.jsonl", "r").readlines()]
embeddings = [json.loads(l) for l in open("samples/embeddings-specter_v2/embeddings-specter_v2-sample.jsonl", "r").readlines()]

# S2ORC
docs = [json.loads(l) for l in open("samples/s2orc/s2orc-sample.jsonl", "r").readlines()]
text = docs[0]['content']['text']
annotations = {k: json.loads(v) for k, v in docs[0]['content']['annotations'].items() if v}

for a in annotations['paragraph'][:10]:
    print(a)
for a in annotations['bibref'][:10]:
    print(a)
for a in annotations['bibentry'][:10]:
    print(a)

def text_of(type):
    return [text[a['start']:a['end']] for a in annotations.get(type, '')]

print(text_of('abstract'))
print('\n\n'.join(text_of('paragraph')[:3]))
print('\n'.join(text_of('bibref')[:10]))
