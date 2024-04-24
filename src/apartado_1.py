import signal
import threading
import time

from phe import paillier
import random

# Generar un par de claves para el cifrado de Paillier
public_key, private_key = paillier.generate_paillier_keypair()

# Función para cifrar los datos de gastos de los clientes
def encrypt_expenses(expenses):
    encrypted_expenses = [public_key.encrypt(expense) for expense in expenses]
    return encrypted_expenses

# Función para sumar los datos cifrados
def sum_encrypted_data(encrypted_data):
    sum_encrypted = sum(encrypted_data, public_key.encrypt(0))
    return sum_encrypted

# Función para desencriptar el resultado de la suma
def decrypt_sum(sum_encrypted):
    sum_decrypted = private_key.decrypt(sum_encrypted)
    return sum_decrypted

# Función principal para realizar las pruebas
def testear_efectividad():
    # Realizar múltiples pruebas
    for i in range(5):
        print(f"Prueba {i+1}:")
        # Generar datos de gastos de ejemplo de los clientes
        client_expenses = [random.randint(100, 1000) for _ in range(random.randint(5, 20))]
        print("Gastos de los clientes:", client_expenses)

        # Cifrar los datos de gastos de los clientes
        encrypted_expenses = encrypt_expenses(client_expenses)

        # Sumar los datos cifrados
        sum_encrypted = sum_encrypted_data(encrypted_expenses)

        # Desencriptar el resultado de la suma
        sum_decrypted = decrypt_sum(sum_encrypted)
        print("Suma de los gastos cifrados:", decrypt_sum(sum_encrypted))

        # Verificar que la suma desencriptada es correcta
        expected_sum = sum(client_expenses)
        print("Suma esperada de los gastos:", expected_sum)
        if sum_decrypted == expected_sum:
            print("La suma desencriptada es correcta.\n")
        else:
            print("ERROR: La suma desencriptada es incorrecta.\n")

# Función para manejar la señal de tiempo límite
def timeout_handler(signum, frame):
    raise TimeoutError("La función ha superado el límite de tiempo")

def testear_rendimiento():
    # Generar un conjunto de datos grande para el rendimiento
    for i in range(1, 10):
        client_expenses = [random.randint(100, 1000) for _ in range(i*5)]

        # Cifrar los datos y medir el tiempo
        start_time = time.time()
        encrypted_expenses = encrypt_expenses(client_expenses)
        encryption_time = time.time() - start_time

        # Sumar los datos cifrados y medir el tiempo
        start_time = time.time()
        sum_encrypted = sum_encrypted_data(encrypted_expenses)
        sum_time = time.time() - start_time

        # Desencriptar el resultado de la suma y medir el tiempo
        decryption_time = None
        t = threading.Timer(5, timeout_handler)
        t.start()
        try:
            start_time = time.time()
            sum_decrypted = decrypt_sum(sum_encrypted)
            decryption_time = time.time() - start_time
        except TimeoutError as e:
            print(f"La función ha superado el límite de tiempo ({e})")
            sum_decrypted = None
            i = 9999
        finally:
            t.cancel()  # Cancelar el temporizador después de que la función haya terminado

        if decryption_time is not None:
            # Verificar que la suma desencriptada es correcta
            expected_sum = sum(client_expenses)

            print("Resultados de la prueba de rendimiento:")
            print(f"Cantidad de datos: {i*5}")
            print(f"Tiempo de cifrado: {encryption_time:.6f} segundos")
            print(f"Tiempo de suma: {sum_time:.6f} segundos")
            print(f"Tiempo de desencriptación: {decryption_time:.6f} segundos")
            print("Suma esperada de los gastos:", expected_sum)
            print("Suma desencriptada:", sum_decrypted)
            if sum_decrypted == expected_sum:
                print("La suma desencriptada es correcta.")
            else:
                print("ERROR: La suma desencriptada es incorrecta.")
            print("\n")


if __name__ == "__main__":
    testear_efectividad()
    testear_rendimiento()
