numero = int(input("Por favor, entre com o número de segundos que deseja converter: "))

days = numero // (60*60*24)
hours = numero % (60*60*24) // (60*60)
minutes = numero % (60*60) // (60)
sec = numero % (60)


print(days, "dias,", hours, "horas,", minutes, "minutos e", sec, "segundos.")