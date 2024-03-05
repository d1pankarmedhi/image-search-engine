import yaml


class Config:
    """Config class."""

    @staticmethod
    def get_config(config_path: str = "config.yaml") -> dict:
        """
        Returns the configuration data.
        """

        with open(config_path, "r") as yamlfile:
            data = yaml.load(yamlfile, Loader=yaml.FullLoader)
        return data
