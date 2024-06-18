from needless import needless_decorator
from unittest.mock import patch

@patch("ddtrace.config._potato", "potato")
@needless_decorator
def test_needless():
    assert True
