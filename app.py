import requests
import time

def load_proxies(file_path):
  
    with open(file_path, "r") as file:
        proxies = file.readlines()
   
    proxies = [proxy.strip() for proxy in proxies if proxy.strip()]
    return proxies

def fetch_with_proxy(url, proxy):
    
    proxy_ip, proxy_port = proxy.split(":")

 
    proxies = {
        "http": f"http://{proxy_ip}:{proxy_port}",
        "https": f"http://{proxy_ip}:{proxy_port}",
    }

    try:
        
        response = requests.get(url, proxies=proxies, timeout=10)

      
        if response.status_code == 200:
            print(f"Successfully accessed the site through proxy: {proxy}")
            print("Site response:")
            print(response.text[:500])  
        else:
            print(f"Failed to access the site through proxy {proxy}. Status code: {response.status_code}")
    except requests.exceptions.ProxyError:
        print(f"Proxy error: {proxy}")
    except requests.exceptions.RequestException as e:
        print(f"Request error through proxy {proxy}: {e}")

def main(url, proxy_file):

    proxies = load_proxies(proxy_file)

   
    while True:
        for proxy in proxies:
            fetch_with_proxy(url, proxy)
            
            time.sleep(1)


url = "URL_TARGET_SITE"   #Site url
proxy_file = "proxy.txt"  #Your proxy list

main(url, proxy_file)