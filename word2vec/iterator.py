class BeyonceIterable(object):
    def __iter__(self):
        """
        The iterable interface: return an iterator from __iter__().

        Every generator is an iterator implicitly (but not vice versa!),
        so implementing `__iter__` as a generator is the easiest way
        to create streamed iterables.

        """
        for word in 'baby let me iterate ya'.split():
            yield word + '!'  # uses yield => __iter__ is a generator


iterable = BeyonceIterable()

for val in iterable:  # iterator created here
    print (val, 'baby! let! me! iterate! ya!')

print ('caca ')
for val in iterable:  # another iterator created here
    print (val, 'baby! let! me! iterate! ya!')