from config.config import config as app_config


# config_loader reads config values and stores as dictionary
# get timeout method
# get base_url
class ConfigLoader:
    def __init__(self, config):
        self.config = config

    def get_timeout(self):
        return self.config["timeout"]  # calling the dictionary value should use ["attribute"]

    def get_base_url(self):
        print(self.config["base_url"])
        return self.config["base_url"]  # calling the dictionary value should use ["attribute"]
