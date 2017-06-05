class TestClassA():
    def setUp(self):
        self.text = "apple"
        print(self.text * 5)

    def teardown(self):
        self.text = None

    def test_1(self):
        assert self.text == "apple"
        self.text = "orange"
        assert self.text == "orange"
        print(self.text)

    def test_2(self):
        assert self.text != "orange"
        print(self.text)
