def test_args(*args):
    print args
    print list(args)
test_args()
test_args(1, 2, 'asdfa')

print("\n\n")
def test_kwargs(**kwargs):
    for key, value in kwargs.iteritems():
        print key, value

test_kwargs(a=1, b= "afsdf", c=["HI", 3], d={1:"qq", 2:22})
