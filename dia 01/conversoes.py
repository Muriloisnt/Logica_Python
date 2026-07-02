

from conversoes import celsius_fahrenheit, metros_quilometros

def main() -> None:
    #exemplos de uso
    c = 25
    m = 1500
    print(f'{c} °C = {celsius_fahrenheit(c):.2f}°F')
    print(f'{m} m = {metros_quilometros(m):.3f} km')

# ponto de entrada do programa
# so executa main() se este arquivo for o script principal
if __name__ == "__main__":
    main()