#-----DATA-------------------------------------------------------------------------------------------------------------------------------------------
#   DATA MOBIL (DM) 
DM    = [   {'Plat'     : 'B 0708 IDV'  ,   'Brand'     : 'Honda'       ,
            'Tipe'      : 'CR-V'        ,   'Warna'     : 'Black'       , 
            'Biaya/hari': '800000'      ,   'Transmisi' : 'Otomatis'    ,
            'Status'    : 'Available'}  ,

            {'Plat'     : 'B 1504 CTG'  ,   'Brand'     : 'Toyota'      ,
            'Tipe'      : 'Fortuner'    ,   'Warna'     : 'Silver'      , 
            'Biaya/hari': '850000'      ,   'Transmisi' : 'Otomatis'    ,   
            'Status'    : 'Available'}  ,

            {'Plat'     : 'B 2301 BRO'  ,   'Brand'     : 'Mazda'       ,
            'Tipe'      : 'CX-5 GT'     ,   'Warna'     : 'Red'         , 
            'Biaya/hari': '850000'      ,   'Transmisi' : 'Otomatis'    ,
            'Status'    : 'Available'}  ,
             
            {'Plat'     : 'B 0801 MOM' ,   'Brand'     : 'Nissan'      ,
            'Tipe'      : 'X-Trail'     ,   'Warna'     : 'White'       , 
            'Biaya/hari': '900000'      ,   'Transmisi' : 'Manual'      ,
            'Status'    : 'Available'}  ,
             
            {'Plat'     : 'B 1304 DAD'  ,   'Brand'     : 'Mitsubishi'  , 
            'Tipe'      : 'Pajero'      ,   'Warna'     : 'Bronze'      , 
            'Biaya/hari': '900000'      ,   'Transmisi' : 'Manual'      ,
            'Status'    : 'Unavailable'}    ]

#   DATA MOBIL AVAILABLE (DMA)
DMA     = []
for i in range (len(DM)) :
    if DM[i]['Status'] == 'Available' : 
        DMA.append (DM[i])

#   LIST KEY
LK      = ['Plat','Brand', 'Tipe', 'Warna', 'Biaya/hari', 'Transmisi','Status']

#   LIST SELAIN PRIMARY KEY
LSPK    = ['Brand','Tipe','Warna','Biaya/hari', 'Transmisi','Status']


#-----LIST MENU-------------------------------------------------------------------------------------------------------------------------------------------
#   MENU UTAMA (M)
M   =   [   'Daftar Mobil', 
            'Tambah Daftar Mobil', 
            'Ubah Data Mobil', 
            'Hapus Data Mobil', 
            'Keluar'    ]

#   MENU READ DATA - DAFTAR MOBIL (M1)
M1  =   [   'Daftar Semua Mobil',
            'Daftar Mobil Available',
            'Menu Utama'    ]

#   MENU CREATE DATA - TAMBAH DAFTAR MOBIL (M2)
M2  =   [   'Tambah Daftar Mobil',
            'Menu Utama'    ]

#   MENU UPDATE DATA - UBAH DATA MOBIL (M3)
M3  =   [   'Ubah Data Mobil',
            'Menu Utama'    ]

#   MENU DELETE DATA - HAPUS DATA MOBIL (M4)
M4  =   [   'Hapus Data Mobil',
            'Menu Utama'    ]



#-----FUNCTION-------------------------------------------------------------------------------------------------------------------------------------------
from prettytable import PrettyTable #penyediaan data output menggunakan tabel

#   Function 1 (untuk menampilkan pembatas)
def space ()    :
    for i in range (100) :
        print ('-',end='')
    print ('\n')

#   Function 2 (untuk menginformasikan ketentuan nomor plat)
def ketentuan_plat ():
    print ('''Ketentuan Nomor Plat : 
B(spasi)XXXX(spasi)YYY
B       = Huruf 'B'
XXXX    = 4 angka
HHH     = 3 Huruf''')

