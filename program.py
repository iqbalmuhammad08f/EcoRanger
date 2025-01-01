
import pandas as pd
import tabulate as tb
import os 
import datetime as dt
import sys
from babel.numbers import format_currency

akun_pengepul = "csv\\akun_pengepul.csv"
akun_supplier = "csv\\akun_supplier.csv"
sampah_organik = "csv\\sampah_organik.csv"
sampah_anorganik = "csv\\sampah_anorganik.csv"
history_setoran = "csv\\history_setoran.csv"
history_penarikan = "csv\\history_penarikan.csv"
history_penukaran = "csv\\history_penukaran.csv"
poin_dan_reward = "csv\\poin_dan_reward.csv"

def read_csv():
  global df_akun_pengepul,df_akun_supplier,df_sampah_anorganik,df_sampah_organik,df_history_setoran,df_history_penarikan,df_history_penukaran,df_poin_dan_reward
  
  if os.path.exists(akun_pengepul):
    df_akun_pengepul = pd.read_csv(akun_pengepul)
  else:
    df = pd.DataFrame({"username":["admin"],"password":[123]})
    df.to_csv(akun_pengepul, index=False)
    df_akun_pengepul = pd.read_csv(akun_pengepul)

  if os.path.exists(akun_supplier):
    df_akun_supplier = pd.read_csv(akun_supplier)
  else:
    df = pd.DataFrame(columns=["username","password","saldo","poin"])
    df.to_csv(akun_supplier, index=False)
    df_akun_supplier = pd.read_csv(akun_supplier)
  
  if os.path.exists(sampah_organik):
    df_sampah_organik = pd.read_csv(sampah_organik)
  else:
    df = pd.DataFrame(columns=["jenis","nama","harga/kg"])
    df.to_csv(sampah_organik, index=False)
    df_sampah_organik = pd.read_csv(sampah_organik)
  
  if os.path.exists(sampah_anorganik):
    df_sampah_anorganik = pd.read_csv(sampah_anorganik)
  else:
    df = pd.DataFrame(columns=["jenis","nama","harga/kg"])
    df.to_csv(sampah_anorganik, index=False)
    df_sampah_anorganik = pd.read_csv(sampah_anorganik)
  
  if os.path.exists(history_setoran):
    df_history_setoran = pd.read_csv(history_setoran)
  else:
    df = pd.DataFrame(columns=["tanggal/waktu","username","jenis","nama","berat","uang","poin","status"])
    df.to_csv(history_setoran, index=False)
    df_history_setoran = pd.read_csv(history_setoran)
  
  if os.path.exists(history_penarikan):
    df_history_penarikan = pd.read_csv(history_penarikan)
  else:
    df = pd.DataFrame(columns=["waktu","username","penarikan","status"])
    df.to_csv(history_penarikan, index=False)
    df_history_penarikan = pd.read_csv(history_penarikan)
  
  if os.path.exists(history_penukaran):
    df_history_penukaran = pd.read_csv(history_penukaran)
  else:
    df = pd.DataFrame(columns=["waktu","username","penukar"])
    df.to_csv(history_penukaran, index=False)
    df_history_penukaran = pd.read_csv(history_penukaran)
  
  if os.path.exists(poin_dan_reward):
    df_poin_dan_reward = pd.read_csv(poin_dan_reward)
  else:
    df = pd.DataFrame({"poin/kg": [0],"reward": [0],"ketentuan": [0]})
    df.to_csv(poin_dan_reward, index=False)
    df_poin_dan_reward = pd.read_csv(poin_dan_reward)

def format_rupiah(uang):
    return format_currency(uang, 'IDR', locale='id_ID')

def menu_utama():
  read_csv()
  while True:
    os.system("cls")
    read_csv()
    print("""
███████  ██████  ██████  ██████   █████  ███    ██  ██████  ███████ ██████  
██      ██      ██    ██ ██   ██ ██   ██ ████   ██ ██       ██      ██   ██ 
█████   ██      ██    ██ ██████  ███████ ██ ██  ██ ██   ███ █████   ██████  
██      ██      ██    ██ ██   ██ ██   ██ ██  ██ ██ ██    ██ ██      ██   ██ 
███████  ██████  ██████  ██   ██ ██   ██ ██   ████  ██████  ███████ ██   ██\n""")
    menu = "1. Login\n2. Register\n0. Keluar"
    print(tb.tabulate([[menu]], tablefmt="rounded_grid"))
    user = input("Masukkan pilihan: ")

    if user == "1":
      login()
    elif user == "2":
      register()
    elif user == "0":
      os.system("cls")
      print("""
████████ ███████ ██████  ██ ███    ███  █████  ██   ██  █████  ███████ ██ ██   ██ 
   ██    ██      ██   ██ ██ ████  ████ ██   ██ ██  ██  ██   ██ ██      ██ ██   ██ 
   ██    █████   ██████  ██ ██ ████ ██ ███████ █████   ███████ ███████ ██ ███████ 
   ██    ██      ██   ██ ██ ██  ██  ██ ██   ██ ██  ██  ██   ██      ██ ██ ██   ██ 
   ██    ███████ ██   ██ ██ ██      ██ ██   ██ ██   ██ ██   ██ ███████ ██ ██   ██ """)
      sys.exit()
    else:
      input("Pilihan tidak tersedia, Enter untuk mengulangi")
      continue

