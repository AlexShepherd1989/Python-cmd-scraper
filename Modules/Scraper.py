import requests

from Config.ScrapConfig import sites, proxies
from Modules.FileCreator import create_file


def scrap():
    for i, url in enumerate(sites, start=1):
        try:
            response = requests.get(
                url,
                headers={"User-Agent": "Mozilla/5.0"},
                proxies=proxies,
                timeout=5
            )
            if response.status_code == 200:
                html = response.text
                create_file(html, i)
            else:
                print(f"Error on request: {response.status_code}")

        except requests.exceptions.ProxyError:
            print(f"Proxy failed fro {url}, skipping...")
            continue
        except requests.exceptions.ConnectTimeout:
            print(f"Connection timed out for {url}, skipping")
            continue
        except requests.exceptions.RequestException as e:
            print(f"Request failed for {url}: {e}")
            continue
