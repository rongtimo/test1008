import time

class retry(object):
    def __init__(self, max_retries=3, wait=0, exceptions=(Exception,)):
        self.max_retries = max_retries
        self.exceptions = exceptions
        self.wait = wait

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            for i in range(self.max_retries + 1):
                try:
                    result = func(*args, **kwargs)
                except self.exceptions:
                    time.sleep(self.wait)
                    continue
                else:
                    return result
        return wrapper


import random

@retry(5, 3, (ValueError, TypeError))
def downloader(url):
    n = random.randint(-10, 10)
    print('n = %s' % n)
    if n < 0:
        raise ValueError('n < 0')
    else:
        return url
