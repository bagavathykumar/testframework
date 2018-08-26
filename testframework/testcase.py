from abc import ABCMeta, abstractmethod

class Environment():
    def get_env(self):
        pass
    def print_env(self):
        pass
    def add_env(self):
        pass
    def remove_env(self):
        pass

class Testcase():
    __metaclass__ = ABCMeta
    @abstractmethod
    def test_setup(self):
        pass
    @abstractmethod
    def test_run(self):
        pass
    @abstractmethod
    def test_verify(self):
        pass
    @abstractmethod
    def test_teardown(self):
        pass
    @abstractmethod
    def test_details(self):
        pass
