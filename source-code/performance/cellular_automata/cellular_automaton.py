#!/usr/bin/env python

import argparse
import functools
import random


class AutomatonRunner:

    def __init__(self, rule_nr):
        self._rules = []
        for _ in range(8):
            self._rules.append(rule_nr % 2)
            rule_nr //= 2

    def random_automaton(self, nr_cells, seed=None):
        if seed is not None:
            random.seed(seed)
        return random.choices((0, 1), k=nr_cells)

    def _next_generation(self, automaton):
        idx = (automaton[-1] << 2) | (automaton[0] << 1) | automaton[1]
        ng_automaton = [self._rules[idx]]
        for i in range(1, len(automaton) - 1):
            idx = (automaton[i - 1] << 2) | (automaton[i] << 1) | automaton[i + 1]
            ng_automaton.append(self._rules[idx])
        idx = (automaton[-2] << 2) | (automaton[-1] << 1) | automaton[0]
        ng_automaton.append(self._rules[idx])
        return ng_automaton

    def evolve(self, automaton, nr_generations, handler):
        if not handler(automaton): return
        for _ in range(nr_generations):
            automaton = self._next_generation(automaton)
            if not handler(automaton): return

    def evolve_random(self, nr_cells, nr_generations, handler, seed=None):
        automaton = self.random_automaton(nr_cells, seed)
        self.evolve(automaton, nr_generations, handler)

    def __str__(self):
        auto_str = ''
        for i, result in enumerate(self._rules):
            auto_str += f'{i//4 % 2}{i//2 % 2}{i % 2} -> {result}\n'
        return auto_strgggg

def do_nothing_handler(automaton):
    return True

def print_automaton(zero_value, one_value, sep,  automaton):
    print(sep.join(one_value if cell else zero_value for cell in automaton))
    return True

def main():
    arg_parser = argparse.ArgumentParser(description='run cellular automata')
    arg_parser.add_argument('--nr_cells', type=int, default=10,
                            help='number of cells of the automaton')
    arg_parser.add_argument('--nr_generations', type=int, default=20,
                            help='number of generation to run the automaton for')
    arg_parser.add_argument('--rule_nr', type=int, default=47,
                            help='rule number between 0 and 255')
    arg_parser.add_argument('--seed', type=int, default=1234,
                            help='seed for the random number generator')
    arg_parser.add_argument('--handler', choices=['nothing', 'visualize', 'numeric'],
                            default='visualize', help='handler to run for each generation')
    options = arg_parser.parse_args()
    runner = AutomatonRunner(options.rule_nr)
    if options.handler == 'numeric':
        handler = functools.partial(print_automaton, '0', '1', ' ')
    elif options.handler == 'visualize':
        handler = functools.partial(print_automaton, ' ', 'X', '')
    else:
        handler = do_nothing_handler
    runner.evolve_random(options.nr_cells, options.nr_generations, handler, options.seed)

if __name__ == '__main__':
    main()

