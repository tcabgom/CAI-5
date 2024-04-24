import signal
import threading
import time

from phe import paillier
import random

KEY_LENGTH = 1024

# Generar un par de claves para el cifrado de Paillier
public_key, private_key = paillier.generate_paillier_keypair(n_length=KEY_LENGTH)

# Función para cifrar los datos de gastos de los clientes
def encrypt_expenses(expenses):
    encrypted_expenses = [public_key.encrypt(expense) for expense in expenses]
    return encrypted_expenses

# Función para obtener el dato cifrado en la posición especificada
def get_encrypted_data_at_position(encrypted_data, position):
    return encrypted_data[position]

# Función para desencriptar el dato en la posición especificada
def decrypt_data_at_position(encrypted_data, position):
    decrypted_data = private_key.decrypt(encrypted_data[position])
    return decrypted_data

# Función principal para realizar las pruebas de efectividad
def testear_efectividad():
    # Realizar múltiples pruebas
    for i in range(5):
        print(f"Prueba {i+1}:")
        # Generar datos de gastos de ejemplo de los clientes
        client_expenses = [random.randint(100, 1000*pow(10,i)) for _ in range(random.randint(5, 20))]
        print("Gastos de los clientes:", client_expenses)

        # Cifrar los datos de gastos de los clientes
        encrypted_expenses = encrypt_expenses(client_expenses)

        # Seleccionar una posición aleatoria para obtener el dato cifrado
        position = random.randint(0, len(encrypted_expenses) - 1)

        # Obtener el dato cifrado en la posición especificada
        encrypted_data_at_position = get_encrypted_data_at_position(encrypted_expenses, position)
        print(f"Dato cifrado en la posición {position}:", encrypted_data_at_position)

        # Desencriptar el dato en la posición especificada
        decrypted_data_at_position = decrypt_data_at_position(encrypted_expenses, position)
        print(f"Dato desencriptado en la posición {position}:", decrypted_data_at_position, "\n")

# Función para manejar la señal de tiempo límite
def timeout_handler(signum, frame):
    raise TimeoutError("La función ha superado el límite de tiempo")

# Función principal para realizar las pruebas de rendimiento
def testear_rendimiento():
    # Generar un conjunto de datos grande para el rendimiento
    for i in range(1, 11):
        client_expenses = [random.randint(100, 1000) for _ in range(i*5)]

        # Cifrar los datos y medir el tiempo
        start_time = time.time()
        encrypted_expenses = encrypt_expenses(client_expenses)
        encryption_time = time.time() - start_time

        # Seleccionar una posición aleatoria para obtener el dato cifrado
        position = random.randint(0, len(encrypted_expenses) - 1)

        # Medir el tiempo para obtener el dato cifrado en la posición especificada
        start_time = time.time()
        encrypted_data_at_position = get_encrypted_data_at_position(encrypted_expenses, position)
        getting_time = time.time() - start_time

        # Desencriptar el dato en la posición especificada y medir el tiempo
        start_time = time.time()
        decrypted_data_at_position = decrypt_data_at_position(encrypted_expenses, position)
        decryption_time = time.time() - start_time

        if decryption_time is not None:
            print("\nResultados de la prueba de rendimiento:")
            print(f"Cantidad de datos: {i*5}")
            print(f"Tiempo de cifrado: {encryption_time:.6f} segundos")
            print(f"Tiempo de obtener dato cifrado: {getting_time:.6f} segundos")
            print(f"Tiempo de desencriptación: {decryption_time:.6f} segundos\n")
            print(f"Tiempo total: {encryption_time+getting_time+decryption_time:.6f} segundos\n")
            print(f"Dato desencriptado en la posición {position}:", decrypted_data_at_position)
            print("\n")


if __name__ == "__main__":
    testear_efectividad()
    testear_rendimiento()