def login():
  while True:
    os.system("cls")
    read_csv()
    print("""
██       ██████   ██████  ██ ███    ██ 
██      ██    ██ ██       ██ ████   ██ 
██      ██    ██ ██   ███ ██ ██ ██  ██ 
██      ██    ██ ██    ██ ██ ██  ██ ██ 
███████  ██████   ██████  ██ ██   ████""")
    global username
    username = input("\nMasukkan username: ")
    password = input("Masukkan password: ")

    if username in df_akun_pengepul["username"].values and password in df_akun_pengepul["password"].values.astype(str):
      menu_pengepul()
    elif username in df_akun_supplier["username"].values and password in df_akun_supplier["password"].values.astype(str):
      menu_supplier()
    else:
      while True:
        os.system("cls")
        print("Username dan Password tidak sesuai atau belum terdaftar")
        menu = "1. Ulangi\n2. Register\n0. kembali"
        print(tb.tabulate([[menu]], tablefmt="rounded_grid"))
        user = input("Masukkan pilihan: ")

        if user == "1":
          break
        elif user == "2":
          register()
        elif user == "0":
          menu_utama()
        else:
          input("Pilihan tidak tersedia, Enter untuk mengulangi")
          continue

def register():
  while True:
    os.system("cls")
    def logo():
      print("""
██████  ███████  ██████  ██ ███████ ████████ ███████ ██████  
██   ██ ██      ██       ██ ██         ██    ██      ██   ██ 
██████  █████   ██   ███ ██ ███████    ██    █████   ██████  
██   ██ ██      ██    ██ ██      ██    ██    ██      ██   ██ 
██   ██ ███████  ██████  ██ ███████    ██    ███████ ██   ██""")
    logo()
    username = input("\nMasukkan username: ")

    if not username:
      input("Username tidak boleh kosong, Enter untuk mengulangi")
      continue
    else:
      if username in df_akun_supplier["username"].values:
        input("Username sudah ada, Enter untuk mengulangi")
        continue
      while True:
        os.system("cls")
        logo()
        print("\nMasukkan username: " + username)
        password = input("Masukkan password: ")

        if not password:
          input("Password tidak boleh kosong, Enter untuk mengulangi")
        else:
          ulangi_password = input("Ulangi password: ")

          if password == ulangi_password:
            df = pd.DataFrame({"username":[username],"password":[password],"saldo":[0],"poin":[0]})
            df.to_csv(akun_supplier, mode='a', header=False, index=False)
            input("Akun berhasil dibuat, Enter untuk kembali ke menu utama")
            menu_utama()
          else:
            input("Password tidak sama, Enter untuk mengulangi")
            continue

def menu_pengepul():
  while True:
    os.system("cls")
    print("""
██████  ███████ ███    ██  ██████  ███████ ██████  ██    ██ ██      
██   ██ ██      ████   ██ ██       ██      ██   ██ ██    ██ ██      
██████  █████   ██ ██  ██ ██   ███ █████   ██████  ██    ██ ██      
██      ██      ██  ██ ██ ██    ██ ██      ██      ██    ██ ██      
██      ███████ ██   ████  ██████  ███████ ██       ██████  ███████\n""")
    menu = "1. CRUD Sampah\n2. Kelola Akun Supplier\n3. Konfirmasi Transaksi\n4. Lihat History\n5. Kelola Poin dan Reward\n0. Keluar"
    print(tb.tabulate([[menu]], tablefmt="rounded_grid"))
    user = input("Masukkan pilihan: ")

    if user == "1":
      crud_sampah()
    elif user == "2":
      kelola_akun_supplier()
    elif user == "3":
      konfirmasi_supplier()
    elif user == "4":
      history_akun_supplier()
    elif user == "5":
      kelola_reward()
    elif user == "0":
      menu_utama()
    else:
      input("Pilihan tidak ada, Enter untuk mengulangi")
      continue

def crud_sampah():
  while True:
    os.system("cls")
    print("MENU CRUD".center(29))
    menu = "\n1. Tambah Sampah\n2. Edit atau Hapus Sampah\n3. Lihat Data Sampah\n0. Kembali"
    print(tb.tabulate([[menu]], tablefmt="rounded_grid"))
    user = input("Masukkan pilihan: ")

    if user == "1":
      tambah_sampah()
    elif user == "2":
      edit_hapus_sampah()
    elif user == "3":
      lihat_data_sampah()
    elif user == "0":
      menu_pengepul()
    else:
      input("Pilihan tidak ada, Enter untuk mengulangi")
      continue

def tambah_sampah():
  while True:
    os.system("cls")
    print("JENIS SAMPAH".center(24))
    menu = "1. Sampah Organik\n2. Sampah Anorganik\n0. Kembali"
    print(tb.tabulate([[menu]], tablefmt="rounded_grid"))
    cek = True
    user = input("Masukkan pilihan: ")

    if user == "1":
      while cek:
        os.system("cls")
        nama = input("Masukkan nama sampah: ")

        if nama in df_sampah_organik["nama"].values:
          input("Sampah sudah ada, Enter untuk mengulangi")
          continue
        try:
          harga = int(input("Masukkan harga/kg: "))
        except ValueError:
          input("Harga harus angka, Enter untuk mengulangi")
          continue

        df = pd.DataFrame({"jenis":["organik"],"nama":[nama],"harga/kg":[harga]})
        df.to_csv(sampah_organik, mode="a", index=False, header= False)

        while cek:
          os.system("cls")
          user = input("Sampah berhasil ditambahkan, Mau menambahkan lagi? (y/t): ")

          if user == "y":
            cek = False
            continue
          elif user == "t":
            crud_sampah()
          else:
            input("Pilihan tidak ada, Enter untuk mengulangi")
            continue
    elif user == "2":
      while cek:
        os.system("cls")
        nama = input("Masukkan nama sampah: ")

        if nama in df_sampah_anorganik["nama"].values:
          input("Sampah sudah ada, Enter untuk mengulangi")
          continue
        try:
          harga = int(input("Masukkan harga/kg: "))
        except ValueError:
          input("Harga harus angka, Enter untuk mengulangi")
          continue

        df = pd.DataFrame({"jenis":["anorganik"],"nama":[nama],"harga/kg":[harga]})
        df.to_csv(sampah_anorganik, mode="a", index=False, header= False)

        while cek:
          os.system("cls")
          user = input("Sampah berhasil ditambahkan, Mau menambahkan lagi? (y/t): ")

          if user == "y":
            cek = False
            continue
          elif user == "t":
            crud_sampah()
          else:
            input("Pilihan tidak ada, Enter untuk mengulangi")
            continue
    elif user == "0":
      crud_sampah()
    else:
      input("Pilihan tidak ada, Enter untuk mengulangi")
      continue
    
