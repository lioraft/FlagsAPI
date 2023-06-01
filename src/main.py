from flask import *
import json

from src.get_by_request import getAllImagesOfCategory

app = Flask(__name__)
# Ngrok link:
# https://827d-93-172-146-139.ngrok-free.app/


# Main page
@app.route('/', methods=['GET'])
def main_page():
    data = {'Page': 'Main', 'Message': 'Welcome to flags and logos API!'}
    return json.dumps(data)


# Request page for all flags in a certain category
@app.route('/get_category/', methods=['GET'])
def request_category_page():
    user_query = str(request.args.get('all')) # /user/?all_category=CATEGORY_NAME
    images = getAllImagesOfCategory(user_query) # get all images of category
    data = {'Message': f'Got user request for {user_query} category successfully', 'Content': images}
    return json.dumps(data) # return the images as json

# Request page for all flags in a certain category
@app.route('/get_image/', methods=['GET'])
def request_image_page():
    # get category and image from the URL path
    user_query_for_category = str(request.args.get('category'))
    user_query_for_image = str(request.args.get('image'))
    # /user/?category=CATEGORY_NAME&image=IMAGE_NAME
    image = f"https://raw.githubusercontent.com/lioraft/FlagsAndLogosAPI/main/resources/{user_query_for_category}/{user_query_for_image}.png" # get the image
    data = { 'Message': f'Got user request for {user_query_for_image} of {user_query_for_category} category successfully', 'Content': image}
    return json.dumps(data) # return the image as json

if __name__ == '__main__':
    app.run(port=5555)