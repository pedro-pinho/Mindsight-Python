import time
from concurrent.futures import ThreadPoolExecutor

def parse_url(url):
    time.sleep(1)
    print(url)
    return "done."

st = time.time()
with ThreadPoolExecutor(max_workers=10) as executor:
    for i in range(300):
        future = executor.submit(parse_url, "http://google.com/%s"%i)

print("total time: %s"%(time.time() - st))