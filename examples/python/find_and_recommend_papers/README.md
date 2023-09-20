This interactive example searches for some candidate papers and 
then has the user select one on which to base other reading recommendations.

APIs involved
* [/graph/v1/paper/search](https://api.semanticscholar.org/api-docs/graph#tag/Paper-Data/operation/get_graph_get_paper_search)
* [/recommendations/v1/papers/forpaper/{paper_id}](https://api.semanticscholar.org/api-docs/recommendations#tag/Paper-Recommendations/operation/get_papers_for_paper)

Usage example

```
Find papers about what: author name disambiguation in papers
Found 87 results. Showing up to 10.
0  Framework for Author Name Disambiguation in Scientific Papers Using an Ontological Approach and Deep Learning https://www.semanticscholar.org/paper/85c385b8a01e3230cd56e618ce14336d8557132d
1  Whois? Deep Author Name Disambiguation using Bibliographic Data https://www.semanticscholar.org/paper/e8e0e046e9d25b90ce073837e48d64135bd09796
2  S2AND: A Benchmark and Evaluation System for Author Name Disambiguation https://www.semanticscholar.org/paper/4bb09aa0e00d104c6057d71f24ab876320286edb
3  Dual-Channel Heterogeneous Graph Network for Author Name Disambiguation https://www.semanticscholar.org/paper/1d68629e2e691d47ad42a1b17e1e0104df876f80
4  AuthCrowd: Author Name Disambiguation and Entity Matching using Crowdsourcing https://www.semanticscholar.org/paper/fe8651bc8a99507ece20618a57c74356f76de3a4
5  Deep Author Name Disambiguation using DBLP Data https://www.semanticscholar.org/paper/df97e51714d78ea606e8854dbfa2846766d98991
6  Author Name Disambiguation on Heterogeneous Information Network with Adversarial Representation Learning https://www.semanticscholar.org/paper/76b8d5f2ef97d71167aa78309918bf3f7d633c96
7  Author Name Disambiguation Based on Rule and Graph Model https://www.semanticscholar.org/paper/42b7b17624753a359d17024e02fc424161d2580c
8  Visual Analysis for Name Disambiguation of Academic Papers https://www.semanticscholar.org/paper/abf2b71554cbdb03cee49e4fce9e53a89b44e1b6
9  Research on Author Name Disambiguation Based on Fusion Features and Semantic Fingerprints https://www.semanticscholar.org/paper/c450c3f9bc041845bc24578d3e4377788d0cead0
Select a paper # to base recommendations on: 2
Up to 10 recommendations based on: S2AND: A Benchmark and Evaluation System for Author Name Disambiguation
0  ZELDA: A Comprehensive Benchmark for Supervised Entity Disambiguation https://www.semanticscholar.org/paper/3bde83fc4c70aa00c214209b0b70890b4610169c
1  A Gold Standard Dataset for the Reviewer Assignment Problem https://www.semanticscholar.org/paper/5ea8eedcb31859c5730dd1da3804e1be529ffabb
2  An Effective Approach for Informational and Lexical Bias Detection https://www.semanticscholar.org/paper/70d448804ea9533193914d4d3ed974ef1a551086
3  unarXive 2022: All arXiv Publications Pre-Processed for NLP, Including Structured Full-Text and Citation Network https://www.semanticscholar.org/paper/060ab95c38eebe71c28d9bab81de32b934a54f70
4  CitePrompt: Using Prompts to Identify Citation Intent in Scientific Papers https://www.semanticscholar.org/paper/68ee8a53f0b1ff146194980337dd6d533b17c59b
5  S2abEL: A Dataset for Entity Linking from Scientific Tables https://www.semanticscholar.org/paper/0bc975e61002ec29ac67d44d91d35cdbfc56982a
6  An analysis of one-to-one matching algorithms for entity resolution https://www.semanticscholar.org/paper/3fff46dfed75b687a4370b7b6d192b41e42585d9
7  BenCoref: A Multi-Domain Dataset of Nominal Phrases and Pronominal Reference Annotations https://www.semanticscholar.org/paper/e6a48e3a8e87bb65561656378e58a589e603526a
8  Information Redundancy and Biases in Public Document Information Extraction Benchmarks https://www.semanticscholar.org/paper/fa75fb586c46a30e742a0bd5748afaa875f30607
9  Automatic Evaluation of Attribution by Large Language Models https://www.semanticscholar.org/paper/2eb6868fdaf6a9bce1385ca2aabb20282c78a52f
```

Note that the keyword search provides a number of works generally related
to author name disambiguation. We choose the 2nd paper to feed as input
to the recommendation API, which re-orients our results to works involving 
NLP techniques applied to scientific literature.
