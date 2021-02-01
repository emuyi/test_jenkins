
class TestStringMethods:

    def test_upper(self):
        assert 'foo'.upper() == 'FOO'

    def test_split(self):
        s = 'hello world'
        assert s.split() ==  ['hell', 'world']
