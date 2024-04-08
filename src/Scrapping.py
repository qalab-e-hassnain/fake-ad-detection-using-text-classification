import requests
from bs4 import BeautifulSoup
import re


def remove_emoji(string):
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"
                               u"\U0001F300-\U0001F5FF"
                               u"\U0001F680-\U0001F6FF"
                               u"\U0001F1E0-\U0001F1FF"
                               u"\U00002500-\U00002BEF"
                               u"\U00002702-\U000027B0"
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               u"\U0001f926-\U0001f937"
                               u"\U00010000-\U0010ffff"
                               u"\u2640-\u2642"
                               u"\u2600-\u2B55"
                               u"\u200d"
                               u"\u200c"
                               u"\u23cf"
                               u"\u23e9"
                               u"\u06d4"
                               u"\u231a"
                               u"\ufe0f"
                               u"\u3030"
                               u"\u013a"
                               u"\u1e34"
                               U"\u0600-\u06ff"
                               U"\u20e3"
                               U"\u2211"
                               U"\u2105"
                               U"\u203c"
                               "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', string)


def Seller_Comment(url):
    r = requests.get(url)
    htmlContent = r.content
    soup = BeautifulSoup(htmlContent, 'html.parser')

    comment_class = soup.find('h2', id="scroll_seller_comments")
    comment_div = comment_class.find_next_sibling('div')
    sellers_comment = comment_div.text
    sellers_comment = str(sellers_comment)
    split_string = sellers_comment.split("Mention", 1)
    s_comment = split_string[0]
    se_comments = remove_emoji(s_comment)
    return se_comments
