import requests


def download_image():
    url = 'https://w.wallhaven.cc/full/x8/wallhaven-x8wz7o.jpg'

    # will only print the binary data of the picture
    # response = requests.get(url)
    # print(response.status_code)
    # print(response.content)

    # download the picture through byte stream
    response = requests.get(url, stream=True)

    with open('Lux.jpg', 'wb') as file:
        for data in response.iter_content(128):
            file.write(data)
    print(response.status_code)


if __name__ == '__main__':
    download_image()
