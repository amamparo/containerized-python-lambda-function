from unittest import TestCase


class FooServiceTest(TestCase):

  def test_foo(self) -> None:
    self.assertEqual('foobar'.upper(), 'FOOBAR')
