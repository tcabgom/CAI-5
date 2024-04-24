import time

from phe import paillier
import random

KEY_LENGTH = 1024

# Generar un par de claves para el cifrado de Paillier
public_key, private_key = paillier.generate_paillier_keypair(n_length=KEY_LENGTH)

# Función para cifrar un conjunto de datos
def encrypt_data(data_set):
    encrypted_set = [public_key.encrypt(data) for data in data_set]
    return encrypted_set

# Función para descifrar un conjunto de datos
def decrypt_data(encrypted_set):
    decrypted_set = [private_key.decrypt(data) for data in encrypted_set]
    return decrypted_set

# Función para cifrar los datos de gastos de los clientes
def encrypt_expenses(expenses):
    return encrypt_data(expenses)

# Función para cifrar el conjunto de delincuentes identificados
def encrypt_criminals(criminals):
    return encrypt_data(criminals)

# Función para buscar las personas comunes entre delincuentes y pasajeros del vuelo
def busca_delincuentes(delincuentes_encriptados, pasajeros_encriptados):
    delincuentes_desencriptados = set(decrypt_data(delincuentes_encriptados))
    pasajeros_desencriptados = set(decrypt_data(pasajeros_encriptados))
    delincuentes_encontrados = delincuentes_desencriptados.intersection(pasajeros_desencriptados)
    return delincuentes_encontrados

def generate_random_people(client_amount, criminals_amount, infiltrated_criminals):
    people_set = set()
    criminals_set = set()

    # Asignar identificadores únicos a las personas
    for i in range(client_amount):
        people_set.add(i)

    # Asignar identificadores únicos a los delincuentes
    for i in range(client_amount, client_amount + criminals_amount):
        criminals_set.add(i)

    # Seleccionar algunos delincuentes para que sean también personas
    for _ in range(infiltrated_criminals):
        criminal_id = random.randint(client_amount, client_amount + criminals_amount - 1)
        people_set.add(criminal_id)

    return people_set, criminals_set

def testeo_funcionalidad():
    # Conjunto de delincuentes identificados
    clientes, criminales = generate_random_people(500, 20, 5)

    # Cifrar los conjuntos de delincuentes y pasajeros del vuelo
    encrypted_delincuentes = encrypt_criminals(criminales)
    encrypted_pasajeros_vuelo = encrypt_data(clientes)

    # Llamada a la función buscaComunes
    delincuentes_encontrados = busca_delincuentes(encrypted_delincuentes, encrypted_pasajeros_vuelo)

    # Resultados
    print("Delincuentes encontrados entre pasajeros del vuelo:")
    print(delincuentes_encontrados)

def testeo_rendimiento():
    # Lista para almacenar los tiempos de ejecución
    tiempos_ejecucion = []

    for client_amount in [10, 25, 50, 100, 250, 500, 1000]:
        # Conjunto de delincuentes identificados
        clientes, criminales = generate_random_people(client_amount, 20, round(client_amount * 0.1))
        # Medir el tiempo de ejecución
        start_time = time.time()

        # Cifrar los conjuntos de delincuentes y pasajeros del vuelo
        encrypted_delincuentes = encrypt_criminals(criminales)
        encrypted_pasajeros_vuelo = encrypt_data(clientes)

        # Llamada a la función buscaComunes
        _ = busca_delincuentes(encrypted_delincuentes, encrypted_pasajeros_vuelo)
        # Calcular el tiempo de ejecución y agregarlo a la lista
        execution_time = time.time() - start_time
        tiempos_ejecucion.append((client_amount, execution_time))
        print(f"Tiempo de ejecución para {client_amount} clientes: {execution_time:.6f} segundos")


if __name__ == "__main__":
    testeo_funcionalidad()
    testeo_rendimiento()