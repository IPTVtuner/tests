import requests
import json
import os
import datetime

if __name__ == '__main__':
    with open('channelList.json') as channelList:
        channels = json.load(channelList)
    #channels = {'Sky News': 'sky-news', 'Tiny Pop (Freeview) Today': 'tiny-pop-freeview'}
    baseurl = 'https://tv24.co.uk'
    today = datetime.datetime.strftime(datetime.datetime.utcnow(), '%B %d')
    for channel in channels:
        ch_name = channels[channel]
        link, title, description = 'NA', 'NA', 'NA'
        try:
            response = requests.get(f'{baseurl}/x/channel/{ch_name}/330/today').text
            raw = response.split('<li class="ongoing">')[-1].split('</li>')[0]
            link = baseurl + raw.split('<a href="')[-1].split('"')[0]
            title = raw.split('<h3>')[-1].split('</h3>')[0]
            description = raw.split('<p>')[-1].split('</p>')[0]
        except Exception as e:
            print(f'some error: {e}')
        if 'files' not in os.listdir():
            os.mkdir('files')
        with open(f'files/{ch_name}.txt', 'w') as writer:
            writer.write(f'{channel}\nToday, {today}\n{description}')
        print(f'{channel}\t{description}')
