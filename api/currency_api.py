from api.base_api_client import ApiClient


class CurrencyApi(ApiClient):
    def __init__(self):
        super().__init__("https://api.frankfurter.dev/v2/rate")

    def get_data(self, query):
        amount = query.get("amount")
        from_currency = query.get("from_currency").upper()
        to_currency = query.get("to_currency").upper()

        url = f"{self._base_url}/{from_currency}/{to_currency}"

        data = self._make_request(url)

        if data is None:
            return None

        rate = data.get("rate")

        if rate is None:
            return None

        converted_amount = round(amount * rate, 2)

        return {
            "amount": amount,
            "from_currency": from_currency,
            "to_currency": to_currency,
            "rate": rate,
            "converted_amount": converted_amount,
        }
