import requests

def get_address_from_coordinates(latitude, longitude):
    # OpenStreetMap Nominatim APIのエンドポイント
    endpoint = "https://nominatim.openstreetmap.org/reverse"

    # パラメータを設定
    params = {
        "format": "json",
        "lat": latitude,
        "lon": longitude,
        "accept-language": "ja"
    }

    try:
        # APIリクエストを送信
        response = requests.get(endpoint, params=params)
        data = response.json()

        if response.status_code == 200 and "address" in data:
            address = data["address"]
            japanese_address = address.get("province", "") +  address.get("city", "") + address.get("town", "") + address.get("quarter", "")
            return japanese_address.strip()
        else:
            return "住所が見つかりませんでした。"

    except requests.RequestException as e:
        return f"エラーが発生しました: {e}"
