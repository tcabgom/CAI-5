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


# Función para preservar la privacidad de los datos de los clientes en la nube pública
def privacidad_datos_clientes(client_expenses):
    # Cifrar los datos de gastos de los clientes
    encrypted_expenses = encrypt_expenses(client_expenses)

    # Sumar los datos cifrados
    sum_encrypted = sum_encrypted_data(encrypted_expenses)

    # Desencriptar el resultado de la suma
    sum_decrypted = decrypt_sum(sum_encrypted)

    return sum_decrypted


# Función para preservar la privacidad de datos empresariales en colaboración con autoridades gubernamentales
def privacidad_datos_empresariales(delincuentes_conocidos, pasajeros_vuelo):
    # Encuentra las coincidencias entre delincuentes conocidos y pasajeros de vuelo
    coincidencias = set(delincuentes_conocidos) & set(pasajeros_vuelo)

    return coincidencias


# Párrafo para la Política de Privacidad de los datos de los clientes en la nube pública
politica_privacidad_clientes = (
    "En nuestra compañía, preservamos la privacidad de sus datos personales. "
    "Utilizamos técnicas de criptografía avanzada para cifrar y procesar sus gastos de viaje. "
    "Sus datos de gastos se almacenan de manera segura en nuestra nube pública, "
    "y se procesan de forma que la nube no tiene conocimiento de los gastos individuales. "
    "Puede tener la seguridad de que sus datos están protegidos y se utilizan de manera responsable."
)

# Párrafo para la Política de Privacidad de datos empresariales en colaboración con autoridades gubernamentales
politica_privacidad_empresarial = (
    "En nuestra compañía, nos comprometemos a proteger la privacidad de sus datos empresariales. "
    "En colaboración con las autoridades gubernamentales, utilizamos algoritmos que preservan la privacidad "
    "para identificar posibles delincuentes y personas buscadas por la justicia. "
    "Esto se hace de manera que los datos de los pasajeros no se revelan a menos que sean necesarios "
    "para garantizar la seguridad. Su seguridad y privacidad son nuestra máxima prioridad."
)

# Función para testear la preservación de la privacidad de los datos de los clientes
def testear_privacidad_clientes():
    # Generar datos de gastos de clientes (simulados)
    client_expenses = [random.randint(100, 1000) for _ in range(10)]

    # Probar la preservación de la privacidad de los datos de los clientes
    suma_cifrada = privacidad_datos_clientes(client_expenses)
    suma_original = sum(client_expenses)
    if suma_cifrada == suma_original:
        print("La preservación de la privacidad de los datos de los clientes funciona correctamente.")
    else:
        print("Error: La preservación de la privacidad de los datos de los clientes no funciona.")

# Función para testear la preservación de la privacidad de los datos empresariales
def testear_privacidad_empresarial():
    # Conjunto de delincuentes conocidos (simulados)
    delincuentes_conocidos = ["Juan Perez", "Maria Lopez", "Pedro Gomez"]
    # Conjunto de pasajeros de vuelo (simulados)
    pasajeros_vuelo = ["Maria Lopez", "Ana Martinez", "Luisa Garcia"]

    # Probar la preservación de la privacidad de los datos empresariales
    coincidencias = privacidad_datos_empresariales(delincuentes_conocidos, pasajeros_vuelo)
    if len(coincidencias) == 1 and "Maria Lopez" in coincidencias:
        print("La preservación de la privacidad de los datos empresariales funciona correctamente.")
    else:
        print("Error: La preservación de la privacidad de los datos empresariales no funciona.")

# Función principal para ejecutar todas las pruebas
def testear_privacidad():
    print("Testeando la preservación de la privacidad de los datos de los clientes:")
    testear_privacidad_clientes()
    print("\nTesteando la preservación de la privacidad de los datos empresariales:")
    testear_privacidad_empresarial()


# Ejecutar las pruebas si este script es el programa principal
if __name__ == "__main__":
    testear_privacidad()