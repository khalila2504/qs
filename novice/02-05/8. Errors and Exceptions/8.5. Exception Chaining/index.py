raise RuntimeError from exc
def func():
    raise ConnectionError
try:
    func()
except ConnectionError as exc:
    raise RuntimeError('failed') from exc
    