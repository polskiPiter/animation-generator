# Import modułów:
from os.path import join
from animations import generate_checkered_pattern

# Funkcja do generowania tablicy pikseli:
def generate_pixel_array(resolution):
    pixel = {"Red": 0, "Green": 0, "Blue": 0}
    pixel_array = [[pixel.copy() for _ in range(resolution[0])] for _ in range(resolution[1])]

    return pixel_array

# Funkcja do generowania plików w formacie ".ppm":
def create_ppm_file(resolution, pixel_array, file_path, frame_number):
    file_header = "P3"
    file_comment = f"# Frame {frame_number}."
    max_value_for_colors = 255

    file_content = f"{file_header}\n{file_comment}\n{resolution[0]} {resolution[1]}\n{max_value_for_colors}"

    for h in range(resolution[1]):
        for w in range(resolution[0]):
            file_content += f"\n{pixel_array[h][w]["Red"]} {pixel_array[h][w]["Green"]} {pixel_array[h][w]["Blue"]}"

    path = join(file_path, f"Frame {frame_number}.ppm")

    with open(path, "w") as ppm_file:
        ppm_file.write(file_content)

# Główna funkcja programu:
def main():
    file_path = r"D:\Kodowanie\Projekty\Python\animation-generator\data\frames\ppm files"
    resolution = (1920, 1080)
    pixel_array = generate_pixel_array(resolution)
    
    number_of_frames = 10
    frame_number = 1

    while frame_number <= number_of_frames:
        generate_checkered_pattern(resolution, pixel_array)
        create_ppm_file(resolution, pixel_array, file_path, frame_number)
        frame_number += 1

# Uruchomienie programu:
if __name__ == "__main__":
    main()