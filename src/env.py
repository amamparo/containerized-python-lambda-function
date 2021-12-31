import json
from dataclasses import dataclass

import boto3
from dotenv import load_dotenv
from os import environ

from injector import singleton, inject

load_dotenv()


@dataclass
@singleton
class Env:
  some_environment_variable: str = environ.get('SOME_ENVIRONMENT_VARIABLE', 'foo')
  some_other_environment_variable: str = environ.get('SOME_OTHER_ENVIRONMENT_VARIABLE', 'bar')


@dataclass
@singleton
class AwsEnv(Env):
  @inject
  def __init__(self) -> None:
    secret = boto3.client('secretsmanager').get_secret_value(SecretId=environ['AWS_ENVIRONMENT_SECRET_ID'])
    env = json.loads(secret['SecretString'])
    self.some_environment_variable = env['SOME_ENVIRONMENT_VARIABLE']
    self.some_other_environment_variable = env['SOME_OTHER_ENVIRONMENT_VARIABLE']