def edit_hapus_sampah():
  while True:
    os.system("cls")
    read_csv()

    if len(df_sampah_organik) > 0 or len(df_sampah_anorganik) > 0:
      print("EDIT atau HAPUS SAMPAH".center(24))
      menu = "\n1. Edit Harga Sampah\n2. Hapus Sampah\n0. Kembali"
      print(tb.tabulate([[menu]], tablefmt="rounded_grid"))
      user = input("Masukkan pilihan: ")

      if user == "1":
        edit_sampah()
      elif user == "2":
        hapus_sampah()
      elif user == "0":
        crud_sampah()
      else:
        input("Pilihan tidak ada, Enter untuk mengulangi")
        continue
    else:
      input("Tidak ada data sampah yang dapat di edit, Enter melanjutkan")
      crud_sampah()

def edit_sampah():
  if len(df_sampah_organik) > 0 or len(df_sampah_anorganik) > 0:
    while True:
      os.system("cls")
      
      read_csv()
      df_gabungan = pd.concat([df_sampah_organik,df_sampah_anorganik],ignore_index=True, axis=0)
      df_gabungan["harga/kg"] = df_gabungan["harga/kg"].apply(format_rupiah)
      df_gabungan.index +=1
      
      print(("DAFTAR SAMPAH").center(52))
      print(tb.tabulate(df_gabungan, headers = ["No","Jenis","Nama","Harga/Kg"], showindex=True, tablefmt="fancy_grid"))
      print("\n0. Kembali")
      nama = input("\nMasukkan Nama sampah yang ingin diubah harganya: ")

      if nama in df_sampah_organik["nama"].values:
        try:
          harga_baru = int(input("Masukkan harga baru: "))
        except ValueError:
          input("Harga harus angka, Enter untuk mengulangi")
          continue

        df_sampah_organik.loc[df_sampah_organik["nama"]==nama, "harga/kg"] = harga_baru
        df_sampah_organik.to_csv(sampah_organik, index=False)
        
        input("Harga sampah berhasil dirubah, Enter melanjutkan")
        continue
      elif nama in df_sampah_anorganik["nama"].values:
        try:
          harga_baru = int(input("Masukkan harga baru: "))
        except ValueError:
          input("Harga harus angka, Enter untuk mengulangi")
          continue

        df_sampah_anorganik.loc[df_sampah_anorganik["nama"]==nama, "harga/kg"] = harga_baru
        df_sampah_anorganik.to_csv(sampah_anorganik, index=False)
        
        input("Harga sampah berhasil dirubah, Enter melanjutkan")
        continue
      elif nama == "0":
        edit_hapus_sampah()
      else:
        input("Sampah tidak ada, Enter untuk mengulangi")
        continue
  else:
    input("Tidak ada data sampah yang dapat diedit atau dihapus, Enter melanjutkan")
    crud_sampah()

def hapus_sampah():
  if len(df_sampah_organik) > 0 or len(df_sampah_anorganik) > 0:
    while True:
      os.system("cls")

      def daftar_sampah():
        read_csv()
        df_gabungan = pd.concat([df_sampah_organik,df_sampah_anorganik],ignore_index=True, axis=0)
        df_gabungan["harga/kg"] = df_gabungan["harga/kg"].apply(format_rupiah)
        df_gabungan.index +=1
        print(("DAFTAR SAMPAH").center(51))
        print(tb.tabulate(df_gabungan, headers = ["No","Jenis","Nama","Harga/Kg"], showindex=True, tablefmt="fancy_grid"))
    
      daftar_sampah() 
      menu = "1. Hapus Nama Sampah\n2. Hapus Jenis sampah\n3. hapus Semua Sampah\n0. Kembali"
      print(tb.tabulate([[menu]],tablefmt="rounded_grid"))
      user = input("\nMasukkan pilihan : ")

      if user == "1":
        while True:
          os.system("cls")
          daftar_sampah()
          print("\n0. Kembali")
          nama = input("\nMasukkan nama sampah yang ingin dihapus: ")

          if nama in df_sampah_organik["nama"].values:
            df = df_sampah_organik[df_sampah_organik["nama"] != nama]
            df.to_csv(sampah_organik, index=False)
            input("Sampah berhasil dihapus, Enter melanjutkan")
            continue
          elif nama in df_sampah_anorganik["nama"].values:
            df = df_sampah_anorganik[df_sampah_anorganik["nama"] != nama]
            df.to_csv(sampah_anorganik, index=False)
            input("Sampah berhasil dihapus, Enter melanjutkan")
            continue
          elif nama == "0":
            break
          else:
            input("Sampah tidak ada, Enter untuk mengulangi")
            continue
      elif user == "2":
        while True:
          os.system("cls")
          daftar_sampah()
          print("\n0. Kembali")
          jenis = input("\nMasukkan jenis sampah yang ingin dihapus: ")

          if jenis in df_sampah_organik["jenis"].values:
            df = pd.DataFrame(columns=["jenis","nama","harga/kg"])
            df.to_csv(sampah_organik, index=False)
            input("Sampah berhasil dihapus, Enter melanjutkan")
            continue
          elif jenis in df_sampah_anorganik["jenis"].values:
            df = pd.DataFrame(columns=["jenis","nama","harga/kg"])
            df.to_csv(sampah_anorganik, index=False)
            input("Sampah berhasil dihapus, Enter melanjutkan")
            continue
          elif jenis == "0":
            break
          else:
            input("Jenis sampah tidak ada, Enter untuk mengulangi")
            continue
      elif user == "3":
        while True:
          os.system("cls")
          user = input("Apakah yakin ingin menghapus semua sampah? (y/t)")

          if user.lower() == "y":
            df = pd.DataFrame(columns=["jenis","nama","harga/kg"])
            df.to_csv(sampah_organik, index=False)
            df = pd.DataFrame(columns=["jenis","nama","harga/kg"])
            df.to_csv(sampah_anorganik, index=False)
            input("Semua sampah berhasil dihapus, Enter melanjutkan")
            break
          elif user.lower() == "t":
            break
          else:
            input("Pilihan tidak ada, Enter untuk mengulangi")
            continue
      elif user == "0":
        edit_hapus_sampah()
  else:
    input("Tidak ada data sampah yang dapat diedit atau dihapus, Enter melanjutkan")
    crud_sampah()

