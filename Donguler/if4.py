# Username - password kontrol

username = input("Kullanıcı Adı: ")
password = input("Parola: ")

if username == "admin" and password == "password":
    print("Giriş Başarılı")
else:
    print("Yanlış kullanıcı adı veya parola")
