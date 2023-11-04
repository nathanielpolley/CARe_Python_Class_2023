from Bio import SeqIO
import csv


class Sequence:
    def __init__(self, name, description, data):
        self.name = name
        self.description = description
        self.data = data

    def calculate_length(self):
        return len(self.data)

    def calculate_gc_content(self):
        gc_count = self.data.count('G') + self.data.count('C')
        return (gc_count / len(self.data)) * 100

    def transcription(self):
        pass

    def translation(self):
        pass


class DNASequence(Sequence):
    def transcription(self):
        return self.data.replace('T', 'U')


class RNASequence(Sequence):
    def translation(self):
        codon_table = {
            'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
            'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
            'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
            'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
            'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
            'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
            'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
            'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
            'UAU': 'Y', 'UAC': 'Y', 'UAA': '*', 'UAG': '*',
            'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
            'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
            'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
            'UGU': 'C', 'UGC': 'C', 'UGA': '*', 'UGG': 'W',
            'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
            'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
            'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G',
        }
        protein = ""
        start = self.data.find("AUG")
        if start != -1:
            while start + 3 <= len(self.data):
                codon = self.data[start:start + 3]
                amino_acid = codon_table.get(codon, '')
                if amino_acid == '*':
                    break
                protein += amino_acid
                start += 3
        return protein


class ProteinSequence(Sequence):
    def calculate_molecular_weight(self):
        amino_acid_weights = {
            'A': 71.03711, 'R': 156.10111, 'N': 114.04293, 'D': 115.02694,
            'C': 103.00919, 'Q': 128.05858, 'E': 129.04259, 'G': 57.02146,
            'H': 137.05891, 'I': 113.08406, 'L': 113.08406, 'K': 128.09496,
            'M': 131.04049, 'F': 147.06841, 'P': 97.05276, 'S': 87.03203,
            'T': 101.04768, 'W': 186.07931, 'Y': 163.06333, 'V': 99.06841,
        }
        weight = sum(amino_acid_weights.get(aa, 0) for aa in self.data)
        return round(weight, 2)


class FastaParser:
    def __init__(self, fasta_file):
        self.fasta_file = fasta_file
        self.sequences = []

    def parse(self):
        for record in SeqIO.parse(self.fasta_file, "fasta"):
            if 'T' in record.seq:
                seq = DNASequence(record.id, record.description, str(record.seq))
            elif 'U' in record.seq:
                seq = RNASequence(record.id, record.description, str(record.seq))
            else:
                seq = ProteinSequence(record.id, record.description, str(record.seq))
            self.sequences.append(seq)

    def process_sequences(self):
        with open("ex_2_advanced_submission.csv", "w", newline='') as csvfile:
            fieldnames = ['Sequence Name', 'Sequence Description', 'DNA Sequence', 'Sequence Length', 'GC Content',
                          'RNA Transcript', 'Protein Translation', 'Molecular Weight']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for seq in self.sequences:
                seq_length = seq.calculate_length()
                gc_content = seq.calculate_gc_content()
                if isinstance(seq, DNASequence):
                    rna_seq = seq.transcription()
                    protein_seq = "N/A"
                    molecular_weight = "N/A"
                elif isinstance(seq, RNASequence):
                    rna_seq = "N/A"
                    protein_seq = seq.translation()
                    molecular_weight = "N/A"
                else:
                    rna_seq = "N/A"
                    protein_seq = "N/A"
                    molecular_weight = seq.calculate_molecular_weight()
                writer.writerow({
                    'Sequence Name': seq.name,
                    'Sequence Description': seq.description,
                    'DNA Sequence': seq.data,
                    'Sequence Length': seq_length,
                    'GC Content': gc_content,
                    'RNA Transcript': rna_seq,
                    'Protein Translation': protein_seq,
                    'Molecular Weight': molecular_weight
                })


if __name__ == "__main__":
    fasta_parser = FastaParser("sequences_advanced.fasta")  # Replace with the path to your FASTA file
    fasta_parser.parse()
    fasta_parser.process_sequences()
#done