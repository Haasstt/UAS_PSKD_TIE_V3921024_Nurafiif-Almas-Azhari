#import library
from PyPDF2 import PdfFileWriter, PdfFileReader
from cryptography.fernet import Fernet
import cv2
import numpy as np

#membuat menu
print("Selamat datang pilih menu dibawah :")
print("1. Enkripsi file PDF")
print("2. Enkripsi file CSV")
print("3. Deskripsi file PDF")
print("4. Deskripsi file CSV")
print("5. Enkripsi dan Deskripsi file Image")
print("===================================\n")

#masukkan pilihan
pilihan = int(input("Masukkan Pilihan (dengan angka) : "))

#pilihan nomor 1
if pilihan == 1:
    
    #judul menu
    print("\nEnkripsi file PDF")
    
    # buat objek pdf writer
    out = PdfFileWriter()
    
    #input file yang dienkripsi dan password
    path = input(r'Masukkan direktori file : ')
    nama_file = input(r'Nama file : ')
    key = (input('password : '))
  
    # buka file pdf asli 
    file = PdfFileReader(path + nama_file + ".pdf")
  
    # identifikasi total halaman file
    num = file.numPages
  
    #program membaca setiap halaman file sesuai halaman yg diidentifikasi 
    for idx in range(num):  
        page = file.getPage(idx)
    
        out.addPage(page)
        
    # enkripsi masing-masing halaman 
    out.encrypt(key)
    
    #deklarasi direktory file sesudah dienkripsi
    file_enkripsi = nama_file + "_enkripsi.pdf"
    path_enkripsi = "D:/uas_prakSKD/pdf/enkripsi/" + file_enkripsi
      
    # buka file enkripsi
    with open(path_enkripsi, "wb") as f:
    
        # simpan pdf 
        out.write(f)
    
    #output 
    print("\n")
    print('Direktori file asli : ', path + nama_file + ".pdf")
    print('Password : ', key) 
    print("File berhasil dienkripsi, lihat file di folder " + path_enkripsi)

#pilihan nomor 2
elif pilihan == 2:
    
    #judul menu
    print("\nEnkripsi file CSV")
    
    #input file yang dienkripsi dan password
    path = input(r'Masukkan direktori file : ')
    nama_file = input(r'Nama file : ')
    
    # key generation
    key = Fernet.generate_key()
 
    # membaca kunci byte menjadi string
    with open('filekey.key', 'wb') as filekey:
        filekey.write(key)

    # pakai kunci
    fernet = Fernet(key)
 
    # buka file csv
    with open(path + nama_file + '.csv', 'rb') as file:
        original = file.read()
     
    # enkripsi file csv
    dienkripsi = fernet.encrypt(original)
    
    #deklarasi direktory file sesudah dienkripsi
    file_enkripsi = nama_file + "_enkripsi.csv"
    path_enkripsi = "D:/uas_prakSKD/csv/enkripsi/" + file_enkripsi
 
    # simpan file enkripsi
    with open(path_enkripsi, 'wb') as enkripsi_file:
        enkripsi_file.write(dienkripsi)
    
    #output 
    print("\n")
    print('Direktori file asli : ', path + nama_file + ".csv")
    print("File berhasil dienkripsi, lihat file di folder " + path_enkripsi)
    #disini menambahkan print key, karena untuk mendeskripsikan file csv harus menggunakan key yang sama, berhubung key didapat dengan cara menggunakan key genarate maka key yang dikeluarkan berbeda beda
    print("Kunci enkripsi : ", key) 
    
