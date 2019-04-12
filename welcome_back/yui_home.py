import datetime
import os
import requests
import serial
import subprocess
import time
import timeout_decorator


SLACK_TOKEN = os.environ['SLACK_TOKEN']
SLACK_CHANNEL = os.environ['SLACK_CHANNEL']


def post_message_to_slack():
    param = {
        'token': SLACK_TOKEN,
        'channel': SLACK_CHANNEL,
        'text': 'yui not home!'
    }
    requests.post(url="https://slack.com/api/chat.postMessage", params=param)


def post_photo_to_slack(file_name):

    param = {
        'token': SLACK_TOKEN,
        'channels': SLACK_CHANNEL,
        'filename': file_name,
        'initial_comment': 'yui go home!',
        'title': "title"
    }
    files = {'file': open(file_name, 'rb')}
    requests.post(url="https://slack.com/api/files.upload", params=param, files=files)


@timeout_decorator.timeout(3600)
def get_open_status():

    today = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    file_name = '/home/pi/welcome_back/photo/image' + today + 'jpg'
    photo_cmd = 'fswebcam -r 600x400 ' + file_name

    s = serial.Serial('/dev/ttyUSB0', 115200)
    while 1:
        rdata = s.readline()
        try:
            subprocess.call(photo_cmd, shell=True)
            post_photo_to_slack(file_name)
            break
        except:
            print('Erro:fswebcam')

    s.close()


if __name__ == '__main__':
    try:
        get_open_status()
    except:
        post_message_to_slack()
