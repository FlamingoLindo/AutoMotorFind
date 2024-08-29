import os

def get_image_paths(directory, extensions=None):
    if extensions is None:
        extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']

    image_paths = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            if any(file.lower().endswith(ext) for ext in extensions):
                full_path = os.path.abspath(os.path.join(root, file))
                image_paths.append(full_path)

    return image_paths

# Example usage:
directory_path = r'Images\Partes'
images = get_image_paths(directory_path)

# Join all paths into a single string separated by spaces
all_paths_single_line = ','.join(images)

print(all_paths_single_line)
