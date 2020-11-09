# https://github.com/alpkeskin
import random
import time
class Colors:
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def banner():
	print(f"{Colors.BOLD}-------------{Colors.ENDC}")
	print(f"{Colors.BOLD}SAHTE KİMLİK OLUŞTURUCUSU{Colors.ENDC}")
	print("! Eğitim ve Eğlence amaçlı oluşturulmuştur !")
	print("github.com/alpkeskin")
	print(f"{Colors.BOLD}-------------{Colors.ENDC}")
	print("Kimlik oluşturuluyor...")
	time.sleep(2)



def main():
	banner()
	print("-------------")
	print(f"{Colors.WARNING}KİŞİSEL VERİLER{Colors.ENDC}")
	print("-------------")
	cinsiyetliste = ["Erkek","Kadın"]
	cinsiyet = random.choice(cinsiyetliste)
	if (cinsiyet == "Erkek"):
		isimdosya = open('erkekisimlistesi.txt').read().splitlines()
		isim =random.choice(isimdosya)
	if (cinsiyet == "Kadın"):
		isimdosya = open('kadinisimlistesi.txt').read().splitlines()
		isim =random.choice(isimdosya)
	soyisimdosya = open('soyisimler.txt').read().splitlines()
	soyisim =random.choice(soyisimdosya)
	annesoyad =random.choice(soyisimdosya)
	gun = random.randint(1,30)
	aylar = ["Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran", "Temmuz", "Ağustos", "Eylül", "Ekim", "Kasım", "Aralık"]
	ay =random.choice(aylar)
	yil = random.randint(1970,2002)
	sehirdosya = open('sehirler.txt').read().splitlines()
	sehir =random.choice(sehirdosya)
	epostaliste = ["@gmail.com","@outlook.com","@icloud.com","@hotmail.com"]
	eposta = random.choice(epostaliste)
	telefonliste = ["501", "505", "506", "507", "551","530", "531", "532", "533", "534", "535","540", "541", "542", "543", "544", "545"]
	telefon =random.choice(telefonliste)
	telefon1 = random.randint(400,900)
	telefon2 = random.randint(10,99)
	telefon3 = random.randint(10,99)
	CCadliste = ["Visa","MasterCard"]
	CCad = random.choice(CCadliste)
	bitisyil = random.randint(2023,2029)
	bitisay = random.randint(1,12)
	cckodu = random.randint(101,999)
	meslekdosya = open('meslekler.txt').read().splitlines()
	meslek =random.choice(meslekdosya)
	kangrupları = ["AB Rh+", "AB Rh-", "A Rh+", "A Rh-", "B Rh+", "B Rh-", "O Rh+", "O Rh-"]
	kan =random.choice(kangrupları)
	arabadosya = open('arabalar.txt').read().splitlines()
	araba =random.choice(arabadosya)
	renkdosya = open('renkler.txt').read().splitlines()
	renk =random.choice(renkdosya)

	#-------------------------------
	print(f"{Colors.OKGREEN}Cinsiyet : {Colors.ENDC}{Colors.ENDC}"+cinsiyet)
	print(f"{Colors.OKGREEN}Ad ve Soyad : {Colors.ENDC}"+isim.capitalize()+" "+soyisim.capitalize())
	print(f"{Colors.OKGREEN}Baş Harfler : {Colors.ENDC}"+isim[0]+"."+soyisim[0])
	print(f"{Colors.OKGREEN}Anne Kızlık Soyadı : {Colors.ENDC}"+annesoyad.capitalize())
	print(f"{Colors.OKGREEN}Doğum Günü : {Colors.ENDC}"+str(gun)+" "+ay+" "+str(yil)+" (Yaş : "+str(2020-yil)+")")
	print(f"{Colors.OKGREEN}Doğum Yeri : {Colors.ENDC}"+sehir)
	print("-------------")
	print(f"{Colors.WARNING}ONLINE{Colors.ENDC}")
	print("-------------")
	print(f"{Colors.OKGREEN}Kullanıcı Adı : {Colors.ENDC}"+isim[0:3].capitalize()+soyisim[0:3].lower()+str(gun))
	print(f"{Colors.OKGREEN}Şifre : {Colors.ENDC}"+isim[2:4]+str(yil)+soyisim[2].lower()+"*")
	print(f"{Colors.OKGREEN}E-Posta : {Colors.ENDC}"+isim[0:3].capitalize()+soyisim[0:3].lower()+str(gun)+eposta)
	print(f"{Colors.OKGREEN}Telefon :{Colors.ENDC} +90 "+str(telefon)+" "+str(telefon1)+" "+str(telefon2)+" "+str(telefon3))
	print("-------------")
	print(f"{Colors.WARNING}FİNANS{Colors.ENDC}")
	print("-------------")
	if (CCad == "Visa"):
		visaliste = open('visa.txt').read().splitlines()
		Visa =random.choice(visaliste)
		print(f"{Colors.OKGREEN}Kredi Kartı : {Colors.ENDC}"+CCad+" "+Visa)
		print(f"{Colors.OKGREEN}Bitiş Tarihi :{Colors.ENDC} 0"+str(bitisay)+"/"+str(bitisyil))
		print(f"{Colors.OKGREEN}CVV2 : {Colors.ENDC}"+str(cckodu))
	elif (CCad == "MasterCard"):
		mastercardliste = open('mastercard.txt').read().splitlines()
		MasterCard =random.choice(mastercardliste)
		print(f"{Colors.OKGREEN}Kredi Kartı : {Colors.ENDC}"+CCad+" "+MasterCard)
		print(f"{Colors.OKGREEN}Bitiş Tarihi :{Colors.ENDC} 0"+str(bitisay)+"/"+str(bitisyil))
		print(f"{Colors.OKGREEN}CVC2 : {Colors.ENDC}"+str(cckodu))
	else:
		print()
	print("-------------")
	print(f"{Colors.WARNING}MESLEK{Colors.ENDC}")
	print("-------------")
	print(f"{Colors.OKGREEN}Meslek : {Colors.ENDC}"+meslek)
	print("-------------")
	print(f"{Colors.WARNING}FİZİKSEL ÖZELLİKLER{Colors.ENDC}")
	print("-------------")
	if (cinsiyet == "Erkek"):
		boy = random.randint(160,200)
		kilo = random.randint(65,105)
		print(f"{Colors.OKGREEN}Boy : {Colors.ENDC}"+str(boy)+" cm")
		print(f"{Colors.OKGREEN}Kilo : {Colors.ENDC}"+str(kilo)+" kg")
		print(f"{Colors.OKGREEN}Kan grubu : {Colors.ENDC}"+kan)
	elif (cinsiyet == "Kadın"):
		boy = random.randint(150,180)
		kilo = random.randint(50,80)
		print(f"{Colors.OKGREEN}Boy : {Colors.ENDC}"+str(boy)+" cm")
		print(f"{Colors.OKGREEN}Kilo : {Colors.ENDC}"+str(kilo)+" kg")
		print(f"{Colors.OKGREEN}Kan grubu : {Colors.ENDC}"+kan)
	print("-------------")
	print(f"{Colors.WARNING}DİĞER{Colors.ENDC}")
	print("-------------")
	print(f"{Colors.OKGREEN}Araba : {Colors.ENDC}"+araba)
	print(f"{Colors.OKGREEN}Favori Renk : {Colors.ENDC}"+renk)
	print(f"{Colors.OKGREEN}Uğurlu Sayı : {Colors.ENDC}"+str(random.randint(0,10)))

main()