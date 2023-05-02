
from quantum_walk import *

from qiskit import Aer
from qiskit_aer.noise import NoiseModel, device
from qiskit_aer import AerSimulator
from qiskit import QuantumCircuit, transpile
from qiskit_ibm_provider import IBMProvider
from qiskit.providers.models import BackendProperties
from qiskit_aer.noise import (NoiseModel, QuantumError, ReadoutError,
                              pauli_error, depolarizing_error, thermal_relaxation_error)

from statistics import median

# load account
IBMProvider.save_account(
    'f88621df23cb74fe37cb19989d9944695cf9fae4c4a138272bf02e949d9e8243dd20d3ba7b3428ac53f8bfd8036451d70201868e525af1e8f7d9e50d782bc6f5', overwrite=True)
provider = IBMProvider()

# get backend
backend = provider.get_backend('ibm_nairobi')
backend_properties: BackendProperties = backend.properties()


def get_pauli_x_median() -> float:
    l = []
    for i in range(7):
        l.append(backend_properties.gate_error('x', [i]))
    return median(l)


def get_SPAM_error() -> tuple[float, float]:
    m0p1 = []
    m1p0 = []
    for i in range(7):
        m0p1.append(backend_properties.qubit_property(i)[
            'prob_meas0_prep1'][0])
        m1p0.append(backend_properties.qubit_property(i)[
            'prob_meas1_prep0'][0])

    return median(m0p1), median(m1p0)


def get_thermal_error() -> tuple[float, float, float]:
    t1 = []
    t2 = []
    gate_time = []
    for i in range(7):
        t1.append(backend_properties.t1(i))
        t2.append(backend_properties.t2(i))

    coupling_map = [(0, 1), (1, 2), (1, 3), (3, 5), (4, 5), (5, 6)]
    for (x, y) in coupling_map:
        gate_time.append(backend_properties.gate_length('cx', [x, y]))
        gate_time.append(backend_properties.gate_length('cx', [y, x]))

    # TODO SKRIV VARFÖR
    return median(t1)/10, median(t2)/10, median(gate_time)/10
