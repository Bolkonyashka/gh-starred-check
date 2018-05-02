import argparse 
import requests
import sys

parser = argparse.ArgumentParser(description="Displays all repositories to which the user has set the rating")
parser.add_argument('username', metavar='username', nargs=1,
                    help='Username on github.com')

args = parser.parse_args()
username = args.username[0]

response = requests.get('https://api.github.com/users/' + username + '/starred')
try:
    response.raise_for_status()
except requests.exceptions.HTTPError as e:
    print('Error: ', e)
    sys.exit()

json_resp = response.json()
if len(json_resp) == 0:
    print('User has not starred any repository')
else:
    print('The user has starred the following repositories:\r\n')
    for repo in json_resp:
        print('%s - %d' % (repo['name'], repo['stargazers_count']))
