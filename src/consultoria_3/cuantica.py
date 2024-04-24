#CONSULTA 1

#ALGORITMO DE Shor

from qiskit import QuantumCircuit, Aer, transpile
from qiskit.visualization import plot_histogram
from qiskit.algorithms import Shor

def shor_algorithm(n):
    # Crear un circuito cuántico
    qc = QuantumCircuit(2*n, n)

    # Implementar el algoritmo de Shor en el circuito
    shor = Shor(n, 2)
    shor.construct_circuit()
    qc.append(shor, range(shor.num_qubits))

    # Simular el circuito cuántico
    simulator = Aer.get_backend('aer_simulator')
    transpiled_qc = transpile(qc, simulator)
    result = simulator.run(transpiled_qc).result()

    # Obtener la distribución de probabilidad resultante
    counts = result.get_counts(qc)

    # Interpretar los resultados para obtener los factores
    factors = []
    for key in counts:
        x = int(key, 2)
        factor = shor.factor(x)
        factors.append(factor)

    return factors

# Factorizar el número 15 como ejemplo
factores_15 = shor_algorithm(15)
print("Los factores de 15 son:", factores_15)

# Factorizar un número grande, por ejemplo 21
factores_21 = shor_algorithm(21)
print("Los factores de 21 son:", factores_21)


# ALGORITMO DE GROVER

from qiskit import QuantumCircuit, Aer, transpile
from qiskit.visualization import plot_histogram
from qiskit.algorithms import Grover

def grover_algorithm(database):
    # Crear un circuito cuántico
    num_qubits = 3  # Ajustar el número de qubits según la base de datos
    qc = QuantumCircuit(num_qubits)

    # Implementar el algoritmo de Grover en el circuito
    grover = Grover()
    grover.construct_circuit()
    qc.append(grover, range(grover.num_qubits))

    # Simular el circuito cuántico
    simulator = Aer.get_backend('aer_simulator')
    transpiled_qc = transpile(qc, simulator)
    result = simulator.run(transpiled_qc).result()

    # Obtener la distribución de probabilidad resultante
    counts = result.get_counts(qc)

    # Interpretar los resultados para buscar en la base de datos
    resultados = {}
    for key in counts:
        index = int(key, 2)
        resultados[index] = database[index]

    return resultados

# Base de datos de ejemplo para buscar
database_ejemplo = {0: 'No', 1: 'Yes', 2: 'No', 3: 'No', 4: 'Yes', 5: 'No', 6: 'Yes', 7: 'No'}
resultados_busqueda = grover_algorithm(database_ejemplo)
print("Resultados de la búsqueda:", resultados_busqueda)


# ALGORITMO DE SIMON

from qiskit import QuantumCircuit, Aer, transpile
from qiskit.visualization import plot_histogram
from qiskit.algorithms import Simon

def simon_algorithm(funcion):
    # Crear un circuito cuántico
    num_qubits = 4  # Ajustar el número de qubits según la función
    qc = QuantumCircuit(num_qubits, num_qubits)

    # Implementar el algoritmo de Simon en el circuito
    simon = Simon(funcion)
    simon.construct_circuit()
    qc.append(simon, range(simon.num_qubits))

    # Simular el circuito cuántico
    simulator = Aer.get_backend('aer_simulator')
    transpiled_qc = transpile(qc, simulator)
    result = simulator.run(transpiled_qc).result()

    # Obtener la distribución de probabilidad resultante
    counts = result.get_counts(qc)

    return counts

# Función periódica de ejemplo
def funcion_ejemplo(x):
    return x % 2

resultados_simon = simon_algorithm(funcion_ejemplo)
print("Resultados de Simon para la función periódica:", resultados_simon)



##CONSULTA 2

#SIMULADO


from qiskit import QuantumCircuit, Aer, execute
import numpy as np

