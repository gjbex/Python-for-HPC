#include <iostream>
#include <random>
#include <tuple>
#include "automaton_runner.h"

Automaton init_automaton(const size_t nr_cells, const size_t seed) {
    Automaton automaton(nr_cells);
    std::mt19937_64 engine(seed);
    std::uniform_int_distribution<uint8_t> distr(0, 1);
    for (size_t cell_nr = 0; cell_nr < automaton.size(); ++cell_nr) {
        automaton[cell_nr] = distr(engine);
    }
    return automaton;
}

bool print_automaton(const Automaton& automaton) {
    for (const auto& value: automaton) {
        if (value == 0) {
            std::cout << ' ';
        } else {
            std::cout << 'X';
        }
    }
    std::cout << '\n';
    return true;
}

bool do_nothing([[maybe_unused]] const Automaton& automaton) {
    return true;
}

auto get_options(int argc, char *argv[]) {
    size_t nr_cells {10};
    uint8_t rule_nr {47};
    size_t nr_generations {20};
    size_t seed {1234};
    GenerationHandler handler {print_automaton};
    int i {1};
    while (i < argc) {
        std::string opt {argv[i]};
        if (opt == "--nr_cells") {
            nr_cells = std::stoul(argv[i + 1]);
        } else if (opt == "--rule_nr") {
            rule_nr = static_cast<uint8_t>(std::stoi(argv[i + 1]));
        } else if (opt == "--nr_generations") {
            nr_generations = std::stoul(argv[i + 1]);
        } else if (opt == "--seed") {
            seed = std::stoul(argv[i + 1]);
        } else if (opt == "--handler") {
            std::string handler_str {argv[i + 1]};
            if (handler_str == "nothing") {
                handler = do_nothing;
            } else if (handler_str == "visualize") {
                handler = print_automaton;
            } else {
                std::cerr << "# error: unknown handler type " << handler_str << "\n";
                std::exit(2);
            }
        } else {
            std::cerr << "# error: unexpected argument " << opt << "\n";
            std::exit(1);
        }
        i += 2;
    }
    return std::make_tuple(nr_cells, rule_nr, nr_generations, handler, seed);
}

int main(int argc, char *argv[]) {
    auto [nr_cells, rule_nr, nr_generations, handler, seed] = get_options(argc, argv);
    Automaton automaton = init_automaton(nr_cells, seed);
    AutomatonRunner runner(rule_nr);
    runner.evolve(automaton, nr_generations, handler);
    return 0;
}
