import json
import requests
import os

# Username = input("Enter Your Username")
# Username = 'aminzayer'

# UserURL = 'https://api.github.com/users/{}'.format(Username)

# UserDataFromGithub = requests.get(UserURL).json()


def save_json(filename, json_data):
    with open('{}/{}.json'.format(os.path.dirname(__file__), filename), 'w') as fp:
        json.dump(json_data, fp, indent=False)

def extract_data(DataNeeded, DataFromGithub, ):
    Data = {}
    for (k, v) in DataFromGithub.items():

        if k in DataNeeded:
            Data[k] = v

    return Data

class User():

    def __init__(self, Username):
        self.Username = Username
        self.UserURL = 'https://api.github.com/users/{}'.format(self.Username)        

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
        print (UserDataFromGithub)
        self.UserData = extract_data(DataNeeded, UserDataFromGithub)
                
        save_json('Github-stats' , self.UserData)

        return json.dumps(self.UserData, indent= True)


aminzayer = User('aminzayer')
data = aminzayer.get_user_stats()
print(data)
