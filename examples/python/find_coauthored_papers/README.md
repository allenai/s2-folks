Given two author names, this script finds coauthored papers.
In the case there are multiple matches for either author's name,
we print a description of each match. The user should figure out which
author they actually want, and then re-run with a specific author ID.

S2 APIs involved:
* [/graph/v1/author/search](https://api.semanticscholar.org/api-docs/graph#tag/Author-Data/operation/get_graph_get_author_search)
* [/graph/v1/author/{author_id}](https://api.semanticscholar.org/api-docs/graph#tag/Author-Data/operation/get_graph_get_author)
* [/graph/v1/author/{author_id}/papers](https://api.semanticscholar.org/api-docs/graph#tag/Author-Data/operation/get_graph_get_author_papers)

Example finding papers coauthored between [Oren Etzioni] and [Dan Weld].

    $ python find_papers.py "o etzioni" "dan s weld"
    Multiple authors matched "o etzioni".
    {'authorId': '1741101', 'url': 'https://www.semanticscholar.org/author/1741101', 'name': 'Oren Etzioni'}
    {'authorId': '70483292', 'url': 'https://www.semanticscholar.org/author/70483292', 'name': 'O. Etzioni'}
    Re-run with a specific ID.

Because "o etzioni" matches two authors, the script prints out links 
to the author pages on semanticscholar.org. We re-run the script with 
the specific ID that we want.

    $ python find_papers.py 1741101 "dan s weld"
    Left author: Oren Etzioni https://www.semanticscholar.org/author/1741101
    Right author: Daniel S. Weld https://www.semanticscholar.org/author/1780531
    Found 40 coauthored papers
    2023 The Semantic Scholar Open Data Platform https://www.semanticscholar.org/paper/cb92a7f9d9dbcf9145e32fdfa0e70e2a6b828eb1
    2022 A Computational Inflection for Scientific Discovery https://www.semanticscholar.org/paper/d1cf6bafac02ac65c7464bc7b168023584a688d7
    2022 Infrastructure for Rapid Open Knowledge Network Development https://www.semanticscholar.org/paper/d49cf805bcef60f206bca60d7315f6e52217b44f
    2020 CORD-19: The Covid-19 Open Research Dataset https://www.semanticscholar.org/paper/4a10dffca6dcce9c570cb75aa4d76522c34a2fd4
    2016 Toward Automatic Bootstrapping of Online Communities Using Decision-theoretic Optimization https://www.semanticscholar.org/paper/8cc2d899876c50305c12a2c3bd2373ce561c46d6
    2013 Open Information Extraction to KBP Relations in 3 Hours https://www.semanticscholar.org/paper/d43181fa9af5440360d4055e1ce7ddaaa6e82d77
    2013 Sound and E cient Closed-World Reasoning for Planning Technical Report 95-02-02 https://www.semanticscholar.org/paper/3db1c4f8d47840964153cbba93c60b7c07b56e75
    2010 Learning First-Order Horn Clauses from Web Text https://www.semanticscholar.org/paper/b71c8e582e8e56d839c962b923b0b79bada2a7f8
    2010 Machine Reading at the University of Washington https://www.semanticscholar.org/paper/380169dfdf019dd77f3316ab14fefab337113652
    ...


[Oren Etzioni]: https://www.semanticscholar.org/author/Oren-Etzioni/1741101
[Dan Weld]: https://www.semanticscholar.org/author/Daniel-S.-Weld/1780531
