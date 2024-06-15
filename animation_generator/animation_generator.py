def generate_pixel_array(image_resolution):
    pixel = {"Red": 0, "Green": 0, "Blue": 0}
    pixel_array = []

    for i in range(image_resolution[1]):
        pixel_array.append([])
        for _ in range(image_resolution[0]):
            pixel_array[i].append(pixel.copy())

    # Flaga Niemiec:
    for i in range(image_resolution[1]):
        for j in range(image_resolution[0]):
            if i >= 0 and i < 360:
                pixel_array[i][j]["Red"] = pixel_array[i][j]["Blue"] = pixel_array[i][j]["Green"] = 15
            elif i >= 360 and i < 720:
                pixel_array[i][j]["Red"] = 255
            else:
                pixel_array[i][j]["Red"] = pixel_array[i][j]["Green"] = 255

    return pixel_array

def save_ppm_file(path_to_file, image_resolution):
    header = "P3"
    comment = "# Testowy obraz 2 (Flaga Niemiec)."
    max_value_for_colors = 255
    pixel_array = generate_pixel_array(image_resolution)

    file_content = f"{header}\n{comment}\n{image_resolution[0]} {image_resolution[1]}\n{max_value_for_colors}"

    for i in range(image_resolution[1]):
        for j in range(image_resolution[0]):
            file_content += f"\n{pixel_array[i][j]["Red"]} {pixel_array[i][j]["Green"]} {pixel_array[i][j]["Blue"]}"

    with open(path_to_file, "w") as ppm_file:
        ppm_file.write(file_content)

# Główna funkcja programu:
def main():
    path = r"D:\Kodowanie\Projekty\Python\animation-generator\data\Testowy obraz 2.ppm"
    resolution = (1920, 1080)

    save_ppm_file(path, resolution)

# Uruchomienie programu:
if __name__ == "__main__":
    main()