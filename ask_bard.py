import argparse
from bardapi import Bard
import os
import requests
os.environ['_BARD_API_KEY'] = 'xxxxxxx'
# token='xxxxxxx'


def main(cookie, question):
    session = requests.Session()
    session.headers = {
        "Host": "bard.google.com",
        "X-Same-Domain": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "Origin": "https://bard.google.com",
        "Referer": "https://bard.google.com/",
    }
    session.cookies.set("__Secure-1PSID", cookie) 

    # bard = Bard(token=token, session=session, timeout=30)
    bard = Bard(session=session, timeout=30)

    answer = bard.get_answer(question)['content']
    print(answer)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Parse cookie and question arguments.')

    parser.add_argument('--cookie', required=True, help='Cookie value')
    parser.add_argument('--question', required=True, help='Question value')

    args = parser.parse_args()

    main(args.cookie, args.question)
