print('------nomor1-------')

kendaraan=["cbr","motor","hitam","250","2"]
kendaraan.append("40juta")
kendaraan.append("cbr")
kendaraan.insert(2,"Honda")
print(kendaraan)

print('------nomor2------')

rumus=int(input("rumus apa yang kamu kerjakan:"))
match rumus:
    case 1:
        print("luas persegi(sisi*sisi)")
        sisi1= float(input("masukan sisi 1:"))
        sisi2= float(input("masukan sisi 2:"))
        luas_persegi= sisi1*sisi2
        print("luasnya adalah", int(luas_persegi))
    case 2:
        print("luas lingkaran(3.14.r*r)")
        phi=3.14
        r=float(input("masukan jari-jari:"))
        luas_lingkkaran= phi*r*r
        print("luasnya adalah", int(luas_lingkkaran))
    case 3:
        print("luas_segitiga(0,5*a*t)")
        setengah=0.5
        a = float(input("masukan alas: "))
        t = float(input("masukan tinggi: "))
        luas_segitiga = setengah*a*t
        print("luasnya adalah", int(luas_segitiga))
    case _ :
        print("salah pilih angka")
