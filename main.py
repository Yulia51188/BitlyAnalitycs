import requests
from dotenv import load_dotenv
import os
import argparse


def parse_arguments ():
    parser = argparse.ArgumentParser(
        description='Create a bitlink if input a long url. '
                'Count clicks if input a bitlink.'
    )
    parser.add_argument(
        'input_url',
        type=str,
        help='a bitlink or a long url'
    )
    return parser.parse_args()


def get_short_url(
    url,bitly_token,
    bitly_host="https://api-ssl.bitly.com",
    bitly_method="/v4/bitlinks"
):
    headers = {
        "Authorization":"Bearer {token}".format(token=bitly_token)
    }
    json_data = {"long_url":url}
    response = requests.post(
        "{host}{method}".format(host=bitly_host, method=bitly_method),
        json=json_data,
        headers=headers
    )
    json_response = response.json()
    if response.ok:
        return json_response['id']
    raise ValueError(json_response['message'])


def get_click_number(
    bitlink,
    bitly_token,
    bitly_host="https://api-ssl.bitly.com",
    bitly_method_template="/v4/bitlinks/{bitlink}/clicks/summary"
):
    headers = {
        "Authorization":"Bearer {token}".format(token=bitly_token)
    }
    settings = {
        "unit":"day",
        "units":-1
    }
    bitly_method = bitly_method_template.format(bitlink=bitlink)
    bitly_url = "{url}{method}".format(url=bitly_host, method=bitly_method)
    response = requests.get(
        bitly_url,
        headers=headers,
        params=settings
    )
    if not response.ok:
        raise ValueError(response.text)
    json_response = response.json()
    return json_response["total_clicks"]


def is_bitlink(
    bitlink,
    bitly_token,
    bitly_host="https://api-ssl.bitly.com",
    bitly_method_template="/v4/bitlinks/{bitlink}"
):
    headers = {
        "Authorization":"Bearer {token}".format(token=bitly_token)
    }
    bitly_method = bitly_method_template.format(bitlink=bitlink)
    bitly_url = "{url}{method}".format(url=bitly_host, method=bitly_method)
    response = requests.get(
        bitly_url,
        headers=headers,
    )
    return response.status_code != 404


def main():
    load_dotenv()
    bitly_token = os.getenv("BITLY_TOKEN")
    args = parse_arguments()
    input_string = args.input_url
    if is_bitlink(input_string, bitly_token):
        click_number = get_click_number(input_string, bitly_token)
        exit("The number of clicks to {0} is {1}".format(input_string,
                                                          click_number))
    print("The input string is not a bitlink.")
    try:
        bitlink = get_short_url(input_string, bitly_token)
    except ValueError as ve:
        exit("Input url or token is invalid. "
               "Can't create bitlink with error:\n{0}#".format(ve))
    print("Success! Your bitlink is: {0}".format(bitlink))


if __name__ == '__main__':
    main()