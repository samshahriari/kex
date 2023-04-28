# Import from Qiskit Aer noise module
from qiskit_aer.noise import (NoiseModel, QuantumError, ReadoutError,
                              pauli_error, depolarizing_error, thermal_relaxation_error)
from get_prop_backend import *

""" noise_model = NoiseModel()
p_error = get_pauli_x_median()
p_meas = 0.1

single_qubit_pauli_error = pauli_error([('X', p_error), ('I', 1 - p_error)])

noise_model.add_all_qubit_quantum_error(
    single_qubit_pauli_error, ['x', 'sx', 'rz'])
print(noise_model) """


def add_SPAM_error(nm: NoiseModel):
    p0given1, p1given0 = get_SPAM_error()
    error = ReadoutError([[1 - p1given0, p1given0], [p0given1, 1 - p0given1]])
    nm.add_all_qubit_readout_error(error)


def add_pauli_error(nm: NoiseModel) :
    p_error = get_pauli_x_median()
    single_qubit_pauli_error = pauli_error(
        [('X', p_error), ('I', 1 - p_error)])
    nm.add_all_qubit_quantum_error(
        single_qubit_pauli_error, ['x', 'sx', 'rz'])


def add_thermal_error(nm: NoiseModel):
    t1, t2, t = get_thermal_error()
    thermal_error = thermal_relaxation_error(t1, t2, t)
    nm.add_all_qubit_quantum_error(thermal_error, ['x', 'sx', 'rz'])
