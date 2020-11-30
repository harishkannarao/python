from mockito import mock, verify
from unittest import TestCase

from helloworld import helloworld


class HelloWorldTest(TestCase):

    def test_should_issue_hello_world_message(self):
        out = mock()

        helloworld(out)

        verify(out).write("Hello world of Python\n")