def lihat_data_sampah():
  while True:
    os.system("cls")
    read_csv()
    print("DATA SAMPAH".center(24))
    menu = "\n1. Sampah Organik\n2. Sampah Anorganik\n0. Kembali"
    print(tb.tabulate([[menu]], tablefmt="rounded_grid"))
    user = input("\nMasukkan pilihan: ")

    if user == "1":
      os.system("cls")
      df_sampah_organik["harga/kg"] = df_sampah_organik["harga/kg"].apply(format_rupiah)
      df_sampah_organik.index += 1

      print("SAMPAH ORGANIK".center(50))
      print(tb.tabulate(df_sampah_organik,headers=["No","Jenis","Nama","Harga/kg"], tablefmt="fancy_grid",showindex=True))
      input("Enter untuk kembali")
      continue
    elif user == "2":
      os.system("cls")
      df_sampah_anorganik["harga/kg"] = df_sampah_anorganik["harga/kg"].apply(format_rupiah)
      df_sampah_anorganik.index += 1
      
      print("SAMPAH ANORGANIK".center(50))
      print(tb.tabulate(df_sampah_anorganik,headers=["No","Jenis","Nama","Harga/kg"], tablefmt="fancy_grid",showindex=True))
      input("Enter untuk kembali")
      continue
    elif user == "0":
      crud_sampah()
    else:
      input("Pilihan tidak ada, Enter untuk mengulangi")
      continue

def kelola_akun_supplier():
  while True:
    os.system("cls")
    def tabel_akun_supplier():
      read_csv()
      tabel = df_akun_supplier.copy()
      tabel["saldo"] = tabel["saldo"].apply(format_rupiah)
      tabel.index += 1
      print(tb.tabulate(tabel,headers=["No","Username","Password","Saldo","Poin"],showindex=True,tablefmt="fancy_grid"))

    tabel_akun_supplier()
    menu = "\n1. Hapus Akun Supplier\n2. Hapus Seluruh Akun Supplier\n0. kembali"
    print(tb.tabulate([[menu]], tablefmt="rounded_grid"))
    user = input("\nMasukkan pilihan: ")

    if user == "1":
      while True:
        os.system("cls")
        tabel_akun_supplier()
        print("\n0. Kembali")
        nama = input("\nMasukkan nama supplier yang ingin dihapus: ")
        
        if nama == "0":
          break
        df = df_akun_supplier[df_akun_supplier["username"] != nama]
        df.to_csv(akun_supplier, index=False)
        os.system("cls")
        print("Akun berhasil dihapus")
        user = input("Apakah ingin menghapus yang lain lagi? (y/t): ")
        
        if user.lower() == "y":
          continue
        elif user.lower() == "t":
          break
        else:
          input("Pilihan tidak ada, Enter untuk mengulangi")
          continue
    elif user == "2":
      while True:
        os.system("cls")
        user = input("Apakah yakin ingin menghapus seluruh akun supplier? (y/t): ")

        if user.lower() == "y":
          df = pd.DataFrame(columns=["username","password","saldo","poin"])
          df.to_csv(akun_supplier, index=False)
          input("Seluruh akun berhasil di hapus, Enter untuk kembali")
          break
        elif user.lower() == "t":
          break
        else:
          input("Pilihan tidak ada, Enter untuk mengulangi")
          continue
    elif user == "0":
      menu_pengepul()
    else:
      input("Pilihan tidak ada, Enter untuk mengulangi")
      continue

def konfirmasi_supplier():
  while True:
    os.system("cls")
    print("KONFIRMASI TRANSAKSI".center(29))
    menu = "1. Konfirmasi Setoran \n2. Konfirmasi Tarik Saldo\n0. Kembali"
    print(tb.tabulate([[menu]], tablefmt="rounded_grid"))
    user = input("\nMasukkan pilihan: ")

    if user == "1":
      setoran_supplier()
    elif user == "2":
      penarikan_saldo()
    elif user == "0":
      menu_pengepul()
    else:
      os.system("cls")
      input("Pilihan tidak ada, Enter untuk mengulangi")
      continue

