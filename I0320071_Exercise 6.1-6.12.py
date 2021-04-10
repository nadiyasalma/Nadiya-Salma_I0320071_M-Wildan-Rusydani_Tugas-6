#exercise 6.1

#menentukan banyak pengulangan
n=5

#melakukan pengulangan
i = 1
while i <= n:
    print(i)
    i = i + 1    # bisa ditulis: i += 1

#exercise 6.2

#input untuk nilai n
n = int(input('masukkan banyak pengulangan: '))

#melakukan pengulangan
i = 1
while i <= n:
    print(i)
    i += 1

#exercise 6.3

#melakukan pengulangan
i = 1
while i <= 10:
    print('Baris ke-%d: Hello World' % i)
    i += 1

#exercise 6.4

# menentukan banyak pengulangan
n = 5
#melakukan pengulangan
i = n
while i >= 1:
    print(i)
    i = i - 1

#exercise 6.5

#menggunakan for pada tipe string
for ch in 'Praktikum':
    print(ch)

#exercise 6.6

#menggunakan for pada tipe list
for matkul in ['Kalkulus','Fisika','Kimia']:
    print(matkul)

#exercise 6.7

#membuat for untuk reentang nilai tertentu
for i in range(2,9) :  #lakukan pengulangan mulai dari i=2 sampai i < 9
    print('kuadrat dari ',i,'adalah', i**2)

#exercise 6.8

for i in range (2, 17, 3): #mulai dari 2 sampai kurang dari 20, step inkremen 3
    print(i, 'kuadrat adalah', i**2)

# exercise 6.9
for i in range (1, 11):
    for j in range(1, i + 1):
        print('%d' % (i*j), end='')
        print()

#exercise 6.10
i = 1
while i <= 10:
    j = 1
    while j <= i:
        print('%d' %(i*j), end= '')
        j += 1
    print()
    i += 1

#exercise 6.11
for i in range(11):
    print(i, end='')
    if i == 7:
        break

#exercise 6.12
for i in range(1,11):
    if i == 5:
        continue
    print (i,' x ',i ,' = ', i*i)
