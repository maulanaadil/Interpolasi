# newton gregory maju

# membuat function temporary
def u_cal(u, n):

    temp = u
    for i in range(1, n):
        temp = temp * (u - i)
    return temp

# membuat function faktorial
def fact(n):
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f


# memasukkan x yang ada di tabel soal
n = 4
x = [ 5, 10, 15, 20]

# memasukkan y yang ada di tabel soal
y = [[0 for i in range(n)]
     for j in range(n)]
y[0][0] = 40
y[1][0] = 30
y[2][0] = 25
y[3][0] = 40

# menghitung menggunakan newton gregory maju pada tabel
# tabel
for i in range(1, n):
    for j in range(n - i):
        y[j][i] = y[j + 1][i - 1] - y[j][i - 1]

# menampilkan hasil dari tabel yang berbeda
for i in range(n):
    print(x[i], end = "\t")
    for j in range(n - i):
        print(y[i][j], end = "\t")
    print("")

# memasukan value atau nilai x yang ditanyakan
value = 12

# proses menghitung
sum = y[0][0]
u = (value - x[0]) / (x[1] - x[0])
for i in range(1,n):
    sum = sum + (u_cal(u, i) * y[0][i]) / fact(i)

print("\nNilai x =", value,
      "adalah", round(sum, 6))
