import requests
import time
  
# api-endpoint
API_ENDPOINT = "https://challenge.crossmint.io/api/polyanets"

# candidateId
CANDIDATE_ID = "95ccae45-102c-4748-98f2-b06b2b3aa93e"

# function to make_cross 
# (it also makes delete request in case there were prior polyanets in canvas)
# n defines the cross length, which is the length from center
# n = 2 would be:
# x x
#  x
# x x
def make_cross(n):
    # since it's a 11x11 canvas, max n should be 6
    if  n < 1 or n > 6 :
        print("Error: n should be between 1 and 6")
        return
    for i in range(11):
        for j in range(11):

            data = {
                "candidateId": CANDIDATE_ID,
                "row": i,
                "column": j
            }

            print(f"modyfing row: {i} column: {j}")

            # verifies it is on the cross of a 11x11 grid and makes the space acording to n
            if (i > (5 - n)) and (i < (5 + n)) and (j == i or j == (10 - i)):
                r = requests.post(url = API_ENDPOINT, data = data)
            else:
                r = requests.delete(url = API_ENDPOINT, data = data)

            print("Response: ")
            print(r.json())

            # wait one sec bewteen requests to avoid "Too many requests"
            print("waiting 1 second...")
            time.sleep(1)

make_cross(4)


