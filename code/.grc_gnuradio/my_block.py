import gras
import numpy

class MyBlock(gras.Block):

	def __init__(self):
		gras.Block.__init__(self,
			name="my_block",
			in_sig=[numpy.float32, numpy.float32], # input and output are 32bit numpy float datatype
			out_sig=[numpy.float32])	
		

	def set_parameters(self, value):
		self.value = value
	
	# Here's where you define the function of block | This function runs for each input value
	def work(self, input_items, output_items):
		
		# output_items is a double array | first index corresponds to output port which starts from 0
		# since we have only one output, first index is 0
		# the item has to be an array even if it is a single integer
		output_items[0][:1] = input_items[0][:1] + self.value

		print "Output Value", output_items[0][:1]
		print "Hello World"
		
		# These lines report to GNU Radio how many items were consumed and produced
		self.consume(0, 1) # Consume one item from input port 0 
		self.produce(0, 1) # Produce one item from output port 0

