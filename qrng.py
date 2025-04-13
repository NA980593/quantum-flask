from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
import numpy as np


def get_random():
    circuit = QuantumCircuit(5, 5)

    for i in range(5):
        circuit.h(i)

    for i in range(5):
        circuit.measure(i, i)

    simulator = Aer.get_backend('qasm_simulator')
    compiled_circuit = transpile(circuit, simulator)
    result = simulator.run(compiled_circuit, shots=102400).result()

    counts = result.get_counts()
    binary_string = list(counts.keys())[0]

    random_number = int(binary_string, 2)

    return random_number