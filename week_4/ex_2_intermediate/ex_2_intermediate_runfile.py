from Bio import SeqIO, SeqUtils, Seq
import csv

'''Matias Medina Tanco - Ex_2_intermediate'''

# Define the Sequence class
class Sequence:

    # Initialize the class
    def __init__(self, name, data, type="Default", gcContent=0, start_codon_presence="Default"):
    #def __init__(self, name, data):
        self.name = name
        self.data = data
        self.type = type
        self.gcContent = gcContent
        self.start_codon_presence = start_codon_presence


# Define the DnaSequence subclass
class DnaSequence(Sequence):
    # Method to calculate and return the sequence's GC content
    def gc_content(self):
        # Define variables for the sequence's type (DNA), GC content, and the presence of a start codon (No)
        self.type = "DNA"
        self.gcContent = 0
        self.start_codon_presence = "No"

        # Calculate GC content
        self.gcContent = SeqUtils.gc_fraction(self.data)

        # Return the gcContent
        return self.gcContent

# Define the RnaSequence subclass
class RnaSequence(Sequence):

    # Method to check whether the sequence is RNA or DNA, and if it is RNA check that it has the start
    # codon ("AUG")
    def has_start_codon(self):
        # Define variables for the sequence's type (RNA), GC content (NA), and the presence of a start codon.
        self.type = "RNA"
        self.gcContent = "NA"
        self.start_codon_presence = "No"
        # Define variable that will store the result of the analysis on whether it is DNA or RNA
        analysis = "RNA"

        # Use Biopython's find method to determine if the Sequence is RNA or DNA (due to presence of U).
        check_U = self.data.find("U")
        if check_U > 0:
            analysis = "RNA"
        else:
            analysis ="DNA"
            return analysis

        # Find whether or not the sequence has a start codon (AUG). Biopython's find method returns
        # -1 if it found nothing
        startCodon = self.data.find("AUG")

        # If the find method returned something different to -1, then change start_codon_presence
        # from "No" to "Yes"
        if startCodon != -1:
            self.start_codon_presence = "Yes"

        # Return the result of the analysis on the sequence's type
        return analysis

# FastaParser class from ex_2_beginner. Added a modified parse_file_seq_obj method for Ex_2_intermediate.
class FastaParser:
    # Initialize the class
    def __init__(self, file, output_file):
        self.file = file
        self.output_file = output_file

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

        # Write all the rows into the output file
        csv_file = open(self.output_file, "w")
        writer = csv.writer(csv_file)
        for row in total_rows:
            writer.writerow(row)
        csv_file.close()

        # Print indicator that method has finished running
        print("CSV output file has been generated.")
        print("The parse_file_csv method has finished running.")

    # Define the parse_file_seq_obj method that will sort the sequences into either
    # DnaSequence or RnaSequence objects and put them in a list
    def parse_file_seq_obj(self):

        # Print indicator that method has started running
        print("The parse_file_seq_obj method is running...")

        # Define empty list that will hold the Sequence objects
        sequence_list = []

        # Read the FASTA file
        entries = list(SeqIO.parse(self.file, "fasta"))

        for sequence in entries:
            # Define a ProcessingSequence object of RnaSequence class with the sequence name and the
            # nucleotide sequence itself
            ProcessingSequence = RnaSequence(sequence.id, sequence.seq)
            # Run the has_start_codon method of RnaSequence, which will determine if the sequence
            # type is DNA or RNA depending on the presence of the start codon
            type_result = ProcessingSequence.has_start_codon()

            # If the sequence type is DNA, then change the ProcessingSequence object to be an
            # object of the DnaSequence class
            if type_result == "DNA":
                ProcessingSequence = DnaSequence(sequence.id, sequence.seq)
                ProcessingSequence.gc_content()

            # Append the RnaSequence or DnaSequence object to the list of objects
            sequence_list.append(ProcessingSequence)

        # Define the rows that will go in the CSV file
        name_obj_row = ["Obj Name"]
        type_obj_row = ["Obj Type"]
        gc_obj_row = ["Obj GC Content"]
        codon_obj_row = ["Obj Start Codon Presence"]

        # Use a for loop to iterate through the sequences in the file
        for object in sequence_list:
            # Obtain the object name, type and GC content and append them to their respective lists
            name_obj_row.append(object.name)
            type_obj_row.append(object.type)
            gc_obj_row.append(object.gcContent)
            codon_obj_row.append(object.start_codon_presence)

        # Make a list with all the rows that will be written to the CSV file
        total_obj_rows = [name_obj_row, type_obj_row, gc_obj_row, codon_obj_row]

        # Append these rows into the output file.
        csv_file = open(self.output_file, "a")
        writer = csv.writer(csv_file)
        for row in total_obj_rows:
            writer.writerow(row)
        csv_file.close()

        # Print indicator that method has finished running
        print("CSV output file has been generated.")
        print("The parse_file_seq_obj method has finished running.")


# Parse the "sequences_beginner.fasta" file (Results from Ex_2_beginner)
parse1 = FastaParser("sequences_beginner.fasta", "ex_2_intermediate_submit.csv")
# parse1.parse_file()
parse1.parse_file_csv()

# Parse the "sequences_intermediate.fasta" file (Results from Ex_2_intermediate)
parse2 = FastaParser("sequences_intermediate.fasta", "ex_2_intermediate_submit.csv")
parse2.parse_file_seq_obj()

