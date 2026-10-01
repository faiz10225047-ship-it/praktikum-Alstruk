def cek_bilangan_prima(n):
  # Bilangan kurang dari atau sama dengan 1 bukan bilangan prima
  if n <= 1:
    return False

  # Cek pembagi dari 2 hingga akar kuadrat dari n
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False

  return True


# Program Utama
if _name_ == "_main_":
  try:
    angka = int(input("Masukkan suatu bilangan bulat: "))
    if cek_bilangan_prima(angka):
      print(f"{angka} adalah bilangan prima.")
    else:
      print(f"{angka} bukan bilangan prima.")
  except ValueError:
    print("Input tidak valid! Harap masukkan angka bulat.")