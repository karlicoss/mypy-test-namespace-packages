from .common import foo, bar
from .module import baz, qux
kkk: str = bar(789) + qux(444)  # deliberate error to make sure mypy checks this file

# ^^^ note:
# if you run "MYPYPATH=pkg1:pkg2 mypy -p aaa.test      --html-report ."
#   if you use relative import for module (from .module ...)
#     - test.py is fully covered in coverage report
#     - common.py:1  -- shows error due to type mismatch foo: str = 123
#     - module.py:1  -- shows error due to type mismatch baz: str = 123
#     - test.py:3    -- shows error due to type mismatch kkk: str = bar(789) + qux(444)
#   if you use absolute import for module (from aaa.module ...)
#     exactly same as above
#   so basically in both cases works properly as expected
#
# however:
# if you run "MYPYPATH=pkg1:pkg2 mypy pkg1/aaa/test.py --html-report ."
#   if you use relative import for module (from .module ...)
#     - test.py is NOT covered in coverage report at all
#     - lines 1 and 2 show 'Skipping analyzing ... : module is installed, but missing library stubs or py.typed marker' error
#     - line 3 doesn't show as a type error (guess cause it assumes Any type?)
#   if you use absolute import for module (from aaa.module ...)
#     - test.py is partially covered (only line 2) in coverage report
#     - module.py:1 -- shows error due to type mismatch baz: str = 123
#     - line 1 shows 'Skipping analyzing ... : module is installed, but missing library stubs or py.typed marker' error
#   if you in addition make aaa.common import absolute (from aaa.common ...)

# so overall I'm convined it's just safer to always use mypy -p
# unless we completely give up on relative imports, but this hardly makes sense?