def setoran_supplier():
  read_csv()
  while True:
    if "checking" in list(df_history_setoran["status"].values):
      os.system("cls")
      tabel = df_history_setoran.loc[df_history_setoran["status"]=="checking"].copy()
      tabel["uang"] = tabel["uang"].apply(format_rupiah)
      tabel = tabel.reset_index(drop=True)
      tabel.index +=1

      print(tb.tabulate(tabel, showindex=True, headers=["No","Tanggal/Waktu","Username","Jenis","Nama","Berat","Uang","Poin","Status"],tablefmt="fancy_grid"))
      menu = "1. Konfirmasi Semua Setoran\n2. Konfirmasi Setoran Per-Akun\n0. Kembali"
      print(tb.tabulate([[menu]],tablefmt="rounded_grid"))
      user = input("\nMasukkan pilihan: ")

      if user == "1":
        while True:
          os.system("cls")
          user = input("Apakah kamu yakin ingin mengkonfirmasi semua setoran? (y/t): ")

          if user.lower() == "y":
            sementara = df_history_setoran.loc[df_history_setoran["status"]=="checking"]
            nama = sementara["username"].unique()

            for i in nama:
              df = sementara[sementara["username"] == i]
              poin = df["poin"].sum()
              df_akun_supplier.loc[df_akun_supplier["username"]==i,"poin"] += poin
              df_akun_supplier.to_csv(akun_supplier,index=False)
              saldo = df["uang"].sum()
              df_akun_supplier.loc[df_akun_supplier["username"]==i,"saldo"] += saldo
              df_akun_supplier.to_csv(akun_supplier,index=False)
              df_history_setoran.loc[df_history_setoran["username"]==i,"status"] = "succeed"
              df_history_setoran.to_csv(history_setoran,index=False)
            sementara = []
            nama = []
            input("Semua setoran berhasil dikonfirmasi, Enter untuk kembali")
            break
          elif user.lower() == "t":
            break
          else:
            input("Pilihan tidak ada, Enter untuk mengulangi")
            continue
      elif user == "2":
        while True:
          os.system("cls")
          print(tb.tabulate(tabel, showindex=True, headers=["No","Tanggal/Waktu","Username","Jenis","Nama","Berat","Uang","Poin","Status"],tablefmt="fancy_grid"))
          print("0. Kembali")
          nama = input("\nMasukkan username supplier yang ingin dikonfirmasi: ")
          
          if nama in list(df_history_setoran["username"].values):
            sementara = df_history_setoran.loc[(df_history_setoran["username"]==nama) & (df_history_setoran["status"]=="checking")]

            poin = sementara["poin"].sum()
            df_akun_supplier.loc[df_akun_supplier["username"]==nama,"poin"] += poin
            df_akun_supplier.to_csv(akun_supplier,index=False)
            saldo = sementara["uang"].sum()
            df_akun_supplier.loc[df_akun_supplier["username"]==nama,"saldo"] += saldo
            df_akun_supplier.to_csv(akun_supplier,index=False)
            df_history_setoran.loc[df_history_setoran["username"]==nama,"status"] = "succeed"
            df_history_setoran.to_csv(history_setoran,index=False)
            sementara = []

            input("Setoran berhasil dikonfirmasi, Enter untuk kembali")
            break
          elif nama == "0":
            break
          else:
            input("Username tidak ada, Enter untuk mengulangi")
            continue
      elif user == "0":
        konfirmasi_supplier()
      else:
        os.system("cls")
        input("Pilihan tidak ada, Enter untuk mengulangi")
        continue
    else:
      os.system("cls")
      input("Tidak ada sampah yang perlu di konfirmasi, Enter untuk kembali")
      menu_pengepul()

def penarikan_saldo():
  while True:
    if "processing" in df_history_penarikan["status"].values:
      os.system("cls")

      tabel = df_history_penarikan.loc[df_history_penarikan["status"]=="processing"].copy()
      tabel["penarikan"] = tabel["penarikan"].apply(format_rupiah)
      tabel = tabel.reset_index(drop=True)
      tabel.index += 1

      print(tb.tabulate(tabel, showindex=True, headers=["No","Tanggal/Waktu","Username","Penarika","Status"], tablefmt="fancy_grid"))
      menu = "1. Komfirmasi Semua\n2. Konfirmasi Per-Akun\n0. Kembali"
      print(tb.tabulate([[menu]],tablefmt="rounded_grid"))
      user = input("\nMasukkan pilihan: ")

      if user == "1":
        while True:
          os.system("cls")
          user = input("Apakah kamu yakin ingin mengkonfirmasi semua penarikan? (y/t): ")

          if user.lower() == "y":
            sementara = df_history_penarikan.loc[df_history_penarikan["status"]=="processing"]
            nama = sementara["username"].unique()

            for i in nama:
              saldo_tarik = sementara.loc[sementara["username"]==i,"penarikan"]
              saldo_tarik = sum(saldo_tarik)
              df_akun_supplier.loc[df_akun_supplier["username"]==i,"saldo"] -= saldo_tarik
              df_akun_supplier.to_csv(akun_supplier,index=False)
              df_history_penarikan.loc[df_history_penarikan["username"]==i,"status"] = "succeed"
              df_history_penarikan.to_csv(history_penarikan,index=False)
            sementara = []
            nama = []

            input("Semua penarikan berhasil dikonfirmasi, Enter untuk kembali")
            break
          elif user.lower() == "t":
            break
          else:
            input("Pilihan tidak ada, Enter untuk mengulangi")
            continue
      elif user == "2":
        while True:
          os.system("cls")
          print(tb.tabulate(tabel, showindex=True, headers=["no"]+list(tabel.columns), tablefmt="fancy_grid"))
          print("0. Kembali")
          nama = input("\nMasukkan username supplier yang ingin dikonfirmasi: ")

          if nama in list(df_history_penarikan["username"].values):
            sementara = df_history_penarikan.loc[(df_history_penarikan["username"]==nama) & (df_history_penarikan["status"]=="processing")]
            saldo = sementara["penarikan"].sum()
            df_akun_supplier.loc[df_akun_supplier["username"]==nama,"saldo"] -= saldo
            df_akun_supplier.to_csv(akun_supplier,index=False)
            df_history_penarikan.loc[df_history_penarikan["username"]==nama,"status"] = "succeed"
            df_history_penarikan.to_csv(history_penarikan,index=False)
            sementara = []
            input("Penarikan berhasil dikonfirmasi, Enter untuk kembali")
            break
          elif nama == "0":
            break
          else:
            input("Username tidak ada, Enter untuk mengulangi")
            continue
      elif user == "0":
        break
      else:
        input("Pilihan tidak ada, Enter untuk mengulangi")
        continue
    else:
      os.system("cls")
      input("Tidak ada penarikan yang perlu di konfirmasi, Enter untuk kembali")
      menu_pengepul()
