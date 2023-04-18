# Plot two counts in the same figure with legends and colors specified.

from qiskit.visualization import plot_histogram

counts1 = {'00': 525, '11': 499}
counts2 = {'00': 511, '11': 514}

legend = ['First execution', 'Second execution']

plot_histogram([counts1, counts2], legend=legend, color=['crimson', 'midnightblue'],
               title="New Histogram")

# You can sort the bitstrings using different methods.

counts = {'001': 596, '011': 211, '010': 50, '000': 117, '101': 33, '111': 8,
          '100': 6, '110': 3}

# Sort by the counts in descending order
hist1 = plot_histogram(counts, sort='value_desc')

# Sort by the hamming distance (the number of bit flips to change from
# one bitstring to the other) from a target string.
hist2 = plot_histogram(counts, sort='hamming', target_string='001')
