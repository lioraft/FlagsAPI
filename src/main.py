from flask import Flask
from flask import request
import json
import requests


app = Flask(__name__)

# Main page
@app.route('/', methods=['GET'])
def main_page():
    data = {'Page': 'Main', 'Message': 'Welcome to flags and logos API!'}
    return json.dumps(data)


# Request page for all flags in a certain category
@app.route('/get_category/', methods=['GET'])
def request_category_page():
    user_query = str(request.args.get('all')) # /get_category/?all=CATEGORY_NAME
    # get the flags of requested category
    response = requests.get(f"https://api.github.com/repos/lioraft/FlagsAPI/contents/resources/{user_query}")
    # check if response is successful
    if response.status_code == 200:
        contents = response.json() # get the contents of the response
        png_files = [content["name"] for content in contents if content["name"].lower().endswith(".png")] # get the png files
        url = f"https://raw.githubusercontent.com/lioraft/FlagsAPI/main/resources/{user_query}/"  # add prefix of url of raw github content
        modified_files = [url + file for file in png_files]
    else:
        modified_files = (f"Error: {response.status_code}")
    data = {'Message': f'Got user request for {user_query} category successfully', 'Content': modified_files}
    return json.dumps(data) # return the images as json

# Request page for a specific flag
@app.route('/get_image/', methods=['GET'])
def request_image_page():
    # get category and image from the URL path
    user_query_for_category = str(request.args.get('category'))
    user_query_for_image = str(request.args.get('image'))
    # /get_image/?category=CATEGORY_NAME&image=IMAGE_NAME
    image = f"https://raw.githubusercontent.com/lioraft/FlagsAPI/main/resources/{user_query_for_category}/{user_query_for_image}.png" # get the image
    image_exists = requests.head(image) # check if image exists
    # if image doesn't exist, put error message instead
    if (image_exists.status_code != 200):
        image = f"Error: {image_exists.status_code}"
    data = { 'Message': f'Got user request for {user_query_for_image} of {user_query_for_category} category successfully', 'Content': image}
    return json.dumps(data) # return the image as json

if __name__ == '__main__':
    app.run(port=5555)