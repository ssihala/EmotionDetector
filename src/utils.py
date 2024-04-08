
"""
Progress bar for displaying various process progress
"""
class ProgressBar:

    def __init__(self, length: int, message: str):
        self.length = length
        self.bar = '-'*length
        self.message = message
        self.frac = 0

    def update(self, frac: float):
        self.frac = 1 if frac > 1 else frac
        whole = int(self.frac * self.length)
        self.bar = '#'*whole + '-'*(self.length - whole)

    def display(self, suffix:str = ''):
        delim = '' if self.frac != 1.0 else '\n'
        print(f'\r{self.message}[{self.bar}] {suffix}', end=delim)

    def update_display(self, frac: float, suffix:str=''):
        self.update(frac)
        self.display(suffix)


