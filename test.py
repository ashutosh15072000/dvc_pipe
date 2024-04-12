import yaml
import os

param_yaml_path = "params.yaml"
with open(param_yaml_path) as yaml_file:
    param_yaml = yaml.safe_load(yaml_file)

print(os.path.join(param_yaml['split']['dir'],param_yaml['split']['train_file']))