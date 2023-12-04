import math
import timeit

class Algorithm:

    def __init__(self, function, name=None, return_result=False):
        self._function = function
        self._name = name if name is not None else getattr(function, '__qualname__', None)
        self._return_result = return_result

    @property
    def name(self):
        return self._name

    def run(self, *args, **kvargs):
        result = self._function(*args, **kvargs)
        if self._return_result:
            return result

    def __str__(self):
        return self.name


class Timings:

    def __init__(self, algorithm_names, number, repeat):
        self._timings = {name: [] for name in algorithm_names}

    @property
    def names(self):
        return self._timings.keys()

    @property
    def number(self):
        return self._number

    @property
    def repeat(self):
        return self._repeat

    def add(self, algorithm_name, timing):
        self._timings[algorithm_name].append(timing)

    def __getitem__(self, algorithm_name):
        return self._timings[algorithm_name]

    def average(self, algorithm_name):
        return math.mean(self._timings[algorithm_name])

    def std(self, algorithm_name):
        return math.std(self._timings[algorithm_name])

    def ratio(self, algorithm_name):
        minimum = min(self.average(name) for name in self.names)
        return self.average(algorithm_name)/minimum

    def stats(self):
        return {name: {
                        'average': self.average(name),
                        'std': self.std(name),
                        'ratio': self.ratio(name),
                      } for name in self.names
                }

    def __str__(self):
        return '\n'.join(f'{name}: {self[name]}' for name in self.names)


class Timer:

    def __init__(self, algorithms, setups=None):
        if callable(algorithms):
            self._algorithms = (algorithms, )
        else:
            try:
                self._algorithms = tuple(algorithms)
            except:
                raise ValueError(f'argument algorithms is not a function or an iterable')
        self._algorithms = tuple(Algorithm(algorithm) for algorithm in self._algorithms)
        if setups is None:
            self._setups = (lambda: ([], {}), )*len(self._algorithms)
        elif callable(setups):
            self._setups = (setups, )*len(self._algorithms)
        else:
            try:
                self._setups = tuple(setups)
            except:
                raise ValueError('setups is not a function or an iterable')

    def time(self, number=1, repeat=1):
        timings = Timings((algorithm.name for algorithm in self._algorithms), number, repeat)
        for i, algorithm in enumerate(self._algorithms):
            for _ in range(repeat):
                args, kvargs = self._setups[i]()
                for _ in range(number):
                    timing = timeit.timeit(lambda: algorithm.run(*args, **kvargs), number=1)
                    self._timings.add(algorithm.name, timing)
