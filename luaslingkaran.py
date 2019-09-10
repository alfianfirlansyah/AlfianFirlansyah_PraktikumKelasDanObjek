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
   print('Objek kotak1')
   print('phi\t: ', Luaslingkaran1.phi)
   print('jarijari\t: ', Luaslingkaran1.jarijari)
   print('Luas\t= ', Luaslingkaran1.hitungLuas())

   # membuat objek kedua
   Luaslingkaran2 = Luaslingkaran(3.14, 7)

   # menggunakan objek kedua
   print("\nObjek kotak2")
   print("phi\t: ", Luaslingkaran2.phi)
   print("jarijari\t: ", Luaslingkaran2.jarijari)
   print("Luas\t= ", Luaslingkaran2.hitungLuas())

if __name__ == "__main__":
   main()
