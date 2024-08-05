import src.environment.default

from src.service1.mixin import Service1Mixin
from src.service2.mixin import Service2Mixin

class Worker(Service1Mixin, Service2Mixin):
    def do_work(self):
        self.service1.work()
        self.service2.work()

Worker().do_work()