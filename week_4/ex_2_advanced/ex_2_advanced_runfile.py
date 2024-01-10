import Bio.Seq
from Bio import SeqIO, SeqUtils, Seq
import csv

'''Matias Medina Tanco - Ex_2_advanced'''

# Define the Sequence class
class Sequence:

    # Initialize the class
    def __init__(self, name, description, data):
        self.name = name
        self.description = description
        self.data = data

    # Define method for calculating sequence length
    def calculate_length(self):
        length = len(self.data)
        return length

    # Define method for calculating GC content
    def calculate_gc(self):
        gc = SeqUtils.gc_fraction(self.data)
        return gc

    # Define abstract method for transcription and translation (as well as for getting protein
    # molecular weight)
    def transcription_translation(self):
        pass

# Define DnaSequence subclass
class DnaSequence(Sequence):
    # Define method that transcribes DNA sequence to RNA sequence
    def transcription_translation(self):
        rna_seq = Bio.Seq.transcribe(self.data)
        return rna_seq

# Define RnaSequence subclass
class RnaSequence(Sequence):
    # Define method that translates nucleotide sequence into protein sequence
    def transcription_translation(self):
        prot_seq = Bio.Seq.translate(self.data)
        return prot_seq

# Define ProteinSequence subclass
class ProteinSequence(Sequence):
    # Define method that gets molecular weight from protein sequence
    def transcription_translation(self):
        to_weight = self.data
        # remove the '*' symbols from the protein sequence. '*' is used by Biopython to for stop codons,
        # but their presence in a sequence provokes an error in the molecular_weight method
        to_weight = to_weight.replace('*','')
        # Calculate molecular weight of protein
        prot_weight = Bio.SeqUtils.molecular_weight(to_weight, seq_type='protein')
        return prot_weight

# Define Fasta Parser class
class FastaParser:
    def __init__(self, file, output_file):
        self.file = file
        self.output_file = output_file

    # Define method that parses file and outputs into the console
    def adv_parse_file(self):
        print("adv_parse_file is running.")

        # Read file
        entries = list(SeqIO.parse(self.file, "fasta"))

        for sequence in entries:
            # Create instances of DnaSequence, RnaSequence, and ProteinSequence.
            # Use their methods to calculate all the required information
            dna = DnaSequence(sequence.id, sequence.description, sequence.seq)
            dna_length = dna.calculate_length()
            gc_content = dna.calculate_gc()
            rna_sequence = dna.transcription_translation()
            # RnaSequence here uses the RNA sequence obtained from DnaSequence for data
            rna = RnaSequence(sequence.id, sequence.description, rna_sequence)
            protein_sequence = rna.transcription_translation()
            # RnaSequence here uses the protein sequence obtained from RnaSequence for data
            protein = ProteinSequence(sequence.id, sequence.description, protein_sequence)
            protein_weight = protein.transcription_translation()

            # Print all the info on the console
            print("Name:", sequence.id)
            print("Description: ", sequence.description)
            print("DNA sequence: ", sequence.seq)
            print("DNA length (nt): ", dna_length)
            print("GC content (0.0 to 1.0): ", gc_content)
            print("RNA transcript: ", rna_sequence)
            print("Protein translation: ", protein_sequence)
            print("Protein molecular weight (Da): ", protein_weight)
            print("\n")

        print("adv_parse_file has finished running.")

    # Modification of adv_parse_file method that parses file and outputs into a CSV file
    def adv_parse_file_csv(self):
        # Read the FASTA file
        entries = list(SeqIO.parse(self.file, "fasta"))

        # Define lists with the rows that will go in the CSV file
        name_row = ["Name"]
        desc_row = ["Description"]
        dna_row = ["DNA length (nt)"]
        gc_row = ["GC content (0.0 to 1.0)"]
        rna_row = ["RNA transcript"]
        prot_row = ["Protein translation"]
        weight_row = ["Protein molecular weight (Da)"]

        # Use a for loop to iterate through the sequences in the file
        for sequence in entries:
            # Create instances of DnaSequence, RnaSequence, and ProteinSequence.
            # Use their methods to calculate all the required information
            dna = DnaSequence(sequence.id, sequence.description, sequence.seq)
            dna_length = dna.calculate_length()
            gc_content = dna.calculate_gc()
            rna_sequence = dna.transcription_translation()
            # RnaSequence here uses the RNA sequence obtained from DnaSequence for data
            rna = RnaSequence(sequence.id, sequence.description, rna_sequence)
            protein_sequence = rna.transcription_translation()
            # RnaSequence here uses the protein sequence obtained from RnaSequence for data
            protein = ProteinSequence(sequence.id, sequence.description, protein_sequence)
            protein_weight = protein.transcription_translation()

            # Append the data to each of the relevant rows
            name_row.append(sequence.id)
            desc_row.append(sequence.description)
            dna_row.append(sequence.seq)
            gc_row.append(gc_content)
            rna_row.append(rna_sequence)
            prot_row.append(protein_sequence)
            weight_row.append(protein_weight)

        # Make a list containing all the rows
        total_obj_rows = [name_row, desc_row, dna_row, gc_row, rna_row, prot_row, weight_row]

        # Write these rows into the output CSV file.
        csv_file = open(self.output_file, "w")
        writer = csv.writer(csv_file)
        for row in total_obj_rows:
            writer.writerow(row)
        csv_file.close()



# Parse the "sequences_advanced.fasta" file (Results from Ex_2_advanced)
parse3 = FastaParser("sequences_advanced.fasta", "ex_2_advanced_submission.csv")
parse3.adv_parse_file()
parse3.adv_parse_file_csv()