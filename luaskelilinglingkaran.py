class Luaslingkaran(object):
   def __init__(self, phi, r):
      self.phi = phi
      self.jarijari = r
   def hitungLuas(self):
      return self.phi * self.jarijari**2

def main():
   # membuat objek pertama
   Luaslingkaran1 = Luaslingkaran(3.14, 22)

   # menggunakan objek pertama
   print('Objek luas kotak1')
   print('phi\t: ', Luaslingkaran1.phi)
   print('jarijari\t: ', Luaslingkaran1.jarijari)
   print('Luas\t= ', Luaslingkaran1.hitungLuas())

   # membuat objek kedua
   Luaslingkaran2 = Luaslingkaran(3.14, 7)

   # menggunakan objek kedua
   print("\nObjek luas kotak2")
   print("phi\t: ", Luaslingkaran2.phi)
   print("jarijari\t: ", Luaslingkaran2.jarijari)
   print("Luas\t= ", Luaslingkaran2.hitungLuas())

if __name__ == "__main__":
   main()

class Kelilinglingkaran(object):
   def __init__(self, phi, r):
      self.phi = phi
      self.jarijari = r
   def hitungKeliling(self):
      return 2 * self.phi * self.jarijari

def main():
   # membuat objek pertama
   Kelilinglingkaran1 = Kelilinglingkaran(3.14, 22)

   # menggunakan objek pertama
   print('Objek keliling kotak1')
   print('phi\t: ', Kelilinglingkaran1.phi)
   print('jarijari\t: ', Kelilinglingkaran1.jarijari)
   print('Keliling\t= ', Kelilinglingkaran1.hitungKeliling())

   # membuat objek kedua
   Kelilinglingkaran2 = Kelilinglingkaran(3.14, 7)

   # menggunakan objek kedua
   print("\nObjek keliling kotak2")
   print("phi\t: ", Kelilinglingkaran2.phi)
   print("jarijari\t: ", Kelilinglingkaran2.jarijari)
   print("Keliling\t= ", Kelilinglingkaran2.hitungKeliling())

if __name__ == "__main__":
   main()

