import argparse
from bardapi import Bard
import os
import requests
from decouple import config

BARD_COOKIE = config('BARD_COOKIE')
BARD_API_TOKEN = config('BARD_API_TOKEN')


def main(question):
    session = requests.Session()
    session.headers = {
        "Host": "bard.google.com",
        "X-Same-Domain": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "Origin": "https://bard.google.com",
        "Referer": "https://bard.google.com/",
    }
    session.cookies.set("__Secure-1PSID", BARD_COOKIE) 

    bard = Bard(token=BARD_API_TOKEN, session=session, timeout=30)

    answer = bard.get_answer(question)['content']
    print(answer)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Parse cookie and question arguments.')

    parser.add_argument('--question', required=True, help='Question value')

    args = parser.parse_args()

    main(args.cookie, args.question)
