import pytest
import requests
import main as p

url = "https://api.exchangerate-api.com/v4/latest/USD"


def main():
    test_show_currencies()
    test_numbers_only()
    test_output()
    test_numbers_only()


def test_show_currencies():

    assert p.show_currencies(url) == requests.get(url).json()["rates"]


def test_convert():
    assert (
        p.convert("USD", "INR", 100) == requests.get(url).json()["rates"]["INR"] * 100
    )
    assert p.convert("JPY", "AUD", 50000) == round(
        50000
        * requests.get(url).json()["rates"]["AUD"]
        / requests.get(url).json()["rates"]["JPY"],
        4,
    )


def test_output():
    assert (
        p.output("USD", "INR", float(100))
        == f"100.0 USD is equivalent to {round(p.convert('USD', 'INR', 100), 2)} INR"
    )
    assert (
        p.output("JPY", "AUD", float(50000))
        == f"50000.0 JPY is equivalent to {round(p.convert('JPY', 'AUD', 50000), 2)} AUD"
    )
    with pytest.raises(SystemExit):
        assert p.output("abc", "xyz", float(123))


def test_numbers_only():
    assert p.numbers_only("1000") == "1000"
    assert p.numbers_only("1,000") == "1000"
    assert p.numbers_only("1,000,000.00") == "1000000.00"
    with pytest.raises(SystemExit):
        p.numbers_only("abc123")
    with pytest.raises(SystemExit):
        p.numbers_only("1.000.00")


if __name__ == "__main__":
    main()
