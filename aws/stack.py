from os import getcwd, environ

from aws_cdk.aws_events import Rule, Schedule
from aws_cdk.aws_events_targets import LambdaFunction
from aws_cdk.aws_lambda import DockerImageFunction, DockerImageCode
from aws_cdk.core import Stack, Construct, App, Duration


class MyStack(Stack):
  def __init__(self, scope: Construct, _id: str, **kwargs) -> None:
    super().__init__(scope, _id, **kwargs)
    function = DockerImageFunction(
      self,
      'Function',
      function_name='template-function',
      code=DockerImageCode.from_image_asset(
        directory=getcwd(),
        file='Dockerfile',
        exclude=['cdk.out']
      ),
      environment={
        'AWS_ENVIRONMENT_SECRET_ID': environ['AWS_ENVIRONMENT_SECRET_ID']
      },
      timeout=Duration.minutes(1),
      allow_public_subnet=True
    )
    Rule(self, 'Schedule', schedule=Schedule.rate(Duration.minutes(5))).add_target(LambdaFunction(function))


if __name__ == '__main__':
  app = App()
  MyStack(app, 'investment-portfolio-template-stack')
  app.synth()