def kelola_reward():
  while True:
    os.system("cls")
    
    read_csv()
    poin = df_poin_dan_reward.loc[0,"poin/kg"]
    reward = df_poin_dan_reward.loc[0,"reward"]
    reward = format_rupiah(reward)
    ketentuan = df_poin_dan_reward.loc[0,"ketentuan"]

    print("POIN dan REWARD".center(56))
    tabel = [[f"Poin yang didapat setelah melakukan setoran: {poin}/kg"],[f"Reward yang dapat ditukarkan: {reward}"],[f"Poin yang diperlukan untuk menukar reward: {ketentuan}"]]
    print(tb.tabulate(tabel,tablefmt="fancy_grid"))

    menu = "1. Edit Poin Yang Didapat\n2. Edit Reward\n3. Edit Ketentuan Poin\n0. Kembali"
    print(tb.tabulate([[menu]], tablefmt="rounded_grid"))
    user = input("Masukkan pilihan: ")

    if user == "1":
      while True:
        os.system("cls")
        try:
          poin = int(input("Masukkan jumlah poin yang didapat setelah melakukan setoran/kg: "))
        except ValueError:
          input("Poin harus berupa angka, Enter untuk kembali")
          continue
        df_poin_dan_reward.iloc[0,0] = poin
        df_poin_dan_reward.to_csv(poin_dan_reward, index=False)
        input("Poin berhasil dirubah, Enter untuk kembali")
        break
    elif user == "2":
      while True:
        os.system("cls")
        try:
          reward = int(input("Masukkan besaran reward yang akan diperoleh: "))
        except ValueError:
          input("Reward harus berupa angka, Enter untuk kembali")
          continue
        df_poin_dan_reward.iloc[0,1] = reward
        df_poin_dan_reward.to_csv(poin_dan_reward, index=False)
        input("Reward berhasil dirubah, Enter untuk kembali")
        break
    elif user == "3":
      while True:
        os.system("cls")
        try:
          ketentuan = int(input("Masukkan poin yang diperlukan untuk penukaran reward: "))
        except ValueError:
          input("Poin ketentuan harus berupa angka, Enter untuk melanjutkan")
          continue
        df_poin_dan_reward.iloc[0,2] = ketentuan
        df_poin_dan_reward.to_csv(poin_dan_reward, index=False)
        input("Ketentuan poin berhasil dirubah, Enter untuk kembali")
        break
    elif user == "0":
      menu_pengepul()
    else:
      input("Pilihan tidak ada, Enter untuk mengulangi")
      continue

def history_akun_supplier():
  while True:
    os.system("cls")
    print("HISTORY".center(24))
    menu = "1. History Setoran\n2. History Penarikan\n3. History Penukaran\n0. Kembali"
    print(tb.tabulate([[menu]], tablefmt="rounded_grid"))
    user = input("Masukkan pilihan: ")

    if user == "1":
      os.system("cls")
      df_history_setoran["uang"] = df_history_setoran["uang"].apply(format_rupiah)
      df_history_setoran.index += 1
      print("HISTORY SETORAN".center(119))
      print(tb.tabulate(df_history_setoran,headers=["No","Taanggal/Waktu","Username","Jenis","Nama","Berat","Uang","Poin","Status"],tablefmt="fancy_grid"))
      input("\nEnter untuk kembali")
      continue
    elif user == "2":
      os.system("cls")
      df_history_penarikan["penarikan"] = df_history_penarikan["penarikan"].apply(format_rupiah)
      df_history_penarikan.index += 1
      print("HISTORY PENARIKAN".center(73))
      print(tb.tabulate(df_history_penarikan,headers=["No","Tanggal/Waktu","Username","Penarikan","Status"]+list(df_history_penarikan.columns),tablefmt="fancy_grid"))
      input("\nEnter untuk kembali")
      continue
    elif user == "3":
      os.system("cls")
      df_history_penukaran["penukar"] = df_history_penukaran["penukar"].apply(format_rupiah)
      df_history_penukaran.index += 1
      print("HISTORY PENUKARAN".center(58))
      print(tb.tabulate(df_history_penukaran,headers=["No","Tanggal/Waktu","Username","Reward"],tablefmt="fancy_grid"))
      input("\nEnter untuk kembali")
      continue
    elif user == "0":
      menu_pengepul()
    else:
      input("Pilihan tidak ada, Enter untuk mengulangi")
      continue

def menu_supplier():
  read_csv()
  while True:
    os.system("cls")

    read_csv()
    saldo = df_akun_supplier.loc[df_akun_supplier["username"]==username,"saldo"].values[0]
    poin = df_akun_supplier.loc[df_akun_supplier["username"]==username,"poin"].values[0]

    saldo = format_rupiah(saldo)
    print("""

███████ ██    ██ ██████  ██████  ██      ██ ███████ ██████  
██      ██    ██ ██   ██ ██   ██ ██      ██ ██      ██   ██ 
███████ ██    ██ ██████  ██████  ██      ██ █████   ██████  
     ██ ██    ██ ██      ██      ██      ██ ██      ██   ██ 
███████  ██████  ██      ██      ███████ ██ ███████ ██   ██\n""")
    print(f"Selamat datang {username}\n")
    print(f"Saldo: {saldo} ")
    print(f"Poin: {poin} ")
    menu = "1. Setor Sampah\n2. Tarik Saldo\n3. Tukar Poin\n4. History dan Status\n0. Logout"
    print(tb.tabulate([[menu]], tablefmt="rounded_grid"))
    user = input("Masukkan pilihan: ")

    if user == "1":
      setor_sampah() 
    elif user == "2":
      tarik_saldo()
    elif user == "3":
      tukar_poin()
    elif user == "4":
      history_setoran_akun()
    elif user == "0":
      menu_utama()
    else:
      input("Pilihan Tidak Sesuai, Enter Untuk Mengulangi")
      continue

