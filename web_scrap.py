import requests
from bs4 import BeautifulSoup as BS
import os

# input for the website URL
url = input("Enter a Website URL: ")
page = requests.get(url)

# Status code check
if page.status_code == 200:
    web_extract = BS(page.content, 'html.parser')

    # HTML extract
    html_code = web_extract.prettify()

    # CSS extract
    css_code = ''
    css_styles = web_extract.find_all('style')
    for tags in css_styles:
        css_code += tags.get_text()

    # JavaScript extract
    js_code = ''
    script_tags = web_extract.find_all('script')
    for tag in script_tags:
        if tag.has_attr('src'):
            js_ex_url = tag['src']
            js_external = requests.get(js_ex_url)
            if js_external.status_code == 200:
                js_code += js_external.text
        else:
            js_code += tag.get_text()

    # Get folder name input
    folder_name = input("Enter Your Folder Name:")

    # Create the folder
    os.makedirs(f"{folder_name}")

    # Write HTML code to file
    with open(f"./{folder_name}/HTML_Code.txt", "w",encoding='utf-8') as file:
        file.write(f"Extracting HTML Data:\n\n{html_code}")

    # Write CSS code to file
    with open(f"./{folder_name}/CSS_Code.txt", "w",encoding='utf-8') as file:
        file.write(f"Extracting CSS Data:\n\n{css_code}")

    # Write JavaScript code to file
    with open(f"./{folder_name}/JavaScript_Code.txt", "w",encoding='utf-8') as file:
        file.write(f"Extracting JavaScript Data:\n\n{js_code}")

else:
    print(f"Failed to retrieve the webpage. Status code: {page.status_code}")
