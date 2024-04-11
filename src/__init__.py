

class Calculator:
    def add(*arg: float) -> float: # type: ignore
        return sum(arg)