#   Function 3 (untuk mengecek plat )
def cek_aturan_plat (plat) :
    panjang_kata    = len (plat)
    huruf_awal      = plat [0]
    angka_plat      = plat [2:6]
    huruf_akhir     = plat [7:10]
    cek_angka       = angka_plat.isnumeric()
    cek_akhir       = huruf_akhir.isalpha()
    if (panjang_kata != 10) or (huruf_awal != 'B') or (cek_angka != True) or (cek_akhir != True):
        return False
    else :
        return True

#   Function 4 (untuk menampilkan data mobil )
def daftar_mobil (judul,i,sumber) :
    print (f'{judul}')
    tabel = PrettyTable ()
    tabel.field_names = ['Plat', 'Brand', 'Tipe', 'Warna', 'Biaya/hari', 'Transmisi', 'Status']
    for i in range (len(sumber)) :
        tabel.add_row([sumber[i]['Plat'], sumber[i]['Brand'], sumber[i]['Tipe'], sumber[i]['Warna'], sumber[i]['Biaya/hari'], sumber[i]['Transmisi'], sumber[i]['Status']])
    print (tabel)

#   Function 5 (untuk menampilkan menu)
def menu (judul,menu,source) :
    space()
    print (f'{judul}')
    for menu in source   :
        print (f'{(source.index(menu))+1}  {menu}')
    print ('\n')




#-----INTRO-------------------------------------------------------------------------------------------------------------------------------------------
space ()
print ('''Hai Para Customer,

Selamat Datang di \'Fast Track\' Rental Mobil

Informasi
1.  Hanya menyediakan jasa peminjaman mobil lepas kunci
2.  Hanya melayani penyewaan mobil di area Jakarta
3.  Pengantaran mobil akan dilakukan oleh kami
4.  Pengembalian mobil merupakan kewajiban customer

Syarat dan ketentuan peminjaman
1. Foto dengan identitas diri berupa KTP dan SIM
2. Deposito sebesar Rp250.000,00 ''' )



#___MENU UTAMA___________________________________________________________________________________________________________________________________________

##  menampilkan menu utama
while True :
    menu ('Menu Utama', menu, M)    # akan selalu ditampilkan selama nilainya benar

##  input pilihan menu
    IM = int (input ('Menu\t\t\t:   '))



#___MENU READ DATA_______________________________________________________________________________________________________________________________________

##  menampilkan submenu 'DAFTAR MOBIL'
    if IM == 1 :
        while True  :
            menu ('Submenu Daftar Mobil',menu,M1)   # menampilkan submenu 1 selama kondisi True

##  input submenu pilihan
            IM1 = int (input ('Menu\t\t\t:   '))    # input nomor menu yg dipilih
            space()


### submenu 1 'DAFTAR SEMUA MOBIL'
            #   mengecek ada/tidaknya data
            if IM1 == 1 :                               
                if len(DM)==0 :
                    print ('Tidak ada data')

                #   menampilkan daftar mobil jika ada data
                else :
                    daftar_mobil('Daftar Mobil',i,DM)

### submenu 2 'DAFTAR MOBIL AVAILABLE'
            #   mengecek ada/tidaknya mobil yang statusnya available  
            elif IM1 == 2   :
                if len(DMA) == 0 :
                    print ('Tidak ada data')

            #   input 'Plat Mobil' jika ada data                
                else : 
                    ketentuan_plat()    # menginformasikan ketentuan plat data yang benar
                    plat = str (input('Plat\t\t\t:   ')).upper()    # user diminta untuk menginput data plat yang datanya ingin ditampilkan
                    print ('\n')
            
                    #   mengecek ada/tidaknya 'Plat Mobil' yang diinput
                    check = []
                    for i in range (len(DMA)) :
                        if plat == DMA[i]['Plat'] :
                            check.append(DMA[i])

                    #   menampilkan data mobil jika 'Plat Mobil' ada
                    if len(check) != 0 :
                        daftar_mobil('Data Mobil',i,check)

                    #   menginformasikan jika 'Plat Mobil' tidak ada
                    else :
                        print (f'Tidak ada data untuk nomor plat {plat}')
                        

### submenu 3 'MENU UTAMA' 
            elif IM1 == 3   :
                print ('Kembali Ke Menu Utama')
                break

### untuk input selain 1,2,3 
            else :
                print ('Maaf, mohon masukkan inputan yang benar')



