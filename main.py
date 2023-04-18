from quantum_walk import *

from qiskit import IBMQ, Aer
from qiskit_aer.noise import NoiseModel
from qiskit_aer import AerSimulator
from qiskit import QuantumCircuit, transpile


def main():
    IBMQ.save_account(
        'f88621df23cb74fe37cb19989d9944695cf9fae4c4a138272bf02e949d9e8243dd20d3ba7b3428ac53f8bfd8036451d70201868e525af1e8f7d9e50d782bc6f5', overwrite=True)
    provider = IBMQ.load_account()
    backend = provider.get_backend('ibm_perth')
    noise_model = NoiseModel.from_backend(backend)

    #  print(noise_model.to_dict())
    qc = create_quantum_walk_with_num_steps(1, "0000")
    print(qc.draw())
    backend = Aer.get_backend('aer_simulator')
    sim_noise = AerSimulator(noise_model=noise_model)
    circ_tnoise = transpile(qc, sim_noise)
    result_bit_flip = sim_noise.run(circ_tnoise).result()
    counts_bit_flip = result_bit_flip.get_counts(0)

    # Plot noisy output
    plot_histogram(counts_bit_flip).show()
    input()
    """ results = backend.run(qc, shots=10000).result()
    hist = results.get_counts()
    print([(key, round(float(val/10000), 3))
           for key, val in collections.OrderedDict(sorted(hist.items())).items()]) """


if __name__ == '__main__':
    main()
