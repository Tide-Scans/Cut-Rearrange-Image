from PIL import Image
import os

# Input and output folders
input_folder = "input"
output_folder = "output"

# Ensure the output folder exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# List all files in the input folder
input_files = os.listdir(input_folder)

# Loop through each input file
for input_file in input_files:
    # Load the image
    input_image = Image.open(os.path.join(input_folder, input_file))

    # Calculate the dimensions of each piece
    width, height = input_image.size
    piece_width = width // 4
    piece_height = height // 4

    pieces = []

# Cut the image into pieces
for i in range(4):
    for j in range(4):
        left = j * piece_width
        upper = i * piece_height
        right = (j + 1) * piece_width
        lower = (i + 1) * piece_height
        piece = input_image.crop((left, upper, right, lower))
        pieces.append(piece)

# Rearrange the pieces
rearranged_pieces = [
    pieces[0], pieces[4], pieces[8], pieces[12],
    pieces[1], pieces[5], pieces[9], pieces[13],
    pieces[2], pieces[6], pieces[10], pieces[14],
    pieces[3], pieces[7], pieces[11], pieces[15]
]

# Create a new image to hold the rearranged pieces
output_image = Image.new("RGB", (width, height))

# Paste the rearranged pieces onto the new image
for i in range(4):
    for j in range(4):
        output_image.paste(rearranged_pieces[i * 4 + j], (j * piece_width, i * piece_height))

    # Save the rearranged image to the output folder
    output_file = os.path.splitext(input_file)[0] + "_rearranged.jpg"
    output_path = os.path.join(output_folder, output_file)
    output_image.save(output_path)

print("Processing complete!")
