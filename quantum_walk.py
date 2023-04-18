from qiskit import QuantumCircuit, Aer, assemble, execute
import numpy as np
import collections
from qiskit.visualization import plot_histogram, plot_bloch_multivector


def add_coin_flip_to_qc(qc: QuantumCircuit) -> None:
    qc.h(4)
    qc.h(5)


def add_shift_operator_to_qc(qc: QuantumCircuit) -> None:
    qc.x(4)
    qc.x(5)
    qc.ccx(4, 5, 0)
    qc.x(4)
    qc.ccx(4, 5, 1)
    qc.x(4)
    qc.x(5)
    qc.ccx(4, 5, 2)
    qc.x(4)
    qc.ccx(4, 5, 3)


def create_quantum_walk_with_num_steps(num_steps: int, start_pos: str) -> QuantumCircuit:
    qc = QuantumCircuit(6, 4)

    set_starting_position(qc, start_pos)

    add_time_steps(qc, num_steps)
    add_measure_gates_to_qc(qc)

    return qc


def add_time_steps(qc: QuantumCircuit, num_steps: int) -> None:
    for _ in range(num_steps):
        add_coin_flip_to_qc(qc)
        add_shift_operator_to_qc(qc)


def add_measure_gates_to_qc(qc: QuantumCircuit) -> None:
    qc.barrier()
    qc.measure([0, 1, 2, 3], [0, 1, 2, 3])


def set_starting_position(qc: QuantumCircuit, s: str) -> None:
    if len(s) != 4:
        print("wrong starting position string, using 0000")
        return
    for bit, op in enumerate(reversed(s)):
        if op == '1':
            qc.x(bit)
        if op == 'h':
            qc.h(bit)
