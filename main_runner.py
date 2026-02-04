import pytest

if __name__ == "__main__":
    pytest.main([
        "tests/end_to_end/test_admin.py",
        "tests/end_to_end/test_pim.py",
        "tests/end_to_end/test_my_info.py",
        "tests/end_to_end/test_directory.py",
        "tests/end_to_end/test_maintenance.py",
        "tests/end_to_end/test_buzz.py",
        "tests/end_to_end/test_profile.py"
    ])
