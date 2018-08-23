import time
from autotest.client import test


class sleeptest23(test.test):
    version = 1

    def run_once(self, seconds=1):
        time.sleep(seconds)
