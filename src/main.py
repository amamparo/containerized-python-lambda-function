from typing import Dict, Any
from injector import inject, Injector, Module

from src.foo_service import FooService
from src.modules import DeployedModule, LocalModule


class Main:
  @inject
  def __init__(self, foo_service: FooService):
    self.__foo_service = foo_service

  def run(self) -> None:
    print('Hello, world')


def run(module: Module) -> None:
  Injector(module).get(Main).run()


def lambda_handler(event: Dict = None, context: Any = None) -> None:
  run(DeployedModule())


if __name__ == '__main__':
  run(LocalModule())