elif pilihan == 3:
    
    #judul menu
    print("\nDeskripsi file PDF")
    
    # buat objek pdf writer
    out = PdfFileWriter()
    
    #input file yang dienkripsi dan password
    path = input(r'Masukkan direktori file : ')
    nama_file = input(r'Nama file : ')
    key = (input('password : '))
    
    # buka file pdf yg terenkripsi
    file = PdfFileReader(path + nama_file + ".pdf")
    
    # cek file terenkripsi atau tidak 
    if file.isEncrypted:
  
        # jika file terenkripsi, langsung di dekripsi pakai password 
        file.decrypt(key)
  
        # dekripsi dilakukan setiap halaman file pdf
        # simpan ke dalam file baru 
        for idx in range(file.numPages):
        
            # identifikasi halaman file 
            page = file.getPage(idx)
          
            # masukkan halaman yg sudah diidentifikasi dan sudah di dekripsi ke file baru 
            out.addPage(page)
      
        #deklarasi direktory file sesudah dideskripsi
        file_deskripsi = nama_file + "_deskripsi.pdf"
        path_deskripsi = "D:/uas_prakSKD/pdf/deskripsi/" + file_deskripsi
      
        # buka file baru
        with open(path_deskripsi, "wb") as f:
        
            # simpan file baru 
            out.write(f)
    
        #output 
        print("\n")
        print('Direktori file terenkripsi : ', path + nama_file + ".pdf")
        print('Password : ', key) 
        print("File berhasil dideskripsi, lihat file di folder " + path_deskripsi)
    
    else:
    
        print("File sudah dideskripsi")
    
elif pilihan == 4:
    
    #judul menu
    print("\nDeskripsi file CSV")
    
    #input file yang dideskripsi dan password
    path = input(r'Masukkan direktori file : ')
    nama_file = input(r'Nama file : ')
    kunci = (input('Masukkan kunci : '))
        
    # pakai kunci
    fernet = Fernet(kunci)
 
    # buka file csv yang dienkripsi
    with open(path + nama_file + '.csv', 'rb') as file:
        terenkripsi = file.read()
     
    # deskripsi file csv
    dideskripsi = fernet.decrypt(terenkripsi)
    
    #deklarasi direktory file sesudah dideskripsi
    file_deskripsi = nama_file + "_deskripsi.csv"
    path_deskripsi = "D:/uas_prakSKD/csv/deskripsi/" + file_deskripsi
 
    # simpan file enkripsi
    with open(path_deskripsi, 'wb') as deskripsi_file:
        deskripsi_file.write(dideskripsi)
    
    #output 
    print("\n")
    print('Direktori file asli : ', path + nama_file + ".csv")
    print("File berhasil dideskripsi, lihat file di folder " + path_deskripsi)
    
elif pilihan == 5:
    
    #judul menu
    print("\nEnkripsi file Gambar")
    
    #input file yang dienkripsi dan password
    path = input(r'Masukkan direktori file : ')
    nama_file = input(r'Nama file : ')
    
    demo = cv2.imread(path + nama_file + ".jpg", 0) # membuka file gambar
    r, c = demo.shape 
    key = np.random.randint(0, 256, size=(r, c), dtype=np.uint8)  # Generate random key image
    cv2.imwrite("D:/uas_prakSKD/image/key/" + nama_file + "_key.jpg", key)   # Save key image
    
    cv2.imshow("demo", demo)  # Display original image
    cv2.imshow("key", key)  # Display key image
    
    # encryption
    encryption = cv2.bitwise_xor(demo, key)  
    # Save the encrypted image
    cv2.imwrite("D:/uas_prakSKD/image/image_enkripsi/"+ nama_file + "_enkripsi.jpg", encryption)  
    # decrypt
    decryption = cv2.bitwise_xor(encryption, key)  
    # Save the decrypted image
    cv2.imwrite("D:/uas_prakSKD/image/image_deskripsi/"+ nama_file + "_deskripsi.jpg", decryption) 

    #output 
    print("\n")
    print('Direktori file asli : ', path + nama_file + ".jpg")
    print("File berhasil dienkripsi, lihat file di folder D:/uas_prakSKD/image/image_ekripsi/"+ nama_file + "_enkripsi.jpg")
    print("File berhasil dideskripsi, lihat file di folder D:/uas_prakSKD/image/image_deskripsi/"+ nama_file + "_deskripsi.jpg")
    
else:
    print("tidak Ada dalam pilihan")