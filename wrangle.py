import os
import json
from typing import Dict, List, Optional, Union, cast
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
from env import github_token, github_username
import unicodedata

def acquire():
    file_name = 'nlp_repos.csv'
    if os.path.isfile(file_name):
        return pd.read_csv(file_name)
    else:
        url = 'https://github.com/EvanLi/Github-Ranking/blob/master/Top100/Top-100-stars.md'
        headers={"Authorization": f"token {github_token}", "User-Agent": github_username}
        response = requests.get(url, headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        repo_links = soup.find_all('a')
        repos = [link_tag['href'] for link_tag in repo_links][3:]

        i = 0 
        for repo in repos:
            repos[i] = repos[i][2:-2]
            i += 1

        url2 = 'https://github.com/trending?since=daily'
        headers2={"Authorization": f"token {github_token}", "User-Agent": github_username}
        response2 = requests.get(url2, headers2)
        soup2 = BeautifulSoup(response2.text, 'html.parser')
        repo_links2 = soup2.find_all('a')
        repos2 = [link_tag['href'] for link_tag in repo_links2]

        link_one = f'https://github.com{repos2[948]}'
        link_two = f'https://github.com{repos2[957]}'
        link_three = f'https://github.com{repos2[966]}'
        link_four = f'https://github.com{repos2[975]}'
        link_five = f'https://github.com{repos2[984]}'

        repos.append(link_one)
        repos.append(link_two)
        repos.append(link_three)
        repos.append(link_four)
        repos.append(link_five)

        url = repos[0]
        response = requests.get(url, headers={"Authorization": f"token {github_token}", "User-Agent": github_username})
        soup = BeautifulSoup(response.text, 'html.parser')

        read = []
        i = 0
        for readme in repos:
            url = repos[i]
            response = requests.get(url, headers={"Authorization": f"token {github_token}", "User-Agent": github_username})
            soup = BeautifulSoup(response.text, 'html.parser')
            read.append([element.text for element in soup.find_all('readme-toc')])
            i += 1

        i = 0
        for readme in repo:
            [element.text for element in soup.find_all('readme-toc')]

        titles = []
        pattern = r'[^/]+$'
        for repo in repos:
            match = re.search(pattern, repo)
            last_part = match.group()
            titles.append(last_part)
        titles[105] = titles[105][-22:]
        titles[106] = titles[106][-10:]

        flat_list = [item for sublist in read for item in sublist]
        # Convert each item to a string
        flat_list_of_strings = [str(item) for item in flat_list]

        new_dict = dict(zip(titles, flat_list_of_strings))

        df = pd.DataFrame(list(new_dict.items()), columns=['title', 'readme'])

        df.title = df.title.str.lower()
        df.readme = df.readme.str.lower()
        df.to_csv('nlp_repos.csv')
        return df