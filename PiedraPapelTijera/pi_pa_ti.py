# coding: utf-8
salir = "false"
num = 31

while salir == "false" :
	if num%7 == 3 and num%5 == 1 :
		print "jugador1=pi, jugador2=pa. Gana jugador2"
	if num%7 == 4 and num%5 == 2 :
		print "jugador1=pa, jugador2=pa. Es un empate"
	if num%7 == 5 and num%5 == 3 :
		print "jugador1=pa, jugador2=ti. Gana jugador2"
	if num%7 == 6 and num%5 == 4 :
		print "jugador1=pi, jugador2=pi. Es un empate"
	if num%7 == 0 and num%5 == 0 :
		print "jugador1=ti, jugador2=pa. Gana jugador1"
	if num%7 == 1 and num%5 == 1 :
		print "jugador1=ti, jugador2=pa, gana jugador1"
	if num%7 == 2 and num%5 == 2 :
		print "jugador1=pi, jugador2=pa. Gana jugador2"
	if num%7 == 3 and num%5 == 3 :
		print "jugador1=pi, jugador2=ti. Gana jugador1"
	if num%7 == 4 and num%5 == 4 :
		print "jugador1=pa, jugador2=pi. Gana jugador1"
	if num%7 == 5 and num%5 == 0 :
		print "jugador1=pa, jugador2=pa. Es un empate"
	if num%7 == 6 and num%5 == 1 :
		print "jugador1=pi, jugador2=pa. Gana jugador2"
	if num%7 == 0 and num%5 == 2 :
		print "jugador1=ti, jugador2=pa. Gana jugador1"
	if num%7 == 1 and num%5 == 3 :
		print "jugador1=ti, jugador2=ti. Es un empate"
	if num%7 == 2 and num%5 == 4 :
		print "jugador1=pi, jugador2=pi. Es un empate"
	if num%7 == 3 and num%5 == 0 :
		print "jugador1=pi, jugador2=pa. Gana jugador2"
	if num%7 == 4 and num%5 == 1 :
		print "jugador1=pa, jugador2=pa. Es un empate"
	if num%7 == 5 and num%5 == 2 :
		print "jugador1=pa, jugador2=pa. Es un empate"
	if num%7 == 6 and num%5 == 3 :
		print "jugador1=pi, jugador2=ti. Gana jugador1"
	if num%7 == 0 and num%5 == 4 :
		print "jugador1=ti, jugador2=pi. Gana jugador2"
	if num%7 == 1 and num%5 == 0 :
		print "jugador1=ti, jugador2=pa. Gana jugador1"
	if num%7 == 2 and num%5 == 1 :
		print "jugador1=pi, jugador2=pa. Gana jugador2"
	if num%7 == 3 and num%5 == 2 :
		print "jugador1=pi, jugador2=pa. Gana jugador2"
	if num%7 == 4 and num%5 == 3 :
		print "jugador1=pa, jugador2=ti. Gana jugador2"
	if num%7 == 5 and num%5 == 4 :
		print "jugador1=pa, jugador2=pi. Gana jugador1"
	if num%7 == 6 and num%5 == 0 :
		print "jugador1=pi, jugador2=pa. Gana jugador2"
	if num%7 == 0 and num%5 == 1 :
		print "jugador1=ti, jugador2=pa. Gana jugador1"
	if num%7 == 1 and num%5 == 2 :
		print "jugador1=ti, jugador2=pa. Gana jugador1"
	if num == 57 :
		salir = "true"
	num = num + 1
