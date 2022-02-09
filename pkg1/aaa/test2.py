foo: str = 123 # deliberate error to make sure mypy checks this file

def bar(xxx: int) -> int:
    return xxx
