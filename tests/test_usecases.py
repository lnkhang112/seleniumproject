import pytest
from usecases.usecases import login, check_requirement

def test_login_ok():
    result = login("admin", "123456")
    assert result["status"] == "success"
    assert result["token"] is not None

def test_login_fail():
    result = login("user", "wrongpass")
    assert result["status"] == "fail"
    assert result["token"] is None

def test_check_requirement_ok():
    # Login trước để lấy token
    login_result = login("admin", "123456")
    token = login_result["token"]

    result = check_requirement(token)
    assert result["status"] == "ok"
    assert len(result["requirements"]) > 0

def test_check_requirement_unauthorized():
    result = check_requirement("wrongtoken")
    assert result["status"] == "unauthorized"
    assert result["requirements"] == []
