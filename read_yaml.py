import yaml

with open("learn.yml","r") as file:
    content = yaml.safe_load(file)
    print(content)