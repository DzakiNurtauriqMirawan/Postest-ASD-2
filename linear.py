# SEARCHING LINEAR 

def LinearSearch(arr, x):
    for c in range(len(arr)):
            if type(arr[c])==list:
                a = LinearSearch(arr[c],x)
                if a == -1:
                    print('Loading. . . .')
                else:
                    print(f'{x} Nama ada pada indeks {c} kolom {a}')
                    exit()
    for i in range (len(arr)):
        if arr[i] == x:
            return i
    return -1

arr = ['Arsel','Avivah','Daiva',['Wahyu','Wibi']]
print(arr)
x = input('Masukan nama yang dicari: ')
b = LinearSearch(arr,x)
if b == -1:
    print('Nama tidak ditemukan')
else:
    print(f'{x} Nama ada pada indeks {b}')