# Generación de números aleatorios cuánticos (QRNG)
def qrng():
    # Creamos un circuito cuántico con un solo qubit
    qrng_circuit = QuantumCircuit(1, 1)
    
    # Aplicamos una compuerta Hadamard para poner el qubit en superposición
    qrng_circuit.h(0)
    
    # Medimos el qubit para obtener un resultado aleatorio
    qrng_circuit.measure(0, 0)
    
    # Simulamos la ejecución del circuito
    simulator = Aer.get_backend('qasm_simulator')
    job = execute(qrng_circuit, simulator, shots=1)
    result = job.result()
    counts = result.get_counts(qrng_circuit)
    
    # Retornamos el resultado aleatorio obtenido
    return int(list(counts.keys())[0])

# Corrección de errores cuánticos (QEC) básica
def qec(input_qubit):
    # Creamos un circuito cuántico con un solo qubit
    qec_circuit = QuantumCircuit(1, 1)
    
    # Codificamos el qubit utilizando una compuerta de Pauli X (bit-flip) en función del número aleatorio generado
    if input_qubit == 1:
        qec_circuit.x(0)
    
    # Aplicamos una compuerta Hadamard para introducir una superposición
    qec_circuit.h(0)
    
    # Simulamos el ruido añadiendo una rotación de Pauli Y (fase-flip) con cierta probabilidad
    noise = np.random.choice([0, 1], p=[0.9, 0.1])  # Probabilidad de 10% de error
    if noise == 1:
        qec_circuit.y(0)
    
    # Aplicamos nuevamente la compuerta Hadamard
    qec_circuit.h(0)
    
    # Medimos el qubit para obtener el resultado corregido
    qec_circuit.measure(0, 0)
    
    # Simulamos la ejecución del circuito
    simulator = Aer.get_backend('qasm_simulator')
    job = execute(qec_circuit, simulator, shots=1)
    result = job.result()
    counts = result.get_counts(qec_circuit)
    
    # Retornamos el resultado corregido
    return int(list(counts.keys())[0])

# Realizamos la prueba de QRNG
print("Número aleatorio cuántico generado:", qrng())

# Realizamos la prueba de QEC con un qubit aleatorio y simulación de error
random_qubit = np.random.choice([0, 1])
print("Qubit original:", random_qubit)
corrected_qubit = qec(random_qubit)
print("Qubit corregido:", corrected_qubit)



##################################


from qiskit import QuantumCircuit, transpile, assemble, Aer, IBMQ
from qiskit.providers.ibmq import least_busy

# Generación de números aleatorios cuánticos (QRNG) en un dispositivo cuántico real
def qrng_real_device():
    # Cargamos la cuenta de IBM Quantum Experience
    provider = IBMQ.load_account()
    
    # Obtenemos el proveedor de servicios cuánticos y seleccionamos el dispositivo menos ocupado
    provider = IBMQ.get_provider(hub='ibm-q')
    backend = least_busy(provider.backends(simulator=False))
    
    # Creamos un circuito cuántico con un solo qubit
    qrng_circuit = QuantumCircuit(1, 1)
    
    # Aplicamos una compuerta Hadamard para poner el qubit en superposición
    qrng_circuit.h(0)
    
    # Medimos el qubit para obtener un resultado aleatorio
    qrng_circuit.measure(0, 0)
    
    # Compilamos el circuito para el dispositivo seleccionado
    transpiled_circuit = transpile(qrng_circuit, backend)
    
    # Ensamblamos el circuito en un objeto Qobj para la ejecución en el dispositivo
    qobj = assemble(transpiled_circuit, backend=backend)
    
    # Ejecutamos el circuito en el dispositivo cuántico
    job = backend.run(qobj)
    result = job.result()
    
    # Retornamos el resultado aleatorio obtenido
    counts = result.get_counts(qrng_circuit)
    return int(list(counts.keys())[0])

# Ejecutamos la generación de números aleatorios cuánticos en un dispositivo real
print("Número aleatorio cuántico generado en un dispositivo real:", qrng_real_device())


