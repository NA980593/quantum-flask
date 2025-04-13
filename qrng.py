from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
import numpy as np


def get_random():
    # Create a quantum circuit with 5 qubits and 5 classical bits
    circuit = QuantumCircuit(5, 5)

    # Apply a Hadamard gate to qubits
    for i in range(5):
        circuit.h(i)

    # Measure qubits
    for i in range(5):
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

    return random_number
