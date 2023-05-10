#!/usr/bin/env bash
# Run by CI GithubAction to test examples, for those that provide tests.

cd "$(dirname "$(readlink -f "$0")")"

for example_test in */test.sh ; do
  echo "Running $example_test"
  example_dir="$(dirname "$example_test")"
  pushd . > /dev/null
  cd "$example_dir"

  if [ -f "requirements.txt" ] ; then
    # Yes, this means dependencies from different examples will mash on top of each other.
    # Solve it later, if it becomes a problem.
    echo "  Installing dependencies"
    pip install -r "requirements.txt"
  fi

  ./test.sh

  if [ $? -eq 0 ]; then
    echo "  $example_test succeeded!"
  else
    tests_failed=yes
    echo "  $example_test exited non-zero and may have errored. Please investigate."
  fi

  popd > /dev/null
done

if [ "$tests_failed" != "" ] ; then
  exit 1
fi
