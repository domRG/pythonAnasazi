import model
import household
import json

with open('props.json', 'r') as file:
    props = json.load(file)
    empty_model = model.AnasaziModel(props["household"]["start_count"], seed=0)
    empty_model.step()
