from mesa import Model
from mesa.time import RandomActivation
import household


class AnasaziModel(Model):
    """A model with some number of agents."""
    def __init__(self, N, seed=None):
        self.num_agents = N
        self.schedule = RandomActivation(self)
        # Create agents
        for i in range(self.num_agents):
            new_agent = household.Household(i, self)
            self.schedule.add(new_agent)

    def step(self):
        '''Advance the model by one step.'''
        self.schedule.step()