import sys

import get_papers

# For occasionally verifying this script, error if we don't find enough records.
if get_papers.count < 580:
    print(f'Too many records missing. S2, please investigate.')
    sys.exit(1)
