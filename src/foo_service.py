from injector import inject, singleton

from src.env import Env


@singleton
class FooService:
  @inject
  def __init__(self, env: Env):
    pass
