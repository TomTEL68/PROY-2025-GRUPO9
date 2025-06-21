contador_mala_posturas = 0
#Como en el codigo nuestro tenemos un bucle "for in range(5) no va en el codigo final"
for i in range(5):
    Rango = int(input("Ángulo de inclinación "))
    if Rango < 70 or Rango > 110:
        contador_mala_posturas += 1

print("Malas posturas detectadas:", contador_mala_posturas)