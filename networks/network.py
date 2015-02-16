class Network(object):
    """Network"""

    def __init__(self, parser=None):
        self.parser = parser
        self.input_layer = []
        self.hidden_layer = []
        self.output_layer = []

    def add_input_neuron(self, neuron):
        self.input_layer.append(neuron)

    def add_hidden_neuron(self,neuron):
        self.hidden_layer.append(neuron)

    def add_output_neuron(self, neuron):
        self.output_layer.append(neuron)

    def run(self):
        for data in self.parser.parse():
            for neuron in self.input_layer:
                neuron.receive(data["return"])
                neuron.activate()
            for neuron in self.hidden_layer:
                neuron.activate()
            for neuron in self.output_layer:
                neuron.activate()

    def connect(self):
        for hidden_neuron in self.hidden_layer:
            for output_neuron in self.output_layer:
                hidden_neuron.add_connection(output_neuron)
        for input_neuron in self.input_layer:
            for hidden_neuron in self.hidden_layer:
                input_neuron.add_connection(hidden_neuron)
