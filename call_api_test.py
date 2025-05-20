import requests
from concurrent.futures import ThreadPoolExecutor

# Hàm gọi API
def call_api():
    url = "http://127.0.0.1:8000/user/list_user/"
    # url = "http://127.0.0.1:8888/user/list_user_async/"

    try:
        requests.get(url)
        # print(f"Status Code: {response.status_code}, Response: {response.text}")
    except Exception as e:
        print(f"Lỗi khi gọi API: {e}")

# Sử dụng ThreadPoolExecutor
def call_api_concurrently(times):
    with ThreadPoolExecutor(max_workers=times) as executor:
        executor.map(lambda _: call_api(), range(times))

# Gọi API 10 lần đồng thời
if __name__ == "__main__":
    call_api_concurrently(10000)
