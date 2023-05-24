Python examples should assume python 3.10 and that `pip install -r requirements.txt` 
is enough to get all the dependencies for that example. Environment management tools 
like Docker, conda, pyenv, virtualenv, ... should not litter example code.

Besides that, only a few other patterns are recommended: 
* Python examples should include a README.md describing what the example does
and which SemanticScholar services are involved.
* Optionally, python examples may include a `test.py` script. If it exists, it will run
as part of PRs and on a schedule via GitHub actions. The hope is this will help keep the 
examples functional over time.
