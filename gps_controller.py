
def navigate(lat, lon):
	latto =	23.861720
	longto = 90.396230
	dell_lat = abs(lat-(latto*1000000))
	dell_long = abs(lon-(longto*1000000))
	print(int(dell_lat))
	print(int(dell_long))
	if dell_lat<20 and dell_long<30:
		return True
	if dell_lat<30 and dell_long<20:
		return True

	else:
		return False

for i in range(23861858, 23861000, -50):
	stat = navigate(i,90396203)
	print(stat)
	if stat == True:
		break

