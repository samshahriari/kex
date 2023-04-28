import pandas as pd
from qiskit_aer.noise import NoiseModel
from qiskit_aer import AerSimulator
from qiskit import transpile

from quantum_walk import *
from errors import *
from get_prop_backend import *


def main():

    error_values = {'Pauli-X': [get_pauli_x_median()], 'Prob meas0 prep1': [get_SPAM_error()[0]], 'Prob meas1 prep0': [get_SPAM_error()[
        1]], 'T1 (us)': [round(get_thermal_error()[0]*10e6, 2)], 'T2 (us)': [round(get_thermal_error()[1]*10e6, 2)], 'gate time (ns)': [round(get_thermal_error()[2]*10e9, 2)]}

    print(error_values)

    error_val_df = pd.DataFrame.from_dict(error_values)
    error_val_df.to_csv('error_val_result_csv.csv', index=False)
    error_val_df.to_json('error_val_results_json.json')
    error_val_df.to_latex(buf='error_val_results_latex.tex', index=False)

    error_types = ["P", "S", "T", "PS", "PT", "ST", "PST"]

    output_dict = {'Noise type': [], 'Start Pos': [], '0000': [], '0001': [], '0010': [], '0011': [], '0100': [], '0101': [
    ], '0110': [], '0111': [], '1000': [], '1001': [], '1010': [], '1011': [], '1100': [], '1101': [], '1110': [], '1111': []}

    for start_pos in ["0000", "1111"]:

        for error_type in error_types:

            # Pauli X noise model
            noise_model = NoiseModel()

            # print(error_type)
            if 'P' in error_type:
                add_pauli_error(noise_model)
            if 'S' in error_type:
                add_SPAM_error(noise_model)
            if 'T' in error_type:
                add_thermal_error(noise_model)

            qc = create_quantum_walk_with_num_steps(1, start_pos)
            # print(qc.draw())
            sim_noise = AerSimulator(noise_model=noise_model)
            circ_tnoise = transpile(qc, sim_noise)
            # print(circ_tnoise)
            result_bit_flip = sim_noise.run(
                circ_tnoise, shots=1000000).result()
            counts_bit_flip = result_bit_flip.get_counts(0)

            for key in output_dict.keys():
                if key == 'Noise type' or key == 'Start Pos':
                    continue
                elif counts_bit_flip.__contains__(key):
                    output_dict[key].append(counts_bit_flip[key])
                else:
                    output_dict[key].append(0)
            output_dict['Start Pos'].append(start_pos)
            output_dict['Noise type'].append(error_type)
            # Plot noisy output
            # print(counts_bit_flip)
            # plot_histogram(counts_bit_flip).show()

            # results = backend.run(qc, shots=10000).result()
            # hist = results.get_counts()
            """  print(f'start: {start_pos}, type: {error_type}')
            print([(key, round(float(val/1000), 6))
                   for key, val in collections.OrderedDict(sorted(counts_bit_flip.items())).items()]) """
    # TODO printa parametrarna till noisemodellen

    # print(output_dict)
    df = pd.DataFrame.from_dict(output_dict)
    print(df)
    # df.to_csv('result_csv.csv', index=False)
    # df.to_json('results_json.json')
    # df.to_latex(buf='results_latex.tex', index=False)

    df['0001'] = df['0001'].to_numpy() / 1000000
    df['error'] = np.power(df['0001'].to_numpy() - ideal, 2)
    print(df)


if __name__ == '__main__':
    main()
