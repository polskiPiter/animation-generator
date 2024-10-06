# Import modułu z funkcjami do generowania grafiki (graphics_ppm):
from graphics_ppm import generate_checkered_pattern

# Funkcja do generowania tablicy (listy podlist) z pikselami:
def generate_pixel_array(image_resolution):
    pixel = {"Red": 0, "Green": 0, "Blue": 0}
    pixel_array = []

    for i in range(image_resolution[1]):
        pixel_array.append([])
        for _ in range(image_resolution[0]):
            pixel_array[i].append(pixel.copy())

    return pixel_array

# Funkcja do zapisywania plików w formacie ".ppm":
def save_ppm_file(path_to_file, image_resolution):
    header = "P3"
    comment = "# Testowy obraz 3 (dwukolorowa Szachownica)."
    max_value_for_colors = 255

    pixel_array = generate_pixel_array(image_resolution)
    array_with_graphics = generate_checkered_pattern(pixel_array, image_resolution)

    file_content = f"{header}\n{comment}\n{image_resolution[0]} {image_resolution[1]}\n{max_value_for_colors}"

    for i in range(image_resolution[1]):
        for j in range(image_resolution[0]):
            file_content += f"\n{array_with_graphics[i][j]["Red"]} {array_with_graphics[i][j]["Green"]} {array_with_graphics[i][j]["Blue"]}"

    with open(path_to_file, "w") as ppm_file:
        ppm_file.write(file_content)

# Główna funkcja programu:
def main():
    path = r"D:\Kodowanie\Projekty\Python\animation-generator\data\Testowy obraz 3.ppm"
    resolution = (1920, 1080)

    save_ppm_file(path, resolution)

# Uruchomienie programu:
if __name__ == "__main__":
    main()