import json
import requests
import os


class Linked_in_User():

    def __init__(self, Username):
        self.Username = Username
        self.UserURL = 'https://ir.linkedin.com/in/{}'.format(self.Username)

    def get_user_stats(self):

        # this is data from github, we dont need all of it
        UserDataFromGithub = requests.get(self.UserURL).json()
        DataNeeded = [
            'name',
            'type',
            'company',
            'blog',
            'location',
            'email',
            'public_repos',
            'followers'
        ]
        print(UserDataFromGithub)
        
        return json.dumps(self.UserData, indent=True)
