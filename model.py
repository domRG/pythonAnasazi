from mesa import Model
from mesa.time import RandomActivation
import household


class AnasaziModel(Model):
    """A model with some number of agents."""
    def __init__(self, props, seed=None):
        self.props = props
        self.agent_init_num = self.props["household"]["start_count"]
        self.schedule = RandomActivation(self)
        # Create agents
        for i in range(self.agent_init_num):
            new_agent = household.Household(i, self)
            self.schedule.add(new_agent)

    def step(self):
        '''Advance the model by one step.'''
        self.schedule.step()