import Pyro.naming, Pyro.core
from Pyro.errors import NamingError

# locate the NS
locator = Pyro.naming.NameServerLocator()
print 'Searching Name Server...',
ns = locator.getNS()
# resolve the Pyro object
print 'finding object'
try:
        URI=ns.resolve('test')
        print 'URI:',URI
except NamingError,x:
        print 'Couldn\'t find object, nameserver says:',x
        raise SystemExit

# create a proxy for the Pyro object, and return that
test = Pyro.core.getProxyForURI(URI)

print test.mul(111,9)
print test.add(100,222)
print test.sub(222,100)
print test.div(2.0,9.0)
print test.mul('*',10)
print test.add('String1','String2')