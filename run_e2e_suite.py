import pytest

if __name__ == "__main__":
    pytest.main([
        "tests/end_to_end/test_dashboard.py",
        "tests/end_to_end/test_admin.py"
    ])
