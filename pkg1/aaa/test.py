from .test2 import foo, bar
baz: str = bar(789)  # deliberate error to make sure mypy checks this file

# ^^^ note:
# if you run "mypy pkg1/aaa/test.py --html-report ."
#    - line 1 shows 'Skipping analyzing ".test2": module is installed, but missing library stubs or py.typed marker' error
#             shows as not covered in coverage report
#    - line 2 doesn't show as a type error (guess cause it assumes Any type?)
#             shows as not covered in coverage report ('Unimported' reason)
#
# however:
# if you run "MYPYPATH=pkg1 mypy -p aaa.test --html-report ."
#    - whole test.py is covered in coverage report
#    - test2.py:1 -- shows error due to type mismatch foo: str = 123
#    - test.py:2  -- shows error due to type mismatch baz: str = bar(789)
