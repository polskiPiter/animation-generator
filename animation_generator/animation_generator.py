# Funkcja do generowania grafiki (dwukolorowa szachownica):
def generate_graphics(pixel_array, image_resolution):
    # Zmienne i kolekcje:
    rectangle_size = (120, 120)
    layouts_of_white_rectangles = [[], []]
    layouts_of_black_rectangles = [[], []]
    white_rectangles = []
    black_rectangles = []

    # Obliczenie przesunięcia każdego prostokąta:
    offset_of_rectangle = (rectangle_size[0] * 2, rectangle_size[1] * 2)
    
    # Obliczenie liczby prostokątów w każdym rzędzie i w każdej kolumnie:
    number_of_rectangles_in_rows_and_columns = (
        image_resolution[0] // rectangle_size[0], 
        image_resolution[1] // rectangle_size[1]
        )
    
    # Obliczenie liczby białych i czarnych prostokątów dla każdego układu:
    for number_of_rectangles in number_of_rectangles_in_rows_and_columns:
        if number_of_rectangles % 2 == 0:
            layouts_of_white_rectangles[0].append(number_of_rectangles // 2)
            layouts_of_white_rectangles[1].append(number_of_rectangles // 2)
            layouts_of_black_rectangles[0].append(number_of_rectangles // 2)
            layouts_of_black_rectangles[1].append(number_of_rectangles // 2)
        else:
            layouts_of_white_rectangles[0].append(int(number_of_rectangles / 2 + 0.5))
            layouts_of_white_rectangles[1].append(int(number_of_rectangles / 2 - 0.5))
            layouts_of_black_rectangles[0].append(int(number_of_rectangles / 2 + 0.5))
            layouts_of_black_rectangles[1].append(int(number_of_rectangles / 2 - 0.5))

    # Obliczenie przedziałów pikseli dla każdego białego i czarnego prostokąta:
    for rectangle_in_column in range(layouts_of_white_rectangles[0][1]):
        for rectangle_in_row in range(layouts_of_white_rectangles[0][0]):
            white_rectangles.append(
                (
                    0 + offset_of_rectangle[0] * rectangle_in_row, 
                    0 + offset_of_rectangle[1] * rectangle_in_column, 
                    rectangle_size[0] + offset_of_rectangle[0] * rectangle_in_row, 
                    rectangle_size[1] + offset_of_rectangle[1] * rectangle_in_column
                    )
                )
    
    for rectangle_in_column in range(layouts_of_white_rectangles[1][1]):
        for rectangle_in_row in range(layouts_of_white_rectangles[1][0]):
            white_rectangles.append(
                (
                    rectangle_size[0] + offset_of_rectangle[0] * rectangle_in_row, 
                    rectangle_size[1] + offset_of_rectangle[1] * rectangle_in_column, 
                    rectangle_size[0] * 2 + offset_of_rectangle[0] * rectangle_in_row, 
                    rectangle_size[1] * 2 + offset_of_rectangle[1] * rectangle_in_column
                    )
                )
            
    for rectangle_in_column in range(layouts_of_black_rectangles[0][1]):
        for rectangle_in_row in range(layouts_of_black_rectangles[0][0]):
            black_rectangles.append(
                (
                    rectangle_size[0] + offset_of_rectangle[0] * rectangle_in_row, 
                    0 + offset_of_rectangle[1] * rectangle_in_column, 
                    rectangle_size[0] * 2 + offset_of_rectangle[0] * rectangle_in_row, 
                    rectangle_size[1] + offset_of_rectangle[1] * rectangle_in_column
                    )
                )
    
    for rectangle_in_column in range(layouts_of_black_rectangles[1][1]):
        for rectangle_in_row in range(layouts_of_black_rectangles[1][0]):
            black_rectangles.append(
                (
                    0 + offset_of_rectangle[0] * rectangle_in_row, 
                    rectangle_size[1] + offset_of_rectangle[1] * rectangle_in_column, 
                    rectangle_size[0] + offset_of_rectangle[0] * rectangle_in_row, 
                    rectangle_size[1] * 2 + offset_of_rectangle[1] * rectangle_in_column
                    )
                )
    
    # Narysowanie białych i czarnych prostokątów przy pomocy przedziałów pikseli: 
    for rectangle in white_rectangles:
        for i in range(rectangle[1], rectangle[3]):
            for j in range(rectangle[0], rectangle[2]):
                pixel_array[i][j]["Red"] = pixel_array[i][j]["Green"] = pixel_array[i][j]["Blue"] =  255

    for rectangle in black_rectangles:
        for i in range(rectangle[1], rectangle[3]):
            for j in range(rectangle[0], rectangle[2]):
                pixel_array[i][j]["Red"] = pixel_array[i][j]["Green"] = pixel_array[i][j]["Blue"] =  25

    # Zwrócenie zmodyfikowanej tablicy (listy podlist) pikseli:
    return pixel_array

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
    pixel_array = generate_graphics(generate_pixel_array(image_resolution), image_resolution)

    file_content = f"{header}\n{comment}\n{image_resolution[0]} {image_resolution[1]}\n{max_value_for_colors}"

    for i in range(image_resolution[1]):
        for j in range(image_resolution[0]):
            file_content += f"\n{pixel_array[i][j]["Red"]} {pixel_array[i][j]["Green"]} {pixel_array[i][j]["Blue"]}"

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