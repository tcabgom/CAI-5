from phe import paillier
import random

KEY_LENGTH = 2048

# Generar un par de claves para el cifrado de Paillier
public_key, private_key = paillier.generate_paillier_keypair(n_length=KEY_LENGTH)

# Función para cifrar los precios de los vuelos utilizando Homomorphic Encryption
def encrypt_flight_prices(prices):
    encrypted_prices = [public_key.encrypt(price) for price in prices]
    return encrypted_prices

# Función para recuperar el precio de un vuelo específico de forma privada
def get_encrypted_price(flight_index, encrypted_prices):
    encrypted_price = encrypted_prices[flight_index]
    return encrypted_price

# Función para desencriptar el precio de un vuelo
def decrypt_price(encrypted_price):
    decrypted_price = private_key.decrypt(encrypted_price)
    return decrypted_price

# Función para testear la eficiencia y eficacia del protocolo
def testear_protocolo():
    # Generar precios de vuelos aleatorios (simulados)
    flight_prices = [random.randint(100, 1000) for _ in range(10)]

    # Cifrar los precios de vuelos
    encrypted_prices = encrypt_flight_prices(flight_prices)

    # Realizar pruebas de recuperación de precios
    for i in range(len(flight_prices)):
        encrypted_price = get_encrypted_price(i, encrypted_prices)
        decrypted_price = decrypt_price(encrypted_price)
        if decrypted_price == flight_prices[i]:
            print(f"Prueba {i+1}: El precio desencriptado del vuelo {i+1} es correcto.")
        else:
            print(f"Prueba {i+1}: Error al desencriptar el precio del vuelo {i+1}.")

# Párrafo para la Política de Privacidad
politica_privacidad_precios = (
    "En nuestra compañía, respetamos su privacidad cuando solicita los precios de nuestros vuelos. "
    "Utilizamos tecnologías de cifrado avanzadas para garantizar que sus solicitudes sean privadas y seguras. "
    "No realizamos ningún seguimiento de sus consultas de precios, ya que su privacidad es nuestra prioridad."
)

# Ejecutar las pruebas y mostrar la Política de Privacidad
if __name__ == "__main__":
    print("Protocolo recomendado para preservar la privacidad en la recuperación de precios de vuelos:")
    testear_protocolo()
    print("\nPárrafo para la Política de Privacidad:")
    print(politica_privacidad_precios)