# Flags API
This is an API I created for flags as PNG files. It includes both international flags and Israeli flags.

How to use:

The response will be a JSON that includes the URL of requested images.

In order to get all the images of category, use the following query: http://lioraft.pythonanywhere.com/get_category/?all={category}.
The content will be a list of all the URLs of PNG images in that category.

In order to get a certain image of category, use the following query: http://lioraft.pythonanywhere.com/get_image/?category={category}&image={image}.
The content will be the URL of the requested PNG image.

Current categories available:
- Countries: get the flag of the country by its alpha2 code.
- Pride: get pride flags by the sexual orientation/gender identity they represent.
- Nautical: get nautical flags by their alphabetical letter.
- Organizations: get international organization flags by their initials.
- US States: get  the flag of the state by its alpha2 code.

Israeli related:
to access Israeli flags, the category should be israeli/{sub-category}. The flags are fully named:
- Governmental
- Coat of Arms
- Historical
- Municipalities
- Organizations
- Political Parties
- Security Forces (IDF, Police, Fire and Rescue, etc)
- Universities