def setor_sampah():
    
    read_csv()
    df_sampah_organik.index += 1
    df_sampah_anorganik.index += 1
    poin_didapat = df_poin_dan_reward.loc[0,"poin/kg"]

    while True:
      os.system("cls")
      print("JENIS SAMPAH".center(23))
      menu = "1. Sampah Organik\n2. Sampah Anorganik\n0. Kembali"
      print(tb.tabulate([[menu]], tablefmt="rounded_grid"))
      user = input("Masukkan pilihan: ")

      if user == "1":
        os.system("cls")
        print("LIST SAMPAH ORGANIK".center(40))
        tabel = df_sampah_organik.loc[:,["nama","harga/kg"]]
        tabel["harga/kg"] = tabel["harga/kg"].apply(format_rupiah)
        print(tb.tabulate(tabel, headers=["No","Nama","Harga/Kg"],tablefmt="fancy_grid" ))
        print(f" Setiap setoran dengan berat 1 kg akan mendapatkan {poin_didapat} poin")
        print("\n0. Kembali")
        try:
          no_sampah = int(input("\nMasukkan nomor sampah: "))

          if no_sampah in df_sampah_organik.index:
            nama = df_sampah_organik.loc[no_sampah,"nama"]
            try:
              berat = float(input("Masukkan berat sampah yang ingin disetor (dalam kg): "))
              harga_sampah = df_sampah_organik.loc[no_sampah,"harga/kg"]
              uang = int(berat*harga_sampah)
              poin = int(berat * df_poin_dan_reward.loc[0,"poin/kg"])
              waktu = dt.datetime.now().strftime("%d %B %Y %H:%M")
            except ValueError:
              input("Berat harus angka, Enter Untuk Mengulangi")
              continue
            df = pd.DataFrame({"tanggal/waktu":[waktu],"username":[username],"jenis":["organik"],"nama":[nama],"berat":[berat],"uang":[uang],"poin":[poin],"status": ["checking"]})
            df.to_csv(history_setoran,mode="a",index=False,header=False)
            while True:
              os.system("cls")
              user = input("Apakah mau setor lagi? (y/t): ")

              if user.lower() == "y":
                break
              elif user.lower() == "t":
                os.system("cls")
                input("Setoran berhasil silahkan tunggu konfirmasi dari Pengepul, Status dapat dilihat di menu history dan status\nEnter Untuk Kembali")
                menu_supplier()
              else:
                input("Pilihan Tidak Sesuai, Enter Untuk Mengulangi")
                continue
          elif no_sampah == 0:
            continue
          else:
            input("Sampah tidak ditemukan, Enter Untuk Mengulangi")
            continue
        except ValueError:
          input("Nomor harus angka, Enter Untuk Mengulangi")
          continue
      elif user == "2":
        os.system("cls")

        tabel = df_sampah_anorganik.loc[:,["nama","harga/kg"]]
        tabel["harga/kg"] = tabel["harga/kg"].apply(format_rupiah)

        print("LIST SAMPAH ANORGANIK".center(30))
        print(tb.tabulate(tabel, headers=["No","Nama","Harga/kg"],tablefmt="fancy_grid" ))
        print(f" Setiap setoran dengan berat 1 kg akan mendapatkan {poin_didapat} poin")
        print("\n0. Kembali")
        try:
          no_sampah = int(input("\nMasukkan nomor sampah: "))

          if no_sampah in df_sampah_anorganik.index:
            nama = df_sampah_anorganik.loc[no_sampah,"nama"]
            try:
              berat = float(input("Masukkan berat sampah yang ingin disetor (dalam kg): "))
              harga_sampah = df_sampah_anorganik.loc[no_sampah,"harga/kg"]
              uang = int(berat*harga_sampah)
              poin = int(berat * df_poin_dan_reward.loc[0,"poin/kg"])
              waktu = dt.datetime.now().strftime("%d %B %Y %H:%M")
            except ValueError:
              input("Berat harus angka, Enter Untuk Mengulangi")
              continue

            df = pd.DataFrame({"tanggal/waktu":[waktu],"username":[username],"jenis":["anorganik"],"nama":[nama],"berat":[berat],"uang":[uang],"poin":[poin],"status":["checking"]})
            df.to_csv(history_setoran,mode="a",index=False,header=False)
            
            while True:
              os.system("cls")
              user = input("Apakah mau setor lagi? (y/t): ")

              if user.lower() == "y":
                break
              elif user.lower() == "t":
                os.system("cls")
                input("Setoran berhasil silahkan tunggu konfirmasi dari Pengepul, Status dapat dilihat di menu history dan status\nEnter Untuk Kembali")
                menu_supplier()
              else:
                input("Pilihan Tidak Sesuai, Enter Untuk Mengulangi")
                continue
          elif no_sampah == 0:
            continue
          else:
            input("Sampah tidak ditemukan, Enter Untuk Mengulangi")
            continue
        except ValueError:
          input("Nomor harus angka, Enter Untuk Mengulangi")
      elif user == "0":
        menu_supplier()
      else:
        input("Pilihan Tidak Sesuai, Enter Untuk Mengulangi")
        continue

