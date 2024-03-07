# Get environment info for effective prompts
import os
import distro

class GetEnvironmentMeta:
    def __init__(self):
        self.shell = os.environ.get('SHELL')
        self.distro_name = distro.name(pretty=True)
        self.distro_version = distro.version(pretty=True)
        self.environment_des = self.distro_name + " " + self.distro_version + " " + self.shell
    def cur_env_meta(self):
        return self.environment_des