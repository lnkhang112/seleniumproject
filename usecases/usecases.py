# Đây là hàm logic mô phỏng chức năng hệ thống

def login(username, password):
    # Giả lập login
    if username == "admin" and password == "123456":
        return {"status": "success", "token": "abc123"}
    else:
        return {"status": "fail", "token": None}


def check_requirement(token):
    # Giả lập check requirement
    if token == "abc123":
        return {"status": "ok", "requirements": ["Req1", "Req2", "Req3"]}
    else:
        return {"status": "unauthorized", "requirements": []}
