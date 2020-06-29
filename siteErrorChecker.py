import time
import requests

class notify:
    def __init__(self):
        self.line = str(input('LINEアクセストークンを入力して下さい:'))
        self.discord = str(input('DiscordアクセスURLを入力して下さい:'))

    def line_message(self, message):
        url = 'https://notify-api.line.me/api/notify'
        headers = {'Authorization': 'Bearer ' + self.line}
        payload = {'message': message}
        requests.post(url, headers=headers, params=payload)

    def discord_notify(self,message):
        url = self.discord
        requests.post(url, data={'content': message})

    def notify(self,message):
        self.line_message(message=message)
        self.discord_notify(message=message)

def access(url):
    html = requests.get(url)
    if html.status_code == 200:
        return False
    else:
        return True

def web_monitor(url,notify):
    print('Monitoring Start!')
    notify.notify(message='Monitoring start!')
    flag = False
    # default value is False
    while True:
        if flag == access(url):
            pass
        else:
            if flag == False:
                notify.notify(message='アクセス障害が発生しています。')
            else:
                notify.notify(memssage='アクセス障害が復旧しました。')
            flag = not flag
        time.sleep(600)

if __name__ == '__main__':
    URL = str(input('監視対象のURLを入力して下さい:'))
    notify = notify()
    web_monitor(URL,notify)