def tukar_poin():
  while True:
    os.system("cls")

    read_csv()
    poin_akun = df_akun_supplier.loc[df_akun_supplier["username"]==username,"poin"].values[0]
    reward = df_poin_dan_reward.loc[0,"reward"]
    poin_ketentuan = df_poin_dan_reward.loc[0,"ketentuan"]
    tabel_reward = df_poin_dan_reward.loc[:,["reward","ketentuan"]]
    tabel_reward["reward"] = tabel_reward["reward"].apply(format_rupiah)

    print("TUKAR POIN".center(44))
    print(tb.tabulate(tabel_reward,showindex=False,headers=["Reward (Uang)","Poin yang diperlukan"], tablefmt="fancy_grid"))
    print(f"Poin kamu sekarang: {poin_akun} \n")
    menu = "1. Tukar poin\n0. Kembali"
    print(tb.tabulate([[menu]], tablefmt="rounded_grid"))
    user = input("Masukkan pilihan: ")

    if user == "1":
      while True:
        if poin_akun >= poin_ketentuan:
          os.system("cls")
          uang = df_akun_supplier.loc[df_akun_supplier["username"]==username,"saldo"]
          uang += reward
          poin_akun = poin_akun - poin_ketentuan
          waktu = dt.datetime.now().strftime("%d %B %Y %H:%M")

          df_akun_supplier.loc[df_akun_supplier["username"]==username,"saldo"] = uang 
          df_akun_supplier.to_csv(akun_supplier,index=False)
          df_akun_supplier.loc[df_akun_supplier["username"]==username,"poin"] = poin_akun
          df_akun_supplier.to_csv(akun_supplier,index=False)
          df = pd.DataFrame([[waktu,username, reward]])
          df.to_csv(history_penukaran,mode="a",index=False,header=False)

          print(f"Selamat kamu mendapatkan {format_rupiah(reward)} dan poin kamu sekarang menjadi {poin_akun}")
          user = input("\nMau tukarkan lagi(y/t): ")
          if user == "y":
            continue
          elif user == "t":
            break
          else:
            input("Pilihan Tidak Sesuai, Enter Untuk Mengulangi")
            continue
        else:
          os.system("cls")
          input("Poin tidak cukup, Enter Untuk kembali")
          break
    elif user == "0":
      menu_supplier()
    else:
      input("Pilihan Tidak Sesuai, Enter Untuk Mengulangi")
      continue

def tarik_saldo():
  while True:
    os.system("cls")

    saldo = df_akun_supplier.loc[df_akun_supplier["username"]==username,"saldo"].values[0]
    saldo = format_rupiah(saldo)

    print(f"Saldo kamu: {saldo}")
    menu = "1. Tarik saldo\n0. Kembali"
    print(tb.tabulate([[menu]], tablefmt="rounded_grid"))
    user = input("Masukkan pilihan: ")

    if user == "1":
      while True:
        os.system("cls")
        print(f"Saldo kamu: {saldo}")
        try:
          tarik = int(input("\nMasukkan jumlah saldo yang ingin ditarik: "))
          saldo = df_akun_supplier.loc[df_akun_supplier["username"]==username,"saldo"].values[0]

          if 0 < tarik <= saldo:
            waktu = dt.datetime.now().strftime("%d %B %Y %H:%M")
            df_History_penarikan = pd.DataFrame([[waktu,username,tarik,"processing"]])
            df_History_penarikan.to_csv(history_penarikan,mode="a",index=False,header=False)
            os.system("cls")
            input(f"Transaksi sedang diproses, status dapat dilihat di menu history dan status\nEnter untuk kembali")
            menu_supplier()
          else:
            input("Saldo tidak cukup, Enter untuk kembali")
            continue
        except ValueError:
          input("Saldo harus berupa angka, Enter untuk kembali")
          continue
    elif user == "0":
      menu_supplier()
    else:
      input("Pilihan Tidak Sesuai, Enter Untuk Mengulangi")
      continue

def history_setoran_akun():
  while True:
    os.system("cls")
    read_csv()
    df_setoran = df_history_setoran.loc[df_history_setoran["username"]==username].copy()
    df_penarikan = df_history_penarikan[df_history_penarikan["username"]==username].copy()
    df_penukaran = df_history_penukaran[df_history_penukaran["username"]==username].copy()

    print("HISTORY".center(35))
    menu = "1. History Setoran dan Status\n2. History Penarikan dan Status\n3. History Penukaran Poin\n0. Kembali"
    print(tb.tabulate([[menu]], tablefmt="rounded_grid"))
    user = input("Masukkan pilihan: ")

    if user == "1":
      os.system("cls")
      df_setoran["uang"] = df_setoran["uang"].apply(format_rupiah)
      df_setoran = df_setoran.reset_index(drop=True)
      df_setoran.index += 1

      print("HISTORY SETORAN".center(111))
      print(tb.tabulate(df_setoran,headers=["No","Tanggal/Waktu","Username","Jenis","Nama","Berat","Uang","Poin","Status"],tablefmt="fancy_grid"))
      input("Enter untuk kembali")
      continue
    elif user == "2":
      os.system("cls")
      df_penarikan = df_penarikan.reset_index(drop=True)
      df_penarikan["penarikan"] = df_penarikan["penarikan"].apply(format_rupiah)
      df_penarikan.index += 1

      print("HISTORY PENARIKAN".center(73))
      print(tb.tabulate(df_penarikan,headers=["No","Tanggal/Waktu","Username","Penarikan","Status"],tablefmt="fancy_grid"))
      input("Enter untuk kembali")
      continue
    elif user == "3":
      os.system("cls")
      df_penukaran = df_penukaran.reset_index(drop=True)
      df_penukaran["penukar"] = df_penukaran["penukar"].apply(format_rupiah)
      df_penukaran.index += 1
      
      print("HISTORY PENUKARAN".center(58))
      print(tb.tabulate(df_penukaran,headers=["No","Tanggal/Waktu","Username","Penukaran"],tablefmt="fancy_grid"))
      input("Enter untuk kembali")
      continue
    elif user == "0":
      menu_supplier()
    else:
      input("Pilihan Tidak Sesuai, Enter Untuk Mengulangi")
      continue

menu_utama()