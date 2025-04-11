import os
import requests

# Save folder
save_directory = "C:/Users/henry/Projects/cpsc386-cv-project/dataset"

# Mushroom species
species = ["Amanita_muscaria", "Coprinus_comatus", "Laetiporus_sulphureus", "Pleurotus_ostreatus"]

# Pexels API Key
api_key = "K3NTmMrcS5xtZfec41AhvL6SsA9m3FfUx5mssPwMbSGTUCdTDidZV20N"

# Pexels API base URL
base_url = "https://api.pexels.com/v1/search?"

# Number of images to download per sepcies
images_per_species = 100

# Function to download images for each species
def download_images(species_name, num_images=images_per_species):
    for i in range(num_images):
        url = f"{base_url}query={species_name}&per_page=1&page={i+1}"
        headers = {"Authorization": api_key}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            if data['photos']:
                image_url = data['photos'][0]['src']['original']
                img_data = requests.get(image_url).content
                image_filename = os.path.join(save_directory, f"{species_name}_{i}.jpg")
                with open(image_filename, 'wb') as f:
                    f.write(img_data)
                print(f"Downloaded: {image_filename}")
            else:
                print(f"No image found for {species_name} on page {i+1}")
        else:
            print(f"Error: Unable to fetch images for {species_name}. Status Code: {response.status_code}")

# Loop through each species and download images
for species_name in species:
    download_images(species_name)
