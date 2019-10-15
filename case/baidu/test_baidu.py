from page import baidu_page
import browser
import pytest
import sys


@pytest.fixture(scope="module")
def setup_module():
    baidu_page.home()
    yield
    browser.stop()


@pytest.mark.parametrize("keyword", ["selenium", "自动化测试", "python"])
def test_search(keyword, setup_module):
    print("输入关键字：【" + keyword + "】搜索")
    baidu_page.search(keyword)
    baidu_page.get_search_result()


if __name__ == '__main__':
    pytest.main([sys.argv[0]])
