import dan067
m = ([2, 0], [1, 0])
n = ([1, 2, 0],[0, 1, 3], [0, 3, 1])

# hasil22 = dan067.invers22(m)  pilih salah satu matriks
hasil22 = dan067.invers33(n)
if hasil22:
    print("\nInvers matriks :")
    dan067.tampilkan(hasil22)
else:
    print("Matriks tidak memiliki invers")