#___MENU CREATE DATA_____________________________________________________________________________________________________________________________________
##  menampilkan submenu 'TAMBAH DAFTAR MOBIL'
    elif IM == 2 :
        while True  :
            menu ('Submenu Tambah Daftar Mobil',menu,M2)    # menampilkan submenu 2 selama kondisi True

##  input submenu pilihan
            IM2 = int (input ('Menu\t\t\t:   '))    # input nomor menu yg dipilih

### submenu 1 'TAMBAH DAFTAR MOBIL'
            ADD = {}        # variabel untuk menambahkan data kedalam list
            check_plat = [] # variabel untuk mengecek apakah nomor plat sudah ada atau belum, jika belum nilai len akan 0
            if IM2 == 1 :
                while True :
                    #   input 'Plat Mobil' baru
                    space ()
                    ketentuan_plat()    # meginformasikan ketentuan penulisan plat
                    plat_baru = str (input ('Plat\t\t\t:   ')).upper()  # input nomor plat baru

                    #   cek kesesuaian aturan 'Plat Mobil' baru
                    if cek_aturan_plat(plat_baru) == False :    # jika plat tidak sesuai dengan ketentuan
                        print ('Mohon cek kembali nomor plat')
                   
                    else :  # jika plat sudah sesuai dengan ketentuan
                        for i in range (len(DM)) :  # mengecek apakah plat baru sudah ada didalam database
                            if plat_baru == DM[i]['Plat'] :
                                check_plat.append(DM[i]['Plat'])        

                        #   input data lengkap untuk mobil dengan 'Plat Mobil' baru
                        if len(check_plat) == 0 :   # jika panjang = 0, maka plat baru belum ada didatabase
                            print (f'\nNomor Plat {plat_baru}')
                            ADD['Plat'] = plat_baru # untuk menambahkan data plat pada key 'Plat', karena input plat sudah dilakukan diawal (line 224)
                            for key in (LSPK) :     # untuk menambahkan data setiap key selain primary key(plat mobil)
                                ADD[f'{key}'] = str (input       (f'{key}\t\t\t:   ')).capitalize() # menambahkan setiap key dan value kedalam variabel add

                            #   konfirmasi penyimpanan data
                            while True :
                                simpan_data = str (input ('\nSimpan Data? (ya/tidak)\n')).lower()   # meminta konfirmasi, apakah data akan disimpan atau tidak
                                print ('\n')

                                if simpan_data != 'ya' and simpan_data != 'tidak' : #jika jawaban bukan (ya/tidak), akan kembali diminta untuk input data
                                    print ('Mohon masukkan input yang benar\n')

                                elif simpan_data =='ya' :   # jawaban = ya, user setuju untuk menyimpan data
                                    DM.append(ADD)  # menambahkan isi dari variabel add kedalam database DM
                                    print ('Data telah disimpan')   # menginformasikan ke user bahwa data telah disimpan
                                    daftar_mobil ('Daftar Mobil',i,DM)  # menampilkan data mobil baru
                                    break

                                else :
                                    print ('Data tidak tersimpan\n')    # jawaban = tidak, data tidak disimpan
                                    break
                    
                        else :  # jika nomor plat sudah ada di database DM
                            print ('Nomor plat sudah ada')
                            break
                    
                    break 

### submenu 2 'MENU UTAMA'
            elif IM2 == 2 : # kembali ke menu utama
                print ('Kembali Ke Menu Utama')
                break

### untuk input selain 1,2
            else :  # input selain 1,2 akan di informasikan dan diminta input ulang
                print ('Maaf, mohon masukkan inputan yang benar')
                space()                 



#___MENU UPDATE DATA_____________________________________________________________________________________________________________________________________ 
##  menampilkan submenu 'UBAH DATA MOBIL'
    elif IM == 3 :
        while True  :
            menu('Submenu Ubah Data Mobil',menu,M3)     # menampilkan submenu 3 selama kondisi True

##  input submenu pilihan
            IM3 = int (input ('Menu\t\t\t:   '))    # input nomor menu yg dipilih

