import requests

def test_ui_running():
    res = requests.get("http://localhost:5000/")
    assert res.status_code == 200
    print("UI test passed.")

if __name__ == "__main__":
    test_ui_running()
