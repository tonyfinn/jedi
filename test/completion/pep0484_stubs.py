""" Pep-0484 type hinting with stub files"""

# python >= 3.2

def basic_works():
    from import_tree import stubbed

    #? str()
    stubbed.x[1]

    #? int()
    stubbed.mismatched[1]

    #? 21 ['k', 'KeyboardInterrupt', 'KeyError']
    y = stubbed.Foo(k)

    z = stubbed.Foo('baz')

    #? ['stubonly']
    z.stu

def stub_only():
    from import_tree import stubonly

    #? ['do_stuff']
    stubonly.d

def stub_pkg():
    from stub_tree import stub

    #? ['do_more']
    stub.d