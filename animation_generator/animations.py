# Funkcja do generowania grafiki (Dwukolorowa szachownica):
def generate_checkered_pattern(resolution, pixel_array):
    # Zmienne i kolekcje:
    rectangle_size = (120, 120)
    layouts_of_white_rectangles = [[], []]
    layouts_of_black_rectangles = [[], []]
    white_rectangles = []
    black_rectangles = []

    # Obliczenie przesunięcia każdego kolejnego prostokąta:
    offset_of_rectangle = (rectangle_size[0] * 2, rectangle_size[1] * 2)
    
    # Obliczenie liczby prostokątów w każdym rzędzie i w każdej kolumnie:
    number_of_rectangles_in_rows_and_columns = (
        resolution[0] // rectangle_size[0], 
        resolution[1] // rectangle_size[1]
        )
    
    # Obliczenie liczby białych i czarnych prostokątów dla każdego układu:
    for number in number_of_rectangles_in_rows_and_columns:
        if number % 2 == 0:
            layouts_of_white_rectangles[0].append(number // 2)
            layouts_of_white_rectangles[1].append(number // 2)
            layouts_of_black_rectangles[0].append(number // 2)
            layouts_of_black_rectangles[1].append(number // 2)
        else:
            layouts_of_white_rectangles[0].append(int(number / 2 + 0.5))
            layouts_of_white_rectangles[1].append(int(number / 2 - 0.5))
            layouts_of_black_rectangles[0].append(int(number / 2 + 0.5))
            layouts_of_black_rectangles[1].append(int(number / 2 - 0.5))

    # Obliczenie przedziałów liczboywch pikseli dla każdego białego i czarnego prostokąta:
    for rectangle_number_in_column in range(layouts_of_white_rectangles[0][1]):
        for rectangle_number_in_row in range(layouts_of_white_rectangles[0][0]):
            white_rectangles.append(
                (
                    0 + offset_of_rectangle[0] * rectangle_number_in_row, 
                    0 + offset_of_rectangle[1] * rectangle_number_in_column, 
                    rectangle_size[0] + offset_of_rectangle[0] * rectangle_number_in_row, 
                    rectangle_size[1] + offset_of_rectangle[1] * rectangle_number_in_column
                    )
                )
    
    for rectangle_number_in_column in range(layouts_of_white_rectangles[1][1]):
        for rectangle_number_in_row in range(layouts_of_white_rectangles[1][0]):
            white_rectangles.append(
                (
                    rectangle_size[0] + offset_of_rectangle[0] * rectangle_number_in_row, 
                    rectangle_size[1] + offset_of_rectangle[1] * rectangle_number_in_column, 
                    rectangle_size[0] * 2 + offset_of_rectangle[0] * rectangle_number_in_row, 
                    rectangle_size[1] * 2 + offset_of_rectangle[1] * rectangle_number_in_column
                    )
                )
            
    for rectangle_number_in_column in range(layouts_of_black_rectangles[0][1]):
        for rectangle_number_in_row in range(layouts_of_black_rectangles[0][0]):
            black_rectangles.append(
                (
                    rectangle_size[0] + offset_of_rectangle[0] * rectangle_number_in_row, 
                    0 + offset_of_rectangle[1] * rectangle_number_in_column, 
                    rectangle_size[0] * 2 + offset_of_rectangle[0] * rectangle_number_in_row, 
                    rectangle_size[1] + offset_of_rectangle[1] * rectangle_number_in_column
                    )
                )
    
    for rectangle_number_in_column in range(layouts_of_black_rectangles[1][1]):
        for rectangle_number_in_row in range(layouts_of_black_rectangles[1][0]):
            black_rectangles.append(
                (
                    0 + offset_of_rectangle[0] * rectangle_number_in_row, 
                    rectangle_size[1] + offset_of_rectangle[1] * rectangle_number_in_column, 
                    rectangle_size[0] + offset_of_rectangle[0] * rectangle_number_in_row, 
                    rectangle_size[1] * 2 + offset_of_rectangle[1] * rectangle_number_in_column
                    )
                )
    
    # Narysowanie białych i czarnych prostokątów przy pomocy przedziałów liczbowych pikseli: 
    for rectangle in white_rectangles:
        for h in range(rectangle[1], rectangle[3]):
            for w in range(rectangle[0], rectangle[2]):
                pixel_array[h][w]["Red"] = pixel_array[h][w]["Green"] = pixel_array[h][w]["Blue"] =  255

    for rectangle in black_rectangles:
        for h in range(rectangle[1], rectangle[3]):
            for w in range(rectangle[0], rectangle[2]):
                pixel_array[h][w]["Red"] = pixel_array[h][w]["Green"] = pixel_array[h][w]["Blue"] =  25