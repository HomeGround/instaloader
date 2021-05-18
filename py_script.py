import instaloader
from instaloader import structures
import re,os
TXT_Urls="urls_to_down.txt"
# Get instance
L = instaloader.Instaloader()
USER="you_even_gym_bro"
PASSWORD=""
drive_name="off_drive"
def url_to_short_code(post_url):
    regexp = '^(?:.*\/(p|tv)\/)([\d\w\-_]+)'
    post_short_code = re.search(regexp, post_url).group(2)
    # print('From url {} extracted shorcode:{}'.format(post_url, post_short_code))
    return post_short_code

# Optionally, login or load session
L.login(USER, PASSWORD)        # (login)
# L.interactive_login(USER)      # (ask password on terminal)
L.load_session_from_file(USER) # (load session created w/
                               #  `instaloader -l USERNAME`)

# for post in instaloader.Hashtag.from_name(L.context, 'cat').get_posts():
#     # post is an instance of instaloader.Post
#     L.download_post(post, target='#cat')
# SHORTCODE="CO0JbpkjOfi"
# post = structures.Post.from_shortcode(L.context, SHORTCODE)
#
#
# L.download_post(post,drive_name)
#
#
#
#
# file=open("urls_to_down.txt")
file=open(TXT_Urls)
lines=file.readlines()
for line in lines:
    url=str(line)
    print(url)
    SHORTCODE=url_to_short_code(url)
    post = structures.Post.from_shortcode(L.context, SHORTCODE)

    L.download_post(post, "Off_drive")
