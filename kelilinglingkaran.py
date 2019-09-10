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
   print('Objek kotak1')
   print('phi\t: ', Kelilinglingkaran1.phi)
   print('jarijari\t: ', Kelilinglingkaran1.jarijari)
   print('Keliling\t= ', Kelilinglingkaran1.hitungKeliling())

   # membuat objek kedua
   Kelilinglingkaran2 = Kelilinglingkaran(3.14, 7)

   # menggunakan objek kedua
   print("\nObjek kotak2")
   print("phi\t: ", Kelilinglingkaran2.phi)
   print("jarijari\t: ", Kelilinglingkaran2.jarijari)
   print("Keliling\t= ", Kelilinglingkaran2.hitungKeliling())

if __name__ == "__main__":
   main()
