import re
import os
def url_to_short_code(post_url):
    regexp = '^(?:.*\/(p|tv)\/)([\d\w\-_]+)'
    post_short_code = re.search(regexp, post_url).group(2)
    # print('From url {} extracted shorcode:{}'.format(post_url, post_short_code))
    return post_short_code

url=url_to_short_code("https://www.instagram.com/p/CO0JbpkjOfi/")
print(("instaloader --login you_even_gym_bro --password aafaq123456 -- -"+url))
os.system("instaloader --login you_even_gym_bro --password aafaq123456 -- -"+url)