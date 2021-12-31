from injector import Binder, Module

from src.env import Env, AwsEnv


class LocalModule(Module):
  def configure(self, binder: Binder) -> None:
    binder.bind(Env, to=Env)


class DeployedModule(Module):
  def configure(self, binder: Binder) -> None:
    binder.bind(Env, to=AwsEnv)
