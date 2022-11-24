import configparser
import requests
import sys

config = configparser.ConfigParser()
config.read('config.ini')

session = config['DEFAULT']['Session']
year = config['DEFAULT']['Year']

day = int(sys.argv[1])
r = requests.get(f'https://adventofcode.com/{year}/day/{day}/input', headers={'cookie':f'session={session}'})

with open(f'day{day}/{day}.txt', 'wb') as f:
    f.write(r.content)