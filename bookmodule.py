import requests
import os
from PIL import Image

def book1():
    # Create a directory to save the images
    save_dir = 'ebook1_images'
    os.makedirs(save_dir, exist_ok=True)

    # Base URL for the images
    base_url = 'https://ebook.lib.ku.ac.th/ebook27/ebook/2014RG0083/files/mobile/{}.jpg'

    # List to hold images for PDF
    image_list = []

    # Loop to download images from page 1 to 219
    for page_number in range(1, 220):  # 220 because the range is exclusive at the end
        url = base_url.format(page_number)
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status() # Raise an exception for 4xx/5xx status codes
            file_path = os.path.join(save_dir, f'page_{page_number}.jpg')
            with open(file_path, 'wb') as file:
                file.write(response.content)
            print(f'Downloaded page {page_number}')

            # Open the image and convert to RGB (required for PDF)
            img = Image.open(file_path).convert('RGB')
            image_list.append(img)

        except requests.RequestException as e:
            print(f'Failed to download page {page_number}: {e}')

    # Save all images as a single PDF
    if image_list:
        pdf_path = 'OrgChem1.pdf'
        image_list[0].save(pdf_path, save_all=True, append_images=image_list[1:])
        print(f'PDF created: {pdf_path}')

    print('Download and PDF OrgChem1 completed.') 




def book2():
    # Create a directory to save the images
    save_dir = 'ebook2_images'
    os.makedirs(save_dir, exist_ok=True)

    # Base URL for the images
    base_url = 'https://ebook.lib.ku.ac.th/ebook27/ebook/2014RG0082/files/mobile/{}.jpg'

    # List to hold images for PDF
    image_list = []

    # Loop to download images from page 1 to 175
    for page_number in range(1, 176):  # 176 because the range is exclusive at the end
        url = base_url.format(page_number)
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status() # Raise an exception for 4xx/5xx status codes
            file_path = os.path.join(save_dir, f'page_{page_number}.jpg')
            with open(file_path, 'wb') as file:
                file.write(response.content)
            print(f'Downloaded page {page_number}')

            # Open the image and convert to RGB (required for PDF)
            img = Image.open(file_path).convert('RGB')
            image_list.append(img)

        except requests.RequestException as e:
            print(f'Failed to download page {page_number}: {e}')

    # Save all images as a single PDF
    if image_list:
        pdf_path = 'OrgChem2.pdf'
        image_list[0].save(pdf_path, save_all=True, append_images=image_list[1:])
        print(f'PDF created: {pdf_path}')

    print('Download and PDF OrgChem2 completed.') 