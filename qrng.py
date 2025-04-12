from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
import numpy as np


def get_random():
    # Create a quantum circuit with 6 qubits and 6 classical bits
    circuit = QuantumCircuit(6, 6)

    # Apply a Hadamard gate to qubits
    for i in range(6):
        circuit.h(i)

    # Measure qubits
    for i in range(6):
        circuit.measure(i, i)

    # Aer simulator
    simulator = Aer.get_backend('qasm_simulator')

    compiled_circuit = transpile(circuit, simulator)

    # Run the circuit
    result = simulator.run(compiled_circuit, shots=102400).result()

    # Get the counts
    counts = result.get_counts()

    # Get the binary string
    binary_string = list(counts.keys())[0]

    # Convert the binary string to an integer
    random_number = int(binary_string, 2)

    # Scale the random number to the range 1-50
    random_number = (random_number % 50) + 1

    return random_number

    #this is bad because it is not uniformly random i dont think...