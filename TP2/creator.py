t = ["3; 7; 2; 8; 5", "1; 2; 3; 4; 5; 6", "8; 15; 3; 7", "2; 2; 2", "1; 2; 3; 4; 5; 6; 7; 8", "20; 30; 2; 10", "1; 2; 3; 4; 5; 6; 7", "1; 2; 5; 10; 7", "1; 5; 10; 20", "1; 5; 10; 6; 2; 50", "1; 1; 1; 1; 1; 1", "5; 5; 5; 5", "10; 20; 30; 40", "2; 4; 6; 8; 10", "1; 3; 5; 7; 9", "1; 2; 4; 8; 16", "3; 6; 9; 12", "7; 14; 21; 28", "2; 3; 5; 7; 11", "1; 4; 9; 16; 25", "1; 2; 3; 4; 5; 6; 7; 8; 9; 10", "10; 9; 8; 7; 6; 5; 4; 3; 2; 1", "1; 1; 1; 1; 1; 1; 1; 1; 1; 1", "2; 4; 6; 8; 10; 12; 14; 16; 18; 20", "5; 10; 15; 20; 25; 30; 35; 40; 45; 50", "3; 6; 9; 12; 15; 18; 21; 24; 27; 30", "1; 3; 5; 7; 9; 11; 13; 15; 17; 19", "2; 3; 5; 7; 11; 13; 17; 19; 23; 29", "1; 2; 4; 8; 16; 32; 64; 128; 256; 512", "10; 20; 30; 40; 50; 60; 70; 80; 90; 100"]

for x in range(2, 32):
    with open(f"{x}.txt", "w") as file:
        file.write("# Los valores de las monedas de la fila se muestran tal cual su orden correspondiente; separados por ;\n")
        file.write(t[x-2])
        file.close()