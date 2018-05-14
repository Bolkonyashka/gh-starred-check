import argparse
import requests
import sys


def get_starred_info():
    descr = "Displays all repositories to which the user has set the star"
    parser = argparse.ArgumentParser(description=descr)
    parser.add_argument('username', type=str, metavar='username',
                        help='Username on github.com')

    args = parser.parse_args()
    username = args.username

    response = requests.get('https://api.github.com/users/' +
                            username + '/starred')
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

if __name__ == "__main__":
    get_starred_info()