### submenu 1 'UBAH DATA MOBIL'
            check_pu    =   []          # variabel untuk mengecek apakah plat yang ingin dirubah ada atau tidak di database DM
            index_ubah  =   int()       # untuk mengetahui index dari data yang ingin dirubah
            key_ubah    =   []          # untuk mengetahui apakah key yang ingin dirubah ada atau tidak didalam list key (LK)
            check_LSPK  =   []          # untuk mengetahui apakah key yang ingin dirubah ada atau tidak didalam list key selain dari primary key (LSPK)

            if IM3 == 1 :   # jika dipilih submenu 1

                #   input 'Plat Mobil' yang ingin dirubah datanya
                space ()
                daftar_mobil('Daftar Mobil',i,DM)   # menampilkan data mobil
                ketentuan_plat()    # menginformasikan ketentuan plat
                plat_ubah = str (input ('Plat\t\t\t:   ')).upper()  # user diminta untuk menginput nomor plat yang datanya ingin dirubah

                #   mengecek apakah 'Plat Mobil' ada/tidak
                for i in range (len(DM)) :
                    if plat_ubah == DM[i]['Plat'] : # looping dilakukan untuk mencocokan satu-satu nilai plat dalam data base dengan nilai plat yang ingin dirubah
                        check_pu.append(DM[i])  # jika ada nilai plat dalam database yang sama dengan plat_ubah maka akan menambahkan nilai ke dalam check_pu
                        index_ubah += i # dan menambahkan i kedalam index_ubah

                if len(check_pu) != 0 : # ketika len check_pu != 0 artinya plat_ubah yang dimasukkan ada didalam database
                    #   menampilkan data mobil terpilih
                    daftar_mobil('Data Mobil',i,check_pu)   # sehingga ditampilkan data keseluruhan untuk mobil dengan plat mobil tersebut

                    #   konfirmasi kelanjutan update
                    while True :
                        lanjut_update = str (input ('Lanjut Update? (ya/tidak)\n')).lower() # selama kondisi True, user akan diminta konfirmasi apakah mau melanjutkan update/tidak
                        print ('\n')

                        if lanjut_update != 'ya' and lanjut_update != 'tidak' : # jika jawabannya selain ya/tidak
                            print ('Mohon masukkan input yang benar\n')
                        
                        elif lanjut_update =='ya' : # jika jawabannya ya
                            kolom = str (input ('Nama kolom yang akan di update\t:   ')).capitalize()   #   user diminta input nama kolom yang akan dirubah datanya

                            for i in range (len(LK)) :  # looping untuk mengetahui apakah nama kolom yang diinput ada didalam list key atau tidak (kolomnya plat atau bukan)
                                if kolom == LK[i] :
                                    key_ubah.append(kolom)

                            for i in range (len(LSPK)) :    # looping untuk mengetahui apakah nama kolom yang diinput ada didalam list key selain primary key atau tidak
                                if kolom == LSPK[i] :
                                    check_LSPK.append(kolom)

                        #   input nilai baru untuk kolom yang dipilih
                            if (len(key_ubah) > 0) and ((len(check_LSPK)) > 0) :    # jika dia ada didalam list key tapi dia bukan primary key
                                nilai = str (input (f'{key_ubah[0]}             :   ')).capitalize()    # user diminta input data/value baru

                                while True :    # selama kondisi True akan berjalan terus
                                    update_data = str (input ('Update Data? (ya/tidak)\n')).lower() # user diminta untuk mengkonfirmasi apakah data mau diupdate/tidak
                                    print ('\n')

                                    if update_data != 'ya' and update_data != 'tidak' : # jika jawabannya selain ya/tidak, akan diinformasikan dan diminta input kembali
                                        print ('Mohon masukkan input yang benar\n')

                                    elif update_data =='ya' :   # jika jawabannya ya
                                        DM[index_ubah][kolom]   =   nilai   # akan mengubah value dari key untuk plat nomor yang dipilih
                                        print ('Data telah diupdate')   # menginformasikan data telah diupdate
                                        daftar_mobil ('Daftar Mobil',i,DM)  # menampilkan data mobil yang baru
                                        break

                                    else : # jika jawabannya tidak
                                        print ('Data batal diupdate\n') # menginformasikan data batal diupdate
                                        break

                                break

                            elif (len(key_ubah) > 0) and (kolom == 'Plat') :    # jika dia ada didalam list key tapi dia primary key ('Plat')
                                nilai_plat = str (input (f'Plat\t\t\t:   ')).upper()    # user diminta untuk input nomor plat baru

                                if cek_aturan_plat(nilai_plat) == False :   # nomor plat akan dicek terlebih dahulu, jika tidak sesuai ketentuan maka akan diinformasikan
                                    print ('Mohon cek kembali nomor plat')
                                
                                else :  # jika plat sudah sesuai ketentuan
                                    while True :
                                        update_data = str (input ('Update Data? (ya/tidak)\n')).lower()     # user diminta untuk mengkonfirmasi apakah data mau diupdate/tidak
                                        print ('\n')

                                        if update_data != 'ya' and update_data != 'tidak' :
                                            print ('Mohon masukkan input yang benar\n')

                                        elif update_data =='ya' :
                                            DM[index_ubah][kolom]   =   nilai_plat
                                            print ('Data telah diupdate')
                                            daftar_mobil ('Daftar Mobil',i,DM)
                                            break

                                        else :
                                            print ('Data batal diupdate\n')
                                            break
                                break

                            else :  # jika nama kolom tidak termasuk dalam list key
                                print ('Maaf, kolom yang anda masukkan tidak tersedia')
                                break


                        else :  # jika user tidak mau melanjutkan update
                            print ('Tidak melanjutkan update data\n')
                            break
                    
                else :  # jika nomor plat tidak ada didalam database
                    print (f'Tidak ada data untuk nomor plat {plat_ubah}')

