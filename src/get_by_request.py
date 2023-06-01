import requests

# my resources repo
repoURL = f"https://api.github.com/repos/lioraft/FlagsAndLogosAPI/contents/resources"

# get all flags and logos of certain category
def getAllImagesOfCategory(category):
    # get the flags of requested category
    response = requests.get(f"{repoURL}/{category}")
    # check if response is successful
    if response.status_code == 200:
        contents = response.json() # get the contents of the response
        png_files = [content["name"] for content in contents if content["name"].lower().endswith(".png")] # get the png files
        return png_files # return the png files
    else:
        return (f"Error: {response.status_code}") # if error occurred, print the error code

