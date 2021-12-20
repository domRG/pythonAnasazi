import model
import household
import json

with open('props.json', 'r') as file:
    props = json.load(file)
    anasazi_model = model.AnasaziModel(props, seed=0)
    anasazi_model.step()
