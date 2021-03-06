from mesa import Agent

class Household(Agent):
    """ An agent with fixed initial wealth."""
    def __init__(self, unique_id, model, age, death_age, init_storage=[0, 0]):
        super().__init__(unique_id, model)
        self.age = age
        self.death_age = death_age
        self.storage = init_storage

    def step(self):
        # The agent's step will go here.
        # For demonstration purposes we will print the agent's unique_id
        print(f"step on #{self.unique_id}")