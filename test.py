from qiskit import QuantumCircuit, Aer, assemble, execute
import numpy as np
import collections
from qiskit.visualization import plot_histogram, plot_bloch_multivector

qc = QuantumCircuit(3, 1)
# Apply H-gate to each qubit:
for qubit in range(3):
    qc.h(qubit)
# See the circuit:
qc.measure(2, 0)
print(qc.draw())

"""
backend = Aer.get_backend('aer_simulator')
results = backend.run(qc, shots=1000000).result()
hist = results.get_counts()
print([(key, round(float(val/1000000), 3))
      for key, val in collections.OrderedDict(sorted(hist.items())).items()])
"""
