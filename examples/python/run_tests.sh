#!/usr/bin/env bash
# Run by CI GithubAction to test examples, for those that provide tests.

cd "$(dirname "$(readlink -f "$0")")"

for example_test in */test.py ; do
  echo "> Running $example_test"
  example_dir="$(dirname "$example_test")"
  pushd . > /dev/null
  cd "$example_dir"

  if [ -f "requirements.txt" ] ; then
    # Yes, this means dependencies from different examples will mash on top of each other.
    # Solve it later, if it becomes a problem.
    echo ">> Installing dependencies"
    pip install -r "requirements.txt"
  fi

  python ./test.py

  if [ $? -eq 0 ]; then
    echo ">> $example_test succeeded!"
  else
    echo ">> $example_test exited non-zero and may have errored."
    tests_failed="$tests_failed"$'\n'"• $example_test"
  fi

  popd > /dev/null
done

if [ "$tests_failed" != "" ] ; then
  echo "These test scripts failed: $tests_failed"
  exit 1
fi
