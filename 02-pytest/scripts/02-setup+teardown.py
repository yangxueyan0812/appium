import pytest
import allure

class Test1:
    #setup_class和tear_down每个类执行一次
    def setup_class(self):
        print("setup_class")
    def teardown_class(self):
        print("teardown_class")

    #setup和teardown每个方法执行一次
    def setup(self):
        print("setup")

    def teardown(self):
        print("teardown")

    @allure.step('我是测试步骤001')
    def test_hello1(self):
        print("hello world--test1")
        assert 1
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_hello2(self):
        allure.attach('hello2', '我是测试步骤002的描述～～～')
        print("hello world--test2")
        assert 1

# if __name__ == '__main__':
#     pytest.main(["-s" , "02-setup+teardown.py"])