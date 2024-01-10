from Bio import SeqIO, SeqUtils
import csv

'''Matias Medina Tanco - Ex_2_beginner'''

# Define the FastaParser class
class FastaParser:
    # Initialize the class
    def __init__(self, file):
        self.file = file

    # Define the parse_file method
    def parse_file(self):

        # Print indicator that method has started running
        print("The parse_file method is running...")

        # Read the FASTA file
        entries = list(SeqIO.parse(self.file, "fasta"))

        # Use a for loop to iterate through the sequences in the file
        for sequence in entries:
            # Obtain the sequence name, description, length, GC content and molecular weight with the
            # functions in biopython. Print them out on the console.
            print("Name:", sequence.id)
            print("Description:", sequence.description)
            print("Length (nt):", len(sequence.seq))
            print("GC content (0.0 to 1.0): ", SeqUtils.gc_fraction(sequence.seq))
            print("Molecular weight (Da): ", SeqUtils.molecular_weight(sequence.seq))

            #Print new line to have space between the different sequences
            print("\n")

        # Print indicator that method has finished running
        print("The parse_file method has finished running.")

    # Define an alternative parse_file_csv method that does the same things than parse_file, but writes
    # output in  to a CSV file named "ex_2_beginner_submit.csv"
    def parse_file_csv(self):

        # Print indicator that method has started running
        print("The parse_file_csv method is running...")

        # Read the FASTA file
        entries = list(SeqIO.parse(self.file, "fasta"))

        # Define the rows that will go in the CSV file
        name_row = ["Name"]
        description_row = ["Description"]
        length_row = ["Length (nt)"]
        gc_row = ["GC content (0.0 to 1.0)"]
        weight_row = ["Molecular weight (Da)"]

        # Use a for loop to iterate through the sequences in the file
        for sequence in entries:
            # Obtain the sequence name, description, length, GC content and molecular weight with the
            # functions in biopython. Append them to their respective row lists.
            name_row.append(sequence.id)
            description_row.append(sequence.description)
            length_row.append(len(sequence.seq))
            gc_row.append(SeqUtils.gc_fraction(sequence.seq))
            weight_row.append(SeqUtils.molecular_weight(sequence.seq))

        # Make a list with all the rows that will be written to the CSV file
        total_rows = [name_row, description_row, length_row, gc_row, weight_row]

        # Write all the rows into the "ex_2_beginner_submit.csv" file
        csv_file = open("ex_2_beginner_submit.csv", "w")
        writer = csv.writer(csv_file)
        for row in total_rows:
            writer.writerow(row)
        csv_file.close()

        # Print indicator that method has finished running
        print("CSV output file has been generated.")
        print("The parse_file_csv method has finished running.")


# Parse the "sequences_beginner.fasta" file
parse1 = FastaParser("sequences_beginner.fasta")
parse1.parse_file()
parse1.parse_file_csv()
