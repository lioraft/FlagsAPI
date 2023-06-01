# Flags, Logos, and Symbols API
This is an API I created for flags, logos, banners, and symbols as PNG files.
I know there are a lot of similar APIs out there. why use this one?
- Very simple to use. two simple queries and you get the images you need.
- I keep modifying this API based on my needs. 
- Very useful if you're an Israeli: I try to include Israeli-related images.

How to use:

1. Get all the images of category:
Simple following query:
https://827d-93-172-146-139.ngrok-free.app/get_category/?all={category}.
You will get JSON in which "Content" is a list of all the URLs of PNG images in that category.

2. Get a certain image of category:
following query:
https://827d-93-172-146-139.ngrok-free.app/get_image/?category={category}&image={image}.
You will get JSON in which "Content" is the URL of the PNG image.

Current categories available:
- Countries: get the flag of the country by its alpha2 code.
- Pride: get pride flags by the sexual orientation/gender identity they represent.
- Nautical: get nautical flags by their alphabetical letter.
- Organizations: get international organization flags by their initials.
- US States: get  the flag of the state by its alpha2 code.

Israeli related:
- Israeli Coat of Arms: get the coat of arms of Israeli cities.
