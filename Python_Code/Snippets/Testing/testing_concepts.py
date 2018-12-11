'''

- Unittest
module used for;
Unit tests | Integration tests | Acceptance tests

it is nice as it is Automated & repeatable

- TestCase:
Groups together related test functions.

- Fixtures:
code run before and/or after each test function
fixtures setup the environment

code exsample start :
set-up fixture

def test_line_count(self):
    "check that the line count is correct."
    self.assertEquel(
        analyze_text(self.filename)[0], 4)

tear-down/clean-up fixture


code exsample end:


- Assertions:
they are specific tests for conditions and behaviors, such as;
x.is_valid()
x == y
raise ValueError()

If an assertion fails, then a test fails!
Lowest level of test that can be performed.


'''