### submenu 2 'MENU UTAMA'
            elif IM3 == 2 :
                print ('Kembali Ke Menu Utama')
                break

### untuk input selain 1,2
            else :
                print ('Maaf, mohon masukkan inputan yang benar')
                space() 



#___MENU DELETE DATA_____________________________________________________________________________________________________________________________________ 
##  menampilkan submenu 'HAPUS DATA MOBIL'
    elif IM == 4 :
        while True  :
            menu('Submenu Hapus Data Mobil',menu,M4)

##  input submenu pilihan
            IM4 = int (input ('Menu\t\t\t:   '))

            check_ph    =   []
            index_hapus =   int()

### submenu 1 'HAPUS DATA MOBIL'
            if IM4 == 1 :

                #   input 'Plat Mobil' yang ingin dihapus datanya
                space ()
                ketentuan_plat()    # meginformasikan ketentuan penulisan plat yang benar
                plat_hapus = str (input ('Plat\t\t\t:   ')).upper() # user diminta input plat mobil yang datanya ingin dihapus

                #   mengecek apakah 'Plat Mobil' ada/tidak didalam database
                for i in range (len(DM)) :
                    if plat_hapus == DM[i]['Plat'] :
                        check_ph.append(DM[i]) 
                        index_hapus += i

                if len(check_ph) != 0 : # artinya plat yang diinput ada didalam database DM
                    daftar_mobil('Data Mobil',i,check_ph)  #   menampilkan data mobil terpilih

                while True :
                    hapus_data = str (input ('Hapus Data? (ya/tidak)\n')).lower()  # user diminta mengkonfirmasi apakah data akan dihapus/tidak     
                    print ('\n')

                    if hapus_data != 'ya' and hapus_data != 'tidak' :
                        print ('Mohon masukkan input yang benar\n')

                    elif hapus_data =='ya' :
                        del DM[index_hapus]
                        print ('Data telah dihapus')
                        daftar_mobil ('Daftar Mobil',i,DM)
                        break

                    else :
                        print ('Data batal dihapus\n')
                        break
            
### submenu 2 'MENU UTAMA'
            elif IM4 == 2 :
                print ('Kembali Ke Menu Utama')
                break

### untuk input selain 1,2
            else :
                print ('Maaf, mohon masukkan inputan yang benar')
                space() 



#___KELUAR_________________________________________________________________________________________________________________________________________________ 
    elif IM == 5    :
        space ()
        print ('Keluar Program')
        break

    else :
        print ('Maaf, mohon masukkan inputan yang benar')
