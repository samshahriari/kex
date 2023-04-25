from quantum_walk import *

from qiskit import IBMQ, Aer
from qiskit_aer.noise import NoiseModel
from qiskit_aer import AerSimulator
from qiskit import QuantumCircuit, transpile
from errors import *


def main():

    # Pauli X noise model
    noise_model = NoiseModel()

    noise_model = add_pauli_error(noise_model)
    noise_model = add_SPAM_error(noise_model)
    # noise_model = add_thermal_error(noise_model)

    qc = create_quantum_walk_with_num_steps(1, "1111")
    # print(qc.draw())
    backend = Aer.get_backend('aer_simulator')
    sim_noise = AerSimulator(noise_model=noise_model)
    circ_tnoise = transpile(qc, sim_noise)
    # print(circ_tnoise)
    result_bit_flip = sim_noise.run(circ_tnoise, shots=1000000).result()
    counts_bit_flip = result_bit_flip.get_counts(0)

    # Plot noisy output
    print(counts_bit_flip)
    plot_histogram(counts_bit_flip).show()

    # results = backend.run(qc, shots=10000).result()
    # hist = results.get_counts()
    print([(key, round(float(val/1000000), 6))
           for key, val in collections.OrderedDict(sorted(counts_bit_flip.items())).items()])
    input()


if __name__ == '__main__':
    main()
