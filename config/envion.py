import os
import configparser

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ENV = os.environ.get("ENV", "test")
conf_dir = os.path.join(base_dir, "config", "conf", f"{ENV}.conf")

print(conf_dir)

env_config = {}


def conf_parse():
    config = configparser.ConfigParser()
    config.read(conf_dir)
    sections = config.sections()
    for section in sections:
        env_config.update(
            {item[0]: item[1] for item in config.items(section)}
        )


conf_parse()
