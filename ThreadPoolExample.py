'''
@see http://stackoverflow.com/questions/6893968/how-to-get-the-return-value-from-a-thread-in-python
'''

def foo(bar, baz):
  print 'hello {0}'.format(bar)
  return 'foo' + baz

from multiprocessing.pool import ThreadPool
pool = ThreadPool(processes=1)

async_result = pool.apply_async(foo, ('world', 'foo')) # tuple of args for foo

# do some other stuff in the main process

return_val = async_result.get()  # get the return value from your function.
