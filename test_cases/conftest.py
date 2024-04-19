from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'ie':
        driver = webdriver.Ie()
    else:
        driver = webdriver.Chrome()
    return driver


def pytest_addoption(parser):
    parser.addoption('--browser')


@pytest.fixture()
def browser(request):
    return request.config.getoption('--browser')


def pytest_configure(config):
    config._metadata = {
    'Project Name' : 'nop commerce',
    'Module Name' : 'customers',
    'Tester' : 'test'
    }

"""
def normalize_hookimpl_opts(opts):
    opts.setdefault("tryfirst", False)
    opts.setdefault("trylast", False)
    opts.setdefault("hookwrapper", True)
    opts.setdefault("optionalhook", False)


@pytest.hookimpl(hookwrapper=True)
def pytest_collection(session):
    collect_timeout = 5
    collect_begin_time = time.time()
    yield
    collect_end_time = time.time()
    c_time = collect_end_time - collect_begin_time
    if c_time > collect_timeout:
        raise Exception('Collection timeout.')
"""
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME',None)
    metadata.pop('Plugins', None)