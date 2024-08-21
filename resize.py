from PIL import Image
import os

def resize_image(image_path, output_path, target_size):
    with Image.open(image_path) as img:
        # Calculate aspect ratio
        aspect = img.width / img.height
        
        if img.width > img.height:
            # Landscape orientation
            new_width = target_size
            new_height = int(target_size / aspect)
        else:
            # Portrait orientation
            new_height = target_size
            new_width = int(target_size * aspect)
        
        # Resize image
        img_resized = img.resize((new_width, new_height), Image.LANCZOS)
        
        # Create new image with padding
        new_img = Image.new("RGB", (target_size, target_size), color="black")
        
        # Paste resized image onto center of new image
        paste_x = (target_size - new_width) // 2
        paste_y = (target_size - new_height) // 2
        new_img.paste(img_resized, (paste_x, paste_y))
        
        # Save the result
        new_img.save(output_path)

# Example usage
target_size = 640  # or 416, 512, etc.
input_folder = "rickshaw_google"
output_folder = "rickshaw_new"

for filename in os.listdir(input_folder):
    if filename.endswith((".jpg", ".png", ".jpeg")):  # Add or remove extensions as needed
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)
        resize_image(input_path, output_path, target_size)