class NetworkService:
  def __init__(self, name, config):
    self.name = name
    self.config = config

  def set_name(self, name):
    self.name = name

  def set_config(self, config):
    self.config = config

  def deploy_service(self):
    Infrastructure.deploy(self.name, self.config)
