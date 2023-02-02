import requests
import time

# api base url
API_URL = "https://challenge.crossmint.io/api/"

# candidateId
CANDIDATE_ID = "95ccae45-102c-4748-98f2-b06b2b3aa93e"

# get goal grid
def get_goal():
    r = requests.get(url = f"{API_URL}/map/{CANDIDATE_ID}/goal")
    json = r.json()
    goal = json["goal"]
    return goal

# make request in order of given array
def draw(goal):
    for i in range(len(goal)):
        for j in range(len(goal[i])):

            data = {
                "candidateId": CANDIDATE_ID,
                "row": i,
                "column": j
            }
            
            shape = goal[i][j]

            if shape == 'POLYANET':
                endpoint = 'polyanets'
            elif 'COMETH' in shape:
                # extract direction of string 
                data['direction'] = shape.split('_COMETH')[0].lower()
                endpoint = 'comeths'
            elif 'SOLOON' in shape:
                # extract color of string
                data['color'] = shape.split('_SOLOON')[0].lower()
                endpoint = 'soloons'
            else:
                # don't make a request if shape is 'SPACE'
                continue
            
            print(f"modyfing row: {i} column: {j}")

            # makes request with given data
            r = requests.post(url = f"{API_URL}/{endpoint}", data = data)

            print("Response: ")
            print(r.json())

            # wait one sec bewteen requests to avoid "Too many requests"
            print("waiting 1 second...")
            time.sleep(1)

goal = get_goal()
draw(goal)

