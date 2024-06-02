def main():
    header = "P3"
    comment = "# Testowy obraz (tło o kolorze turkusowym)."
    resolution = (1920, 1080)
    path_to_file = r"D:\Kodowanie\Projekty\Python\animation-generator\data\Testowy obraz.ppm"

    content = f"{header}\n{comment}\n{resolution[0]} {resolution[1]}\n255"

    for _ in range(resolution[0] * resolution[1]):
        content += "\n64 224 208"
    
    ppm_file = open(path_to_file, "w")
    ppm_file.write(content)
    ppm_file.close()

if __name__ == "__main__":
    main()