import requests
import yaml



def get_BGB():
    coin_url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=bitget-token"
    response = requests.get(coin_url)
    response = response.json()
    current_price, change_percentage = response[0]['current_price'], response[0]['price_change_percentage_24h']
    data = {
        "current_price": current_price,
        "change_percentage": change_percentage
    }
    return data

def notion_update(current_price, current_change_percentage):

    with open("my_variables.yml", 'r') as stream:
        try:
            my_variables_map = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print("[Error]: while reading yml file", exc)

    headers = {
    'Notion-Version': '2021-05-13',
    'Authorization': 'Bearer ' + my_variables_map["MY_NOTION_SECRET_TOKEN"]
    }

    page_id = my_variables_map['PAGE_ID']
    BGBUSDT = current_price
    change_percentage = current_change_percentage

    update_data = {
        "properties": {
            'symbol': {
                'id': 'title',
                'type': 'title',
                'title': [
                    {
                        'type': 'text',
                        'text': {'content': 'BGBUSDT'},
                        'annotations': {'bold': False, 'italic': False, 'strikethrough': False, 'underline': False, 'color': 'default'},
                        'plain_text': 'BGBUSDT',
                    }
                ]
            },
            'price': {
                'id': 'Xo;P',
                'type': 'rich_text',
                'rich_text': [
                    {
                        'type': 'text',
                        'text': {'content': current_price},
                        'annotations': {'bold': False, 'italic': False, 'strikethrough': False, 'underline': False, 'color': 'default'},
                        'plain_text': current_price,
                    }
                ]
            },
            'changesPercentage': {
                'id': 'MG`I',
                'type': 'rich_text',
                'rich_text': [
                    {
                        'type': 'text',
                        'text': {'content': current_change_percentage},
                        'annotations': {'bold': False, 'italic': False, 'strikethrough': False, 'underline': False, 'color': 'default'},
                        'plain_text': current_change_percentage,
                    }
                ]
            }
        }
    }
    url = f"https://api.notion.com/v1/pages/{page_id}"
    response = requests.patch(url, headers=headers, json=update_data)

    return response