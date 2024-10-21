
def pagomensual(P, tasaanual, plazoaños):
    r = tasaanual / 100 / 12
    n = plazoaños * 12
    
    M = P * (r * (1 + r) ** n) / ((1 + r) ** n - 1)
    
    return M

P = 250000
tasaanual = 5 
plazoaños = 30

Pagomensual = pagomensual(P, tasaanual, plazoaños)

print(f"El pago mensual para un préstamo de {P}€ a una tasa anual de {tasaanual}% por {plazoaños} años es: {Pagomensual:.2f}€")
