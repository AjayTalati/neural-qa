import data_io
import sys
import cPickle as pickle
def load(filename):
	vocab = pickle.load(open(filename,'rb'))
	vocab_in  = { i:k for k,i in enumerate(vocab['input_vocab']) }
	vocab_out = { i:k for k,i in enumerate(vocab['output_vocab']) }
	return vocab_in,vocab_out

if __name__ == "__main__":
	filenames = sys.argv[1:-1]
	output_file = sys.argv[-1]
	input_vocab = set()
	output_vocab = set()
	for filename in filenames:
		for input_sentence,response_sentence in data_io.process_lines(filename):
			input_vocab.update(input_sentence[1])
			if response_sentence != None:
				output_vocab.add(response_sentence[0])

	pickle.dump({
		"input_vocab":  input_vocab,
		"output_vocab": output_vocab,
	},open(output_file,'wb'),2)
