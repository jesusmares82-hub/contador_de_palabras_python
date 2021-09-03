# Programa que solicita al usuario cuantas horas trabaja y el pago por hora
# para calcular el pago el sueldo

def computepay(hours, pagoxhora):
    hours = float(hours)
    pagoxhora = float(pagoxhora)
    if float(hours) <= 40:
        sueldo = float(hours) * float(pagoxhora)
    else:
        horas_extra = float(hours) - 40
        pagoxhora_extra = float(pagoxhora) * 0.5
        sueldo = ((float(hours) - float(horas_extra)) * float(pagoxhora)) + (
                float(horas_extra) * (float(pagoxhora) + float(pagoxhora_extra)))
    return sueldo


horas = input("Ingresa las horas:")
pagoxhora = input("Ingresa el pago por hora:")
try:
    print("El pago es: ",computepay(horas, pagoxhora))
except:
    print("Error, por favor ingresar números.")


