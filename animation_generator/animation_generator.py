def save_ppm_file(image_resolution, path_to_file):
    header = "P3"
    comment = "# Testowy obraz (tło o kolorze turkusowym)."
    max_value_for_color = 255

    content = f"{header}\n{comment}\n{image_resolution[0]} {image_resolution[1]}\n{max_value_for_color}"

    for _ in range(image_resolution[0] * image_resolution[1]):
        content += "\n64 224 208"

    # Nowoczesna metoda obsługi plików w Python'ie:
    with open(path_to_file, "w") as ppm_file:
        ppm_file.write(content)

def main():
    resolution = (1920, 1080)
    path = r"D:\Kodowanie\Projekty\Python\animation-generator\data\Testowy obraz.ppm"

    save_ppm_file(resolution, path)

    # Klasyczna metoda obsługi plików w Python'ie:
    #ppm_file = open(path_to_file, "w")
    #ppm_file.write(content)
    #ppm_file.close()

if __name__ == "__main__":
    main()