def weight_conversion():
    berat = int(input("masukan angka >"))
    satuan = input("dalam satuan apa berat yang anda masukan ? (K untuk KG, L untuk LBS) >")

    if satuan.lower() == 'l':
        print(f"berat anda dikonversi menjadi kilogram adalah {round(berat*0.453592)} kg")
    elif satuan.lower() == 'k':
        print(f"berat anda dikonversi menjadi pons adalah {round(berat*2.20462)} lbs")