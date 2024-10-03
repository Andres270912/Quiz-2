
#Ingreso de datos
nombre = input("Ingrese el nombre del empleado: ")
dias_laborados = int(input("Ingrese el numero de dias laborados: "))
salario = float(input("Ingrese el salario: "))

#Calculo de la prima
prima = salario * dias_laborados / 360

#Calculo de cesantias
cesantias = salario * dias_laborados / 360

#Calculo de intereses cesantias
intereses_cesantias = cesantias * 0.12 / dias_laborados

#Calculo de vacaciones
vacaciones = salario * dias_laborados / 720

#Calculo de la liquidacion
liquidacion = prima + cesantias + intereses_cesantias + vacaciones

#Resultados
print(f"Señor: {nombre} para los {dias_laborados} dias laborados y salario {salario},su liquidacion se compone asi:"
      f"\nPrima: {prima:.2f}\nCesantias: {cesantias:.2f}\nIntereses cesantias: {intereses_cesantias:.2f}\nVacaciones: {vacaciones:.2f}\nLiquidacion: {liquidacion:.2f}")


