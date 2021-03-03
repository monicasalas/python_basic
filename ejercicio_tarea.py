dia = 5
mes = 10
anio = 1994

dia_hoy=2
mes_hoy=3
anio_hoy=2021

edad = 0

if anio < anio_hoy:
    edad = anio_hoy - anio 
    if mes > mes_hoy:
        edad -= 1 
    elif  dia > dia_hoy:
        print("")
else:
    print("Aun no es tú cumpleaños")
print(f'Tienes {edad} años')

print("Perteneces a la generación")
if anio >= 1920 and anio <= 1939:
    print("'SILENCIOSA'")
elif anio >= 1940 and anio <= 1959:
    print("'BABY BOOMER'")
elif anio >= 1960 and anio <= 1979:
    print("'X'")
elif anio >= 1980 and anio <= 1989:
    print("'Y O MILLENIAL'")
elif anio >= 1990 :
    print("'Z'")
else:
    print("ZOOMBIE")


