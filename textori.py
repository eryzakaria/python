nama = 'Tidak'
kata = 'Iya'
text = 'Jadi Malu'

print('Kamu Suka Aku?')
print('Tinggal Pilih Iya atau Tidak')

while(True):
    nama = input('Dipilih Kak! ')
    if nama == kata:
        print(text)
        break
