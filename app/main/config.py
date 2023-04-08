import os
import json

basedir = os.path.abspath(
    os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

user_config_filepath = os.path.join(
    basedir, "configs", "user_configs.json"
)

with open(user_config_filepath) as f:
    user_config = json.load(f)

cur_profile = os.environ["PROFILE"] if "PROFILE" in os.environ else user_config["profile"]
print("Using profile", cur_profile)


class Config:

    @staticmethod
    def get_application_version():
        return user_config["version"]

    def __init__(self) -> None:
        pass
