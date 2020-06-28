import requests
import pandas
from bs4 import BeautifulSoup


def get_url_html(url: str):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'

    headers = {
        "User-Agent": user_agent,
        'Cookie': '__mta=222122535.1593142612666.1593142847141.1593142870733.9; uuid_n_v=v1; uuid=46318240B75E11EA9C0AF732B1940F47A9A76B57EC6A4BE3A7DD92F2C403AB0A; _csrf=c31ce07eb8faab105663ad62a516058cd6b047979b0770110547127735f7c5d1; mojo-uuid=c6b8eb14bb2f3bc501074e94b8074f9c; _lxsdk_cuid=172eeb31223c8-07bc15662ca93c-4353760-1bcab9-172eeb3122395; _lxsdk=46318240B75E11EA9C0AF732B1940F47A9A76B57EC6A4BE3A7DD92F2C403AB0A; mojo-session-id={"id":"d92f353ffc75eaa9580519f8974943c0","time":1593142612536}; lt=NGasidSZ6zE6ovA8CG95KS-_rIQAAAAA5woAAA55z4CS3rvkpsKkv2GYbmTFuB37EgqV3pC5Cmh2WN6mJ8IOPFgebttlkYAd3MOG7w; lt.sig=XB09fEDTRPnAVsOyo4IJJAxXq5s; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593142630,1593147432,1593147698,1593147812; mojo-trace-id=23; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593149271; __mta=222122535.1593142612666.1593142870733.1593149271077.10; _lxsdk_s=172eeb31225-e42-e97-639%7C%7C46',
        "Referer": "https://www.maoyan.com/",
    }

    response = requests.get(url, headers=headers)

    return response.text


def get_movie_info_by_bs(html):
    bs_info = BeautifulSoup(html, 'html.parser')
    movie_info_list = []
    for tag in bs_info.find_all('div', {'class': 'movie-item film-channel'}):
        movie_name = tag.find('span', {'class': 'name'}).text
        movie_type = tag.find_all("div", {"class":"movie-hover-title"})[1].text.split(":")[-1].strip()
        movie_date = tag.find_all("div", {"class":"movie-hover-title movie-hover-brief"})[0].text.split(":")[-1].strip()
        movie_info_list.append([movie_name, movie_type, movie_date])
    return movie_info_list


def data_to_csv(data_list, file_name):
    data = pandas.DataFrame(data=data_list)
    data.to_csv(file_name, encoding='utf-8', index=False, header=False, mode='a')


if __name__ == '__main__':
    html = get_url_html('https://maoyan.com/films?showType=3')
    movie_info_list = get_movie_info_by_bs(html)
    print(movie_info_list)

    for i in range(10):
        if i < len(movie_info_list):
            data_to_csv(movie_info_list[i], './movie_1.csv')
