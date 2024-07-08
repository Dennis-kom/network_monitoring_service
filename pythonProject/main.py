import requests

MIN_SPEC_TO = 5
MAX_SPEC_TO = 20


def internet_connection(timeout_spec: int = 5):
    try:
        response = requests.get("https://www.google.com", timeout=timeout_spec)
        return True
    except requests.ConnectionError:
        return False


def connection_test(long_test: bool = False):
    return all(
        list(map(internet_connection, (MAX_SPEC_TO, 15, 12, 9, 6, MIN_SPEC_TO) if long_test else (7, 6, MIN_SPEC_TO))))


def main():
    print("Connected" if connection_test() else "Disconnected")


if __name__ == "__main__":
    main()
