import sys
import csv
import math
import array

class BloomFilter:

  def __init__(self, element_count):
    # Calculate the bloom parameters
    self.bt_size, self.num_hashes = self.calculateBloomParameters(element_count, 0.0000001)
    
    # Allocate the necessary bits
    self.bit_array = self.makeBitArray(self.bt_size, fill=0)

  def makeBitArray(self, bitSize, fill = 0):
    intSize = bitSize >> 5      # number of 32 bit integers
    if (bitSize & 31):          # if bitSize != (32 * n) add
        intSize += 1            #    a record for stragglers
    if fill == 1:    
        fill = 4294967295       # all bits set == 2^32
    else:    
        fill = 0                # all bits cleared

    bitArray = array.array('I') # 'I' = unsigned 32-bit integer
    bitArray.extend((fill,) * intSize)
    return(bitArray)

  # testBit() returns a nonzero result, 2**offset, if the bit at 'bit_num' is set to 1.
  def testBit(self, bit_num):
    record = bit_num >> 5
    offset = bit_num & 31
    mask = 1 << offset
    return(self.bit_array[record] & mask)

  # setBit() returns an integer with the bit at 'bit_num' set to 1.
  def setBit(self, bit_num):
    record = bit_num >> 5
    offset = bit_num & 31
    mask = 1 << offset
    self.bit_array[record] |= mask
    return(self.bit_array[record])

  # clearBit() returns an integer with the bit at 'bit_num' cleared.
  def clearBit(self, bit_num):
    record = bit_num >> 5
    offset = bit_num & 31
    mask = ~(1 << offset)
    self.bit_array[record] &= mask
    return(self.bit_array[record])

  # toggleBit() returns an integer with the bit at 'bit_num' inverted, 0 -> 1 and 1 -> 0.
  def toggleBit(self, bit_num):
    record = bit_num >> 5
    offset = bit_num & 31
    mask = 1 << offset
    self.bit_array[record] ^= mask
    return(self.bit_array[record])

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
      self.setBit(index)

  # Check if the value is probably in filter
  def check(self, value):
    hashes = [self.hash(i * i, value) % self.bt_size for i in range(0, self.num_hashes)]

    for index in hashes:
      if self.testBit(index) == 0:
        return False # Is definitely NOT in database
    
    return True # Probably in database
  
def readCSV(file_path):
  with open(file_path, 'r') as file:
      return [row[0] for row in csv.reader(file)][1:]
  
def main(input_1, input_2):
  database = readCSV(input_1)
  database_request = readCSV(input_2)

  # Create the filter for testing
  filter = BloomFilter(len(database))

  # Add data to database set
  for element in database:
    filter.cache(element)

  for element in database_request:
    if filter.check(element):
      print(f'{element},Probably in the DB')
    else:
      print(f'{element},Not in the DB')

if len(sys.argv) > 1:
   main(sys.argv[1], sys.argv[2])