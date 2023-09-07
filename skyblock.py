
import requests
import time



def skyblockMates(profile):
    return uuidToUser(profile)
    
        
        
def skyblockProfile(player_name):
    try:
        player_uuid = requests.get(url = 'https://api.mojang.com/users/profiles/minecraft/' + player_name).json()['id']
        params = {
                "key": "031a6abf-cc50-4047-bf9a-b03d54978144",
                "uuid": player_uuid
            }

        data = requests.get(
            url = "https://api.hypixel.net/skyblock/profiles", params=params).json()
        return data
    except KeyError:
        print('Invalid Username')


def uuidToUser(data):
    try:
        profiles = []
        
        for num in range(len(data['profiles'])): #for each profile
            
            uuids = list((data['profiles'][num]['members']).keys())
            #print("\n")
            #print("On your {number} profile, the members on your skyblock island are:".format(number = num+1))
            nameList = "Profile " + str(num + 1) + " " + data['profiles'][num]['cute_name'] + ": "
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

def getPlayerMoney(file, profileNum):
    try:
        profileNum = int(profileNum)
        return file['profiles'][profileNum]['banking']['balance']
    except KeyError:
        return "No banking information"
    

    
