from automata.fa.nfa import NFA
import graphviz

def regex_to_nfa(regex):
    nfa = NFA.from_regex(regex)
    return nfa

def nfa_to_graphviz(nfa):
    dot = graphviz.Digraph()
    for state in nfa.states:
        state_str = str(state)
        if state == nfa.initial_state:
            dot.node(state_str, shape='doublecircle', style='filled', color='lightgrey')
        elif state in nfa.final_states:
            dot.node(state_str, shape='doublecircle')
        else:
            dot.node(state_str, shape='circle')
    for from_state, transitions in nfa.transitions.items():
        for symbol, to_states in transitions.items():
            for to_state in to_states:
                from_state_str = str(from_state)  # Преобразуем состояния в строку
                to_state_str = str(to_state)
                dot.edge(from_state_str, to_state_str, label=symbol)
    return dot
def main():
    regex = input("Введите регулярное выражение: ")
    nfa = regex_to_nfa(regex)
    dot = nfa_to_graphviz(nfa)
    dot.render('nfa_graph', format='png', view=True)

if __name__ == "__main__":
    main()
