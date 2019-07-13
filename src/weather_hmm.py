'''weather prediction HMM'''
from pomegranate import HiddenMarkovModel, DiscreteDistribution, State

model = HiddenMarkovModel(name='weather')

sunny_emissions = DiscreteDistribution({'yes': 0.1, 'no': 0.9})
sunny_state = State(sunny_emissions, name='sunny')

rainy_emissions = DiscreteDistribution({'yes': 0.8, 'no': 0.2})
rainy_state = State(rainy_emissions, name='rainy')

model.add_states(sunny_state, rainy_state)

model.add_transition(model.start, sunny_state, 0.5)
model.add_transition(model.start, rainy_state, 0.5)

model.add_transition(sunny_state, rainy_state, 0.2)
model.add_transition(sunny_state, sunny_state, 0.8)

model.add_transition(rainy_state, rainy_state, 0.6)
model.add_transition(rainy_state, sunny_state, 0.4)

model.bake()

print(model.edge_count())
print(model.node_count())
