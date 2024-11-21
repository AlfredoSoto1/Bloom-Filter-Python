import mmh3
from bitarray import bitarray
import csv
import math
import sys

class BloomFilter:
    def __init__(self, size, num_hashes):
        self.size = size
        self.num_hashes = num_hashes
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)

    def add(self, item):
        for i in range(self.num_hashes):
            index = mmh3.hash(item, i) % self.size
            self.bit_array[index] = 1

    def check(self, item):
        for i in range(self.num_hashes):
            index = mmh3.hash(item, i) % self.size
            if not self.bit_array[index]:
                return False
        return True

def calculate_parameters(n, p):
    """Calculate size (m) and number of hashes (k) for the Bloom Filter."""
    m = - (n * math.log(p)) / (math.log(2) ** 2)
    k = (m / n) * math.log(2)
    return int(math.ceil(m)), int(math.ceil(k))

def read_csv(file_path):
    """Read emails from a CSV file."""
    with open(file_path, 'r') as file:
        return [row[0] for row in csv.reader(file)]

def main(db_input_file, db_check_file):
    # Parameters
    false_positive_prob = 0.0000001
    emails = read_csv(db_input_file)
    n = len(emails)  # Number of items to store

    # Calculate Bloom Filter parameters
    m, k = calculate_parameters(n, false_positive_prob)

    # Initialize Bloom Filter
    bloom_filter = BloomFilter(m, k)

    # Add emails to the Bloom Filter
    for email in emails:
        bloom_filter.add(email)

    # Check emails from the second file
    check_emails = read_csv(db_check_file)
    for email in check_emails:
        result = "Probably in the DB" if bloom_filter.check(email) else "Not in the DB"
        print(f"{email},{result}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python <your_program> db_input.csv db_check.csv")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])
