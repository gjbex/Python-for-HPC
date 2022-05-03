#!/usr/bin/env python
# coding: utf-8

# # Requirements

import argparse
import random
import sys

# # Implementation

# First we define a class to evolve the cellular autotomaton.  A runner is created for a specific rule, specified by a number between 0 and 255.  For instance, rule 47 would translate to:
# * $000 \mapsto 1$
# * $001 \mapsto 1$
# * $010 \mapsto 1$
# * $011 \mapsto 1$
# * $100 \mapsto 0$
# * $101 \mapsto 1$
# * $110 \mapsto 0$
# * $111 \mapsto 0$

class AutomatonRunner:
    
    def __init__(self, rule_nr):
        self._compute_rules(rule_nr)
        
    def _compute_rules(self, rule_nr):
        self._rules = []
        for _ in range(8):
            self._rules.append(rule_nr % 2)
            rule_nr //= 2
    
    def _apply_rule(self, environment):
        env_nr = 4*environment[0] + 2*environment[1] + environment[2]
        return self._rules[env_nr]
    
    def _make_environment(self, automaton, i):
        if 0 < i < len(automaton) - 1:
            return automaton[i - 1:i + 2]
        elif i == 0:
            return [automaton[-1]] + automaton[:2]
        elif i == len(automaton) - 1:
            return automaton[i - 1:] + [automaton[0]]
        
    def next_generation(self, automaton):
        ng_automaton = []
        for i in range(len(automaton)):
            environment = self._make_environment(automaton, i)
            ng_automaton.append(self._apply_rule(environment))
        return ng_automaton
                                
    def evolve(self, automaton, nr_generations):
        generations = [automaton]
        for _ in range(nr_generations):
            generations.append(self.next_generation(generations[-1]))
        return generations
    
    def __str__(self):
        auto_str = ''
        for i, result in enumerate(self._rules):
            auto_str += f'{i//4 % 2}{i//2 % 2}{i % 2} -> {result}\n'
        return auto_str


def automaton2str(automaton):
    return ''.join(str(c) for c in automaton).replace('0', ' ').replace('1', 'X')


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(description='run cellular automaton')
    arg_parser.add_argument('--nr_cells', type=int, default=10,
                            help='number of cells in automaton')
    arg_parser.add_argument('--nr_steps', type=int, default=50,
                            help='number of evolution steps')
    arg_parser.add_argument('--rule_nr', type=int, default=129,
                            help='number between 0 and 255 that defines the rul')
    arg_parser.add_argument('--seed', type=int, help='random number generator seed')
    arg_parser.add_argument('--verbose', action='store_true',
                            help='verbose output for debugging')
    options = arg_parser.parse_args()
    if options.seed:
        random.seed(options.seed)
    runner = AutomatonRunner(options.rule_nr)
    if options.verbose:
        print(runner, file=sys.stderr)
    automaton = random.choices((0, 1), k=options.nr_cells)
    if options.verbose:
        print(automaton2str(automaton), file=sys.stderr)
    generations = runner.evolve(automaton, options.nr_steps)
    for generation in generations:
        print(automaton2str(generation))
