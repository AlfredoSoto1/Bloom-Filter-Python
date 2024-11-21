import sys
import csv
import math

class BloomFilter:

  def __init__(self, element_count):
    # Calculate the bloom parameters
    self.bt_size, self.num_hashes = self.calculateBloomParameters(element_count, 0.0000001)
    
    # Allocate the necessary bits
    self.cache_filter = [0] * self.bt_size

  # Parameters:
  # n == count of elements from hash set
  # p == desired probability
  # 
  # Returns:
  # m == Bloom table size
  # k == Number of hashes to be done
  def calculateBloomParameters(self, n, p):
      m = math.ceil((n * math.log(p)) / math.log(1 / math.pow(2, math.log(2))))
      k = round((m / n) * math.log(2))
      return m, k
  
  # Customize the hash function to work with a given seed
  def hash(self, seed, value):
    return hash(value) * seed + seed
  
  # Cache the value in filter
  def cache(self, value):
    hashes = [self.hash(i * i, value) % self.bt_size for i in range(0, self.num_hashes)]
    
    for index in hashes:
      self.cache_filter[index] = 1 # set as active

  # Check if the value is probably in filter
  def check(self, value):
    hashes = [self.hash(i * i, value) % self.bt_size for i in range(0, self.num_hashes)]

    for index in hashes:
      if self.cache_filter[index] == 0:
        return False # Is definitely NOT in database
    
    return True # Probably in database
  
class HashTableSet:

  # Create the Set with N ammount of elements
  # Start with an empty set of already allocated spaces
  def __init__(self, element_count):
    # Create a filter
    self.filter = BloomFilter(element_count)
    # Set hashtable-set
    self.data = [None] * element_count

  # Adds a value to the set
  def add(self, value):
    # Obtain the index of the element in hash table
    index = self.filter.hash(1, value) % len(self.data)

    # If element exists, dont add it
    if self.filter.check(value):
      return 

    # If element doesnt exist, insert it
    self.data[index] = value
    self.filter.cache(value)

  # Returns the corresponding value from table
  def tableCheck(self, value):
    if not self.filter.check(value):
      return False # Not in hash table
    return True
  
def readCSV(file_path):
  with open(file_path, 'r') as file:
      return [row[0] for row in csv.reader(file)][1:]
  
def main(input_1, input_2):
  database = readCSV(input_1)
  database_request = readCSV(input_2)

  # Create a new database with a preset size
  database_set = HashTableSet(len(database))

  # Add data to database set
  for element in database:
    database_set.add(element)

  for element in database_request:
    if database_set.tableCheck(element):
      print(f'{element},Probably in the DB')
    else:
      print(f'{element},Not in the DB')

if len(sys.argv) > 1:
   main(sys.argv[1], sys.argv[2])
