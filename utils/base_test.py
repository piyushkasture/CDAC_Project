import pytest

@pytest.mark.usefixtures("setup_and_teardown")
class BaseTest:
    page = None


