
import requests
import time



def skyblockMates(profile):
    print(profile.keys())
    if (profile == None or profile['profile'] == None):
            print("No profile available/Error loading profile")
            return
        
    return uuidToUser(profile)
    
        
        
def skyblockProfile(player_name):
    try:
        player_uuid = requests.get(url = 'https://api.mojang.com/users/profiles/minecraft/' + player_name).json()['id']

        params = {
                "key": "18c9cd38-51eb-4b40-a4d5-7bb9510dd9de",
                "profile": player_uuid
            }

        data = requests.get(
            url = "https://api.hypixel.net/skyblock/profile", params=params).json()
        return data
    except KeyError:
        print('Invalid Username')


def uuidToUser(data):
    try:
        profiles = []
        
        for num in range(len(data['profile'])): #for each profile
            
            uuids = list((data['profile'][num]['members']).keys())
            #print("\n")
            #print("On your {number} profile, the members on your skyblock island are:".format(number = num+1))
            nameList = "Profile " + (str)(num+1) + ": "
            for uuid in uuids: #for each player in profile
                result = requests.get( url = 'https://api.mojang.com/user/profile/' + uuid).json()
                #print(result['name'], end=" ")
                nameList += (result['name']) + " "
                
                
                
            profiles.append(nameList)
        return profiles
    except KeyError:
        nameList = ["Error loading user, Loading Too Fast"]
        profiles.append(nameList)
        return profiles

def getPlayerMoney(file):
    print(file['profiles'][0].keys())
