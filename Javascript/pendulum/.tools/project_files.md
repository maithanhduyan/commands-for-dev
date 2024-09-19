Ta có dự án như sau: 

# ../ai.js

```
/**
 * A node, representing a biological neuron.
 * @param {Number} ID  The ID of the node.
 * @param {Number} val The value of the node.
 */
function Node(ID, val) {
    this.id = ID;
    this.incomingConnections = [];
    this.outgoingConnections = [];
    if (val === undefined) {
        val = 0;
    }
    this.value = val;
    this.bias = 0;
}

/**
* A connection, representing a biological synapse.
* @param {String} inID   The ID of the incoming node.
* @param {String} outID  The ID of the outgoing node.
* @param {Number} weight The weight of the connection.
*/
function Connection(inID, outID, weight) {
    this.in = inID;
    this.out = outID;
    if (weight === undefined) {
        weight = 1;
    }
    this.id = inID + ":" + outID;
    this.weight = weight;
}

/**
* The neural network, containing nodes and connections.
* @param {Object} config The configuration to use.
*/
function Network(config) {
    this.nodes = {};
    this.inputs = [];
    this.hidden = [];
    this.outputs = [];
    this.connections = {};
    this.nodes.BIAS = new Node("BIAS", 1);

    if (config !== undefined) {
        var inputNum = config.inputNodes || 0;
        var hiddenNum = config.hiddenNodes || 0;
        var outputNum = config.outputNodes || 0;
        this.createNodes(inputNum, hiddenNum, outputNum);

        if (config.createAllConnections) {
            this.createAllConnections(true);
        }
    }
}

/**
* Populates the network with the given number of nodes of each type.
* @param  {Number} inputNum The number of input nodes to create.
* @param  {Number} hiddenNum The number of hidden nodes to create.
* @param  {Number} outputNum The number of output nodes to create.
*/
Network.prototype.createNodes = function(inputNum, hiddenNum, outputNum) {
    for (var i = 0; i < inputNum; i++) {
        this.addInput();
    }
    for (var j = 0; j < hiddenNum; j++) {
        this.addHidden();
    }
    for (var k = 0; k < outputNum; k++) {
        this.addOutput();
    }
};

/**
* @param {Number} [value] The value to set the node to [Default is 0].
*/
Network.prototype.addInput = function(value) {
    var nodeID = "INPUT:" + this.inputs.length;
    if (value === undefined) {
        value = 0;
    }
    this.nodes[nodeID] = new Node(nodeID, value);
    this.inputs.push(nodeID);
};

/**
* Creates a hidden node.
*/
Network.prototype.addHidden = function() {
    var nodeID = "HIDDEN:" + this.hidden.length;
    this.nodes[nodeID] = new Node(nodeID);
    this.hidden.push(nodeID);
};

/**
* Creates an output node.
*/
Network.prototype.addOutput = function() {
    var nodeID = "OUTPUT:" + this.outputs.length;
    this.nodes[nodeID] = new Node(nodeID);
    this.outputs.push(nodeID);
};

/**
* Returns the node with the given ID.
* @param  {String} nodeID The ID of the node to return.
* @return {Node} The node with the given ID.
*/
Network.prototype.getNodeByID = function(nodeID) {
    return this.nodes[nodeID];
};

/**
* Returns the node of the given type at the given index.
* @param  {String} type  The type of node requested [Accepted arguments: "INPUT", "HIDDEN", "OUTPUT"].
* @param  {Number} index The index of the node (from the array containing nodes of the requested type).
* @return {Node} The node requested. Will return null if no node is found.
*/
Network.prototype.getNode = function(type, index) {
    if (type.toUpperCase() == "INPUT") {
        return this.nodes[this.inputs[index]];
    } else 	if (type.toUpperCase() == "HIDDEN") {
        return this.nodes[this.hidden[index]];
    } else 	if (type.toUpperCase() == "OUTPUT") {
        return this.nodes[this.outputs[index]];
    }
    return null;
};

/**
* Returns the connection with the given ID.
* @param  {String} connectionID The ID of the connection to return.
* @return {Connection} The connection with the given ID.
*/
Network.prototype.getConnection = function(connectionID) {
    return this.connections[connectionID];
};

/**
* Calculates the values of the nodes in the neural network.
*/
Network.prototype.calculate = function calculate() {
    this.updateNodeConnections();
    for (var i = 0; i < this.hidden.length; i++) {
        this.calculateNodeValue(this.hidden[i]);
    }
    for (var j = 0; j < this.outputs.length; j++) {
        this.calculateNodeValue(this.outputs[j]);
    }
};

/**
* Updates the node's to reference the current connections.
*/
Network.prototype.updateNodeConnections = function() {
    for (var nodeKey in this.nodes) {
        this.nodes[nodeKey].incomingConnections = [];
        this.nodes[nodeKey].outgoingConnections = [];
    }
    for (var connectionKey in this.connections) {
        this.nodes[this.connections[connectionKey].in].outgoingConnections.push(connectionKey);
        this.nodes[this.connections[connectionKey].out].incomingConnections.push(connectionKey);
    }
};

/**
* Calculates and updates the value of the node with the given ID. Node values are computed using a sigmoid function.
* @param  {String} nodeId The ID of the node to update.
*/
Network.prototype.calculateNodeValue = function(nodeID) {
    var sum = 0;
    for (var incomingIndex = 0; incomingIndex < this.nodes[nodeID].incomingConnections.length; incomingIndex++) {
        var connection = this.connections[this.nodes[nodeID].incomingConnections[incomingIndex]];
        sum += this.nodes[connection.in].value * connection.weight;
    }
    this.nodes[nodeID].value = sigmoid(sum);
};

/**
* Creates a connection with the given values.
* @param {String} inID The ID of the node that the connection comes from. 
* @param {String} outID The ID of the node that the connection enters.
* @param {Number} [weight] The weight of the connection [Default is 1].
*/
Network.prototype.addConnection = function(inID, outID, weight) {
    if (weight === undefined) {
        weight = 1;
    }
    this.connections[inID + ":" + outID] = new Connection(inID, outID, weight);
};

/**
* Creates all possible connections between nodes, not including connections to the bias node.
* @param  {Boolean} randomWeights Whether to choose a random weight between -1 and 1, or to default to 1.
*/
Network.prototype.createAllConnections = function(randomWeights) {
    if (randomWeights === undefined) {
        randomWeights = false;
    }
    var weight = 1;
    for (var i = 0; i < this.inputs.length; i++) {
        for (var j = 0; j < this.hidden.length; j++) {
            if (randomWeights) {
                weight = Math.random() * 4 - 2;
            }
            this.addConnection(this.inputs[i], this.hidden[j], weight);
        }
        if (randomWeights) {
            weight = Math.random() * 4 - 2;
        }
        this.addConnection("BIAS", this.inputs[i], weight);
    }
    for (var k = 0; k < this.hidden.length; k++) {
        for (var l = 0; l < this.outputs.length; l++) {
            if (randomWeights) {
                weight = Math.random() * 4 - 2;
            }
            this.addConnection(this.hidden[k], this.outputs[l], weight);
        }
        if (randomWeights) {
            weight = Math.random() * 4 - 2;
        }
        this.addConnection("BIAS", this.hidden[k], weight);
    }
};

/**
* Sets the value of the node with the given ID to the given value.
* @param {String} nodeID The ID of the node to modify.
* @param {Number} value The value to set the node to.
*/
Network.prototype.setNodeValue = function(nodeID, value) {
    this.nodes[nodeID].value = value;
};

/**
* Sets the values of the input neurons to the given values.
* @param {Array} array An array of values to set the input node values to.
*/
Network.prototype.setInputs = function(array) {
    for (var i = 0; i < array.length; i++) {
        this.nodes[this.inputs[i]].value = array[i];
    }
};

/**
* Sets the value of multiple nodes, given an object with node ID's as parameters and node values as values.
* @param {Object} valuesByID The values to set the nodes to.
*/
Network.prototype.setMultipleNodeValues = function(valuesByID) {
    for (var key in valuesByID) {
        this.nodes[key].value = valuesByID[key];
    }
};


/**
* A visualization of the neural network, showing all connections and nodes.
* @param {Object} config The configuration to use.
*/
function NetworkVisualizer(config) {
    this.canvas = "NetworkVisualizer";
    this.backgroundColor = "#FFFFFF";
    this.nodeRadius = -1;
    this.nodeColor = "grey";
    this.positiveConnectionColor = "green";
    this.negativeConnectionColor = "red";
    this.connectionStrokeModifier = 1;
    if (config !== undefined) {
        if (config.canvas !== undefined) {
            this.canvas = config.canvas;
        }
        if (config.backgroundColor !== undefined) {
            this.backgroundColor = config.backgroundColor;
        }
        if (config.nodeRadius !== undefined) {
            this.nodeRadius = config.nodeRadius;
        }
        if (config.nodeColor !== undefined) {
            this.nodeColor = config.nodeColor;
        }
        if (config.positiveConnectionColor !== undefined) {
            this.positiveConnectionColor = config.positiveConnectionColor;
        }
        if (config.negativeConnectionColor !== undefined) {
            this.negativeConnectionColor = config.negativeConnectionColor;
        }
        if (config.connectionStrokeModifier !== undefined) {
            this.connectionStrokeModifier = config.connectionStrokeModifier;
        }
    }
}

/**
* Draws the visualized network upon the canvas.
* @param  {Network} network The network to visualize.
*/
NetworkVisualizer.prototype.drawNetwork = function(network) {
    var canv = document.getElementById(this.canvas); 
    var ctx = canv.getContext("2d");
    var radius;
    ctx.fillStyle = this.backgroundColor;
    ctx.fillRect(0, 0, canv.width, canv.height);
    if (this.nodeRadius != -1) {
        radius = this.nodeRadius;
    } else {
        radius = Math.min(canv.width, canv.height) / (Math.max(network.inputs.length, network.hidden.length, network.outputs.length, 3)) / 2.5;
    }
    var nodeLocations = {};
    var inputX = canv.width / 5;
    for (var inputIndex = 0; inputIndex < network.inputs.length; inputIndex++) {
        nodeLocations[network.inputs[inputIndex]] = {x: inputX, y: canv.height / (network.inputs.length) * (inputIndex + 0.5)};
    }
    var hiddenX = canv.width / 2;
    for (var hiddenIndex = 0; hiddenIndex < network.hidden.length; hiddenIndex++) {
        nodeLocations[network.hidden[hiddenIndex]] = {x: hiddenX, y: canv.height / (network.hidden.length) * (hiddenIndex + 0.5)};
    }
    var outputX = canv.width / 5 * 4;
    for (var outputIndex = 0; outputIndex < network.outputs.length; outputIndex++) {
        nodeLocations[network.outputs[outputIndex]] = {x: outputX, y: canv.height / (network.outputs.length) * (outputIndex + 0.5)};
    }
    nodeLocations.BIAS = {x: canv.width / 3, y: radius / 2};
    for (var connectionKey in network.connections) {
        var connection = network.connections[connectionKey];
        //if (connection.in != "BIAS" && connection.out != "BIAS") {
            ctx.beginPath();
            ctx.moveTo(nodeLocations[connection.in].x, nodeLocations[connection.in].y);
            ctx.lineTo(nodeLocations[connection.out].x, nodeLocations[connection.out].y);
            if (connection.weight > 0) {
                ctx.strokeStyle = this.positiveConnectionColor;
            } else {
                ctx.strokeStyle = this.negativeConnectionColor;
            }
            ctx.lineWidth = connection.weight * this.connectionStrokeModifier;
            ctx.lineCap = "round";
            ctx.stroke();
        //}
    }
    for (var nodeKey in nodeLocations) {
        var node = network.getNodeByID(nodeKey);
        ctx.beginPath();
        if (nodeKey == "BIAS") {
            ctx.arc(nodeLocations[nodeKey].x, nodeLocations[nodeKey].y, radius / 2.2, 0, 2 * Math.PI);
        } else {
            ctx.arc(nodeLocations[nodeKey].x, nodeLocations[nodeKey].y, radius, 0, 2 * Math.PI);
        }
        ctx.fillStyle = this.backgroundColor;
        ctx.fill();
        ctx.strokeStyle = this.nodeColor;
        ctx.lineWidth = 3;
        ctx.stroke();
        ctx.globalAlpha = node.value;
        ctx.fillStyle = this.nodeColor;
        ctx.fill();
        ctx.globalAlpha = 1; 	
    }
};


BackpropNetwork.prototype = new Network();
BackpropNetwork.prototype.constructor = BackpropNetwork;

/**
* Neural network that is optimized via backpropagation.
* @param {Object} config The configuration to use.
*/
function BackpropNetwork(config) {
    Network.call(this, config);
    this.inputData = {};
    this.targetData = {};
    this.learningRate = 0.5;
    this.step = 0;
    this.totalErrorSum = 0;
    this.averageError = [];

    if (config !== undefined) {
        if (config.learningRate !== undefined) {
            this.learningRate = config.learningRate;
        }
        if (config.inputData !== undefined) {
            this.setInputData(config.inputData);
        }
        if (config.targetData !== undefined) {
            this.setTargetData(config.targetData);
        }
    }
}

/**
* Backpropagates the neural network, using the input and training data given. Currently does not affect connections to the bias node.
*/
BackpropNetwork.prototype.backpropagate = function() {
    this.step++;
    if (this.inputData[this.step] === undefined) {
        this.averageError.push(this.totalErrorSum / this.step);
        this.totalErrorSum = 0;
        this.step = 0;
    }
    for (var inputKey in this.inputData[this.step]) {
        this.nodes[inputKey].value = this.inputData[this.step][inputKey];
    }
    this.calculate();
    var currentTargetData = this.targetData[this.step];
    var totalError = this.getTotalError();
    this.totalErrorSum += totalError;
    var newWeights = {};
    for (var i = 0; i < this.outputs.length; i++) {
        var outputNode = this.nodes[this.outputs[i]];
        for (var j = 0; j < outputNode.incomingConnections.length; j++) {
            var hiddenToOutput = this.connections[outputNode.incomingConnections[j]];
            var deltaRuleResult = -(currentTargetData[this.outputs[i]] - outputNode.value) * outputNode.value * (1 - outputNode.value) * this.nodes[hiddenToOutput.in].value;
            newWeights[hiddenToOutput.id] = hiddenToOutput.weight - this.learningRate * deltaRuleResult;
        }
    }
    for (var k = 0; k < this.hidden.length; k++) {
        var hiddenNode = this.nodes[this.hidden[k]];
        for (var l = 0; l < hiddenNode.incomingConnections.length; l++) {
            var inputToHidden = this.connections[hiddenNode.incomingConnections[l]];
            var total = 0;
            for (var m = 0; m < hiddenNode.outgoingConnections.length; m++) {
                var outgoing = this.connections[hiddenNode.outgoingConnections[m]];
                var outgoingNode = this.nodes[outgoing.out];
                total += ((-(currentTargetData[outgoing.out] - outgoingNode.value)) * (outgoingNode.value * (1 - outgoingNode.value))) * outgoing.weight;
            }
            var outOverNet = hiddenNode.value * (1 - hiddenNode.value);
            var netOverWeight = this.nodes[inputToHidden.in].value;
            var result = total * outOverNet * netOverWeight;
            newWeights[inputToHidden.id] = inputToHidden.weight - this.learningRate * result;
        }
    }
    for (var key in newWeights) {
        this.connections[key].weight = newWeights[key];
    }
};

/**
* Adds a target result to the target data. This will be compared to the output in order to determine error.
* @param {String} outputNodeID The ID of the output node whose value will be compared to the target.
* @param {Number} target The value to compare against the output when checking for errors.
*/
BackpropNetwork.prototype.addTarget = function(outputNodeID, target) {
    this.targetData[outputNodeID] = target;
};

/**
* Sets the input data that will be compared to the target data.
* @param {Array} array An array containing the data to be inputted (ex. [0, 1] will set the first input node
* to have a value of 0 and the second to have a value of 1). Each array argument represents a single
* step, and will be compared against the parallel set in the target data.
*/
BackpropNetwork.prototype.setInputData = function() {
    var all = arguments;
    if (arguments.length == 1 && arguments[0].constructor == Array) {
        all = arguments[0];
    } 
    this.inputData = {};
    for (var i = 0; i < all.length; i++) {
        var data = all[i];
        var instance = {};
        for (var j = 0; j < data.length; j++) {
            instance["INPUT:" + j] = data[j]; 
        }
        this.inputData[i] = instance;
    }
};

/**
* Sets the target data that will be used to check for total error.
* @param {Array} array An array containing the data to be compared against (ex. [0, 1] will compare the first
* output node against 0 and the second against 1). Each array argument represents a single step.
*/
BackpropNetwork.prototype.setTargetData = function() {
    var all = arguments;
    if (arguments.length == 1 && arguments[0].constructor == Array) {
        all = arguments[0];
    } 
    this.targetData = {};
    for (var i = 0; i < all.length; i++) {
        var data = all[i];
        var instance = {};
        for (var j = 0; j < data.length; j++) {
            instance["OUTPUT:" + j] = data[j]; 
        }
        this.targetData[i] = instance;
    }
};

/**
* Calculates the total error of all the outputs' values compared to the target data.
* @return {Number} The total error.
*/
BackpropNetwork.prototype.getTotalError = function() {
    var sum = 0;
    for (var i = 0; i < this.outputs.length; i++) {
        sum += Math.pow(this.targetData[this.step][this.outputs[i]] - this.nodes[this.outputs[i]].value, 2) / 2;
    }
    return sum;
};

/**
* A gene containing the data for a single connection in the neural network.
* @param {String} inID       The ID of the incoming node.
* @param {String} outID      The ID of the outgoing node.
* @param {Number} weight     The weight of the connection to create.
* @param {Number} innovation The innovation number of the gene.
* @param {Boolean} enabled   Whether the gene is expressed or not.
*/	
function Gene(inID, outID, weight, innovation, enabled) {
    if (innovation === undefined) {
        innovation = 0;
    }
    this.innovation = innovation;
    this.in = inID;
    this.out = outID;
    if (weight === undefined) {
        weight = 1;
    }
    this.weight = weight;
    if (enabled === undefined) {
        enabled = true;
    }
    this.enabled = enabled;
}

/**
* Returns the connection that the gene represents.
* @return {Connection} The generated connection.
*/
Gene.prototype.getConnection = function() {
    return new Connection(this.in, this.out, this.weight);
};

/**
* A genome containing genes that will make up the neural network.
* @param {Number} inputNodes  The number of input nodes to create.
* @param {Number} outputNodes The number of output nodes to create.
*/
function Genome(inputNodes, outputNodes) {
    this.inputNodes = inputNodes;
    this.outputNodes = outputNodes;
    this.genes = [];
    this.fitness = -Number.MAX_VALUE;
    this.globalRank = 0;
    this.randomIdentifier = Math.random();
}

Genome.prototype.containsGene = function(inID, outID) {
    for (var i = 0; i < this.genes.length; i++) {
        if (this.genes[i].inID == inID && this.genes[i].outID == outID) {
            return true;
        }
    }
    return false;
};

/**
* A species of genomes that contains genomes which closely resemble one another, enough so that they are able to breed.
*/
function Species() {
    this.genomes = [];
    this.averageFitness = 0;
}

/**
* Culls the genomes to the given amount by removing less fit genomes.
* @param  {Number} [remaining] The number of genomes to cull to [Default is half the size of the species (rounded up)].
*/
Species.prototype.cull = function(remaining) {
    this.genomes.sort(compareGenomesDescending);
    if (remaining === undefined) {
        remaining = Math.ceil(this.genomes.length / 2);
    }
    while (this.genomes.length > remaining) {
        this.genomes.pop();
    }
};

/**
* Calculates the average fitness of the species.
*/
Species.prototype.calculateAverageFitness = function() {
    var sum = 0;
    for (var j = 0; j < this.genomes.length; j++) {
        sum += this.genomes[j].fitness;
    }
    this.averageFitness = sum / this.genomes.length;
};

/**
* Returns the network that the genome represents.
* @return {Network} The generated network.
*/
Genome.prototype.getNetwork = function() {
    var network = new Network();
    network.createNodes(this.inputNodes, 0, this.outputNodes);
    for (var i = 0; i < this.genes.length; i++) {
        var gene = this.genes[i];
        if (gene.enabled) {
            if (network.nodes[gene.in] === undefined && gene.in.indexOf("HIDDEN") != -1) {
                network.nodes[gene.in] = new Node(gene.in);
                network.hidden.push(gene.in);
            }
            if (network.nodes[gene.out] === undefined && gene.out.indexOf("HIDDEN") != -1) {
                network.nodes[gene.out] = new Node(gene.out);
                network.hidden.push(gene.out);
            }
            network.addConnection(gene.in, gene.out, gene.weight);
        }
    }
    return network;
};

/**
* Creates and optimizes neural networks via neuroevolution, using the Neuroevolution of Augmenting Topologies method.
* @param {Object} config The configuration to use.
*/
function Neuroevolution(config) {
    this.genomes = [];
    this.populationSize = 100;
    this.mutationRates = {
        createConnection: 0.05,
        createNode: 0.02,
        modifyWeight: 0.15,
        enableGene: 0.05,
        disableGene: 0.1,
        createBias: 0.1,
        weightMutationStep: 2
    };
    this.inputNodes = 0;
    this.outputNodes = 0;
    this.elitism = true;
    this.deltaDisjoint = 2;
    this.deltaWeights = 0.4;
    this.deltaThreshold = 2;
    this.hiddenNodeCap = 10;
    this.fitnessFunction = function (network) {log("ERROR: Fitness function not set"); return -1;};
    this.globalInnovationCounter = 1;
    this.currentGeneration = 0;
    this.species = [];
    this.newInnovations = {};
    if (config !== undefined) {
        if (config.populationSize !== undefined) {
            this.populationSize = config.populationSize;
        }
        if (config.inputNodes !== undefined) {
            this.inputNodes = config.inputNodes;
        }
        if (config.outputNodes !== undefined) {
            this.outputNodes = config.outputNodes;
        }
        if (config.mutationRates !== undefined) {
            var configRates = config.mutationRates;
            if (configRates.createConnection !== undefined) {
                this.mutationRates.createConnection = configRates.createConnection;
            }
            if (configRates.createNode !== undefined) {
                this.mutationRates.createNode = configRates.createNode;
            }
            if (configRates.modifyWeight !== undefined) {
                this.mutationRates.modifyWeight = configRates.modifyWeight;
            }
            if (configRates.enableGene !== undefined) {
                this.mutationRates.enableGene = configRates.enableGene;
            }
            if (configRates.disableGene !== undefined) {
                this.mutationRates.disableGene = configRates.disableGene;
            }
            if (configRates.createBias !== undefined) {
                this.mutationRates.createBias = configRates.createBias;
            }
            if (configRates.weightMutationStep !== undefined) {
                this.mutationRates.weightMutationStep = configRates.weightMutationStep;
            }
        }
        if (config.elitism !== undefined) {
            this.elitism = config.elitism;
        }
        if (config.deltaDisjoint !== undefined) {
            this.deltaDisjoint = config.deltaDisjoint;
        }
        if (config.deltaWeights !== undefined) {
            this.deltaWeights = config.deltaWeights;
        }
        if (config.deltaThreshold !== undefined) {
            this.deltaThreshold = config.deltaThreshold;
        }
        if (config.hiddenNodeCap !== undefined) {
            this.hiddenNodeCap = config.hiddenNodeCap;
        }
    }
}

/**
* Populates the population with empty genomes, and then mutates the genomes.
*/
Neuroevolution.prototype.createInitialPopulation = function() {
    this.genomes = [];
    for (var i = 0; i < this.populationSize; i++) {
        var genome = this.linkMutate(new Genome(this.inputNodes, this.outputNodes));
        this.genomes.push(genome);
    }
    this.mutate();
};

/**
* Mutates the entire population based on the mutation rates.
*/
Neuroevolution.prototype.mutate = function() {
    for (var i = 0; i < this.genomes.length; i++) {
        var network = this.genomes[i].getNetwork();
        if (Math.random() < this.mutationRates.createConnection) {
            this.genomes[i] = this.linkMutate(this.genomes[i]);
        }
        if (Math.random() < this.mutationRates.createNode && this.genomes[i].genes.length > 0 && network.hidden.length < this.hiddenNodeCap) {
            var geneIndex = randomNumBetween(0, this.genomes[i].genes.length - 1);
            var gene = this.genomes[i].genes[geneIndex];
            if (gene.enabled && gene.in.indexOf("INPUT") != -1 && gene.out.indexOf("OUTPUT") != -1) {
                var newNum = -1;
                var found = true;
                while (found) {
                    newNum++;
                    found = false;
                    for (var j = 0; j < this.genomes[i].genes.length; j++) {
                        if (this.genomes[i].genes[j].in.indexOf("HIDDEN:" + newNum) != -1 || this.genomes[i].genes[j].out.indexOf("HIDDEN:" + newNum) != -1) {
                            found = true;
                        }
                    }
                }
                if (newNum < this.hiddenNodeCap) {
                    var nodeName = "HIDDEN:" + newNum;
                    this.genomes[i].genes[geneIndex].enabled = false;
                    this.genomes[i].genes.push(new Gene(gene.in, nodeName, 1, this.globalInnovationCounter));
                    this.globalInnovationCounter++;
                    this.genomes[i].genes.push(new Gene(nodeName, gene.out, gene.weight, this.globalInnovationCounter));
                    this.globalInnovationCounter++;
                    network = this.genomes[i].getNetwork();
                }
            }
        }
        if (Math.random() < this.mutationRates.createBias) {
            if (Math.random() > 0.5 && network.inputs.length > 0) {
                var inputIndex = randomNumBetween(0, network.inputs.length - 1);
                if (network.getConnection("BIAS:" + network.inputs[inputIndex]) === undefined) {
                    this.genomes[i].genes.push(new Gene("BIAS", network.inputs[inputIndex]));
                }
            } else if (network.hidden.length > 0) {
                var hiddenIndex = randomNumBetween(0, network.hidden.length - 1);
                if (network.getConnection("BIAS:" + network.hidden[hiddenIndex]) === undefined) {
                    this.genomes[i].genes.push(new Gene("BIAS", network.hidden[hiddenIndex]));
                }
            }
        }
        for (var k = 0; k < this.genomes[i].genes.length; k++) {
            this.genomes[i].genes[k] = this.pointMutate(this.genomes[i].genes[k]);
        }

    }
};

/**
* Attempts to create a new connection gene in the given genome.
* @param  {Genome} genome The genome to mutate.
* @return {Genome} The mutated genome.
*/
Neuroevolution.prototype.linkMutate = function(genome) {
    var network = genome.getNetwork();
    var inNode = "";
    var outNode = "";
    if (Math.random() < 1/3 || network.hidden.length <= 0) {
        inNode = network.inputs[randomNumBetween(0, this.inputNodes - 1)];
        outNode = network.outputs[randomNumBetween(0, this.outputNodes - 1)];
    } else if (Math.random() < 2/3) {
        inNode = network.inputs[randomNumBetween(0, this.inputNodes - 1)];
        outNode = network.hidden[randomNumBetween(0, network.hidden.length - 1)];
    } else {
        inNode = network.hidden[randomNumBetween(0, network.hidden.length - 1)];
        outNode = network.outputs[randomNumBetween(0, this.outputNodes - 1)];
    }
    if (!genome.containsGene(inNode, outNode)) {
        var newGene = new Gene(inNode, outNode, Math.random() * 2 - 1);
        if (this.newInnovations[newGene.in + ":" + newGene.out] === undefined) {
            this.newInnovations[newGene.in + ":" + newGene.out] = this.globalInnovationCounter;
            newGene.innovation = this.globalInnovationCounter;
            this.globalInnovationCounter++;
        } else {
            newGene.innovation = this.newInnovations[newGene.in + ":" + newGene.out];
        }
        genome.genes.push(newGene);
    }
    return genome;
};

/**
* Mutates the given gene based on the mutation rates.
* @param  {Gene} gene The gene to mutate.
* @return {Gene} The mutated gene.
*/
Neuroevolution.prototype.pointMutate = function(gene) {
    if (Math.random() < this.mutationRates.modifyWeight) {
        gene.weight = gene.weight + Math.random() * this.mutationRates.weightMutationStep * 2 - this.mutationRates.weightMutationStep; 
    }
    if (Math.random() < this.mutationRates.enableGene) {
        gene.enabled = true;
    }
    if (Math.random() < this.mutationRates.disableGene) {
        gene.enabled = false;
    }
    return gene;
};

/**
* Crosses two parent genomes with one another, forming a child genome.
* @param  {Genome} firstGenome  The first genome to mate.
* @param  {Genome} secondGenome The second genome to mate.
* @return {Genome} The resultant child genome.
*/
Neuroevolution.prototype.crossover = function(firstGenome, secondGenome) {
    var child = new Genome(firstGenome.inputNodes, firstGenome.outputNodes);
    var firstInnovationNumbers = {};
    for (var h = 0; h < firstGenome.genes.length; h++) {
        firstInnovationNumbers[firstGenome.genes[h].innovation] = h;
    }
    var secondInnovationNumbers = {};
    for (var j = 0; j < secondGenome.genes.length; j++) {
        secondInnovationNumbers[secondGenome.genes[j].innovation] = j;
    }
    for (var i = 0; i < firstGenome.genes.length; i++) {
        var geneToClone;
        if (secondInnovationNumbers[firstGenome.genes[i].innovation] !== undefined) {
            if (Math.random() < 0.5) {
                geneToClone = firstGenome.genes[i];
            } else {
                geneToClone = secondGenome.genes[secondInnovationNumbers[firstGenome.genes[i].innovation]];
            }
        } else {
            geneToClone = firstGenome.genes[i];
        }
        child.genes.push(new Gene(geneToClone.in, geneToClone.out, geneToClone.weight, geneToClone.innovation, geneToClone.enabled)); 		
    }
    for (var k = 0; k < secondGenome.genes.length; k++) {
        if (firstInnovationNumbers[secondGenome.genes[k].innovation] === undefined) {
            var secondDisjoint = secondGenome.genes[k];
            child.genes.push(new Gene(secondDisjoint.in, secondDisjoint.out, secondDisjoint.weight, secondDisjoint.innovation, secondDisjoint.enabled)); 		
        }
    }
    return child;
};

/**
* Evolves the population by creating a new generation and mutating the children.
*/
Neuroevolution.prototype.evolve = function() {
    this.currentGeneration++;
    this.newInnovations = {};
    this.genomes.sort(compareGenomesDescending);
    var children = [];
    this.speciate();
    this.cullSpecies();
    this.calculateSpeciesAvgFitness();

    var totalAvgFitness = 0;
    var avgFitnesses = [];
    for (var s = 0; s < this.species.length; s++) {
        totalAvgFitness += this.species[s].averageFitness;
        avgFitnesses.push(this.species[s].averageFitness);
    }
    var arr = [];
    for (var j = 0; j < this.species.length; j++) {
        var childrenToMake = Math.floor(this.species[j].averageFitness / totalAvgFitness * this.populationSize);
        arr.push(childrenToMake);
        if (childrenToMake > 0) {
            children.push(this.species[j].genomes[0]);
        }
        for (var c = 0; c < childrenToMake - 1; c++) {
            children.push(this.makeBaby(this.species[j]));
        }
    }
    while (children.length < this.populationSize) {
        children.push(this.makeBaby(this.species[randomNumBetween(0, this.species.length - 1)]));
    }
    this.genomes = [];
    this.genomes = this.genomes.concat(children);
    this.mutate();
    this.speciate();
    log(this.species.length);
};

/**
* Sorts the genomes into different species.
*/
Neuroevolution.prototype.speciate = function() {
    this.species = [];
    for (var i = 0; i < this.genomes.length; i++) {
        var placed = false;
        for (var j = 0; j < this.species.length; j++) {
            if (!placed && this.species[j].genomes.length > 0 && this.isSameSpecies(this.genomes[i], this.species[j].genomes[0])) {
                this.species[j].genomes.push(this.genomes[i]);
                placed = true;
            }
        }
        if (!placed) {
            var newSpecies = new Species();
            newSpecies.genomes.push(this.genomes[i]);
            this.species.push(newSpecies);
        }
    }
};

/**
* Culls all the species to the given amount by removing less fit members of each species.
* @param  {Number} [remaining] The number of genomes to cull all the species to [Default is half the size of the species].
*/
Neuroevolution.prototype.cullSpecies = function(remaining) {
    var toRemove = [];
    for (var i = 0; i < this.species.length; i++) {
        this.species[i].cull(remaining);
        if (this.species[i].genomes.length < 1) {
            toRemove.push(this.species[i]);
        }
    }
    for (var r = 0; r < toRemove.length; r++) {
        this.species.remove(toRemove[r]);
    }
};

/**
* Calculates the average fitness of all the species.
*/
Neuroevolution.prototype.calculateSpeciesAvgFitness = function() {
    for (var i = 0; i < this.species.length; i++) {
        this.species[i].calculateAverageFitness();
    }
};

/**
* Creates a baby in the given species, with fitter genomes having a higher chance to reproduce.
* @param  {Species} species The species to create a baby in.
* @return {Genome} The resultant baby.
*/
Neuroevolution.prototype.makeBaby = function(species) {
    var mum = species.genomes[randomWeightedNumBetween(0, species.genomes.length - 1)];
    var dad = species.genomes[randomWeightedNumBetween(0, species.genomes.length - 1)];
    return this.crossover(mum, dad);
};

/**
* Calculates the fitness of all the genomes in the population.
*/
Neuroevolution.prototype.calculateFitnesses = function() {
    for (var i = 0; i < this.genomes.length; i++) {
        this.genomes[i].fitness = this.fitnessFunction(this.genomes[i].getNetwork());
    }
};

/**
* Returns the relative compatibility metric for the given genomes.
* @param  {Genome} genomeA The first genome to compare.
* @param  {Genome} genomeB The second genome to compare.
* @return {Number} The relative compatibility metric. 
*/
Neuroevolution.prototype.getCompatibility = function(genomeA, genomeB) {
    var disjoint = 0;
    var totalWeight = 0;
    var aInnovationNums = {};
    for (var i = 0; i < genomeA.genes.length; i++) {
        aInnovationNums[genomeA.genes[i].innovation] = i;
    }
    var bInnovationNums = [];
    for (var j = 0; j < genomeB.genes.length; j++) {
        bInnovationNums[genomeB.genes[j].innovation] = j;
    }
    for (var k = 0; k < genomeA.genes.length; k++) {
        if (bInnovationNums[genomeA.genes[k].innovation] === undefined) {
            disjoint++;
        } else {
            totalWeight += Math.abs(genomeA.genes[k].weight - genomeB.genes[bInnovationNums[genomeA.genes[k].innovation]].weight);
        }
    }
    for (var l = 0; l < genomeB.genes.length; l++) {
        if (aInnovationNums[genomeB.genes[l].innovation] === undefined) {
            disjoint++;
        }
    }
    var n = Math.max(genomeA.genes.length, genomeB.genes.length);
    return this.deltaDisjoint * (disjoint / n) + this.deltaWeights * (totalWeight / n);
};

/**
* Determines whether the given genomes are from the same species.
* @param  {Genome}  genomeA The first genome to compare.
* @param  {Genome}  genomeB The second genome to compare.
* @return {Boolean} Whether the given genomes are from the same species.
*/
Neuroevolution.prototype.isSameSpecies = function(genomeA, genomeB) {
    return this.getCompatibility(genomeA, genomeB) < this.deltaThreshold;
};

/**
* Returns the genome with the highest fitness in the population.
* @return {Genome} The elite genome.
*/
Neuroevolution.prototype.getElite = function() {
    this.genomes.sort(compareGenomesDescending);
    return this.genomes[0];
};


//Private static functions
function sigmoid(t) {
   return 1 / (1 + Math.exp(-t));
}

function randomNumBetween(min, max) {
   return Math.floor(Math.random() * (max - min + 1) + min);
}

function randomWeightedNumBetween(min, max) {
   return Math.floor(Math.pow(Math.random(), 2) * (max - min + 1) + min);
}

function compareGenomesAscending(genomeA, genomeB) {
   return genomeA.fitness - genomeB.fitness;
}

function compareGenomesDescending(genomeA, genomeB) {
   return genomeB.fitness - genomeA.fitness;
}

Array.prototype.remove = function() {
   var what, a = arguments, L = a.length, ax;
   while (L && this.length) {
       what = a[--L];
       while ((ax = this.indexOf(what)) !== -1) {
           this.splice(ax, 1);
       }
   }
   return this;
};


function log(text) {
   console.log(text);
}
```

# ../index.html

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Inverted Pendulum Neural Network</title>
    <style>
        body {
            margin: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f0f0f0;
            flex-direction: column;
        }
        canvas {
            background-color: #ffffff;
            margin-bottom: 20px;
        }
        button {
            margin: 10px;
            padding: 10px 20px;
            font-size: 16px;
        }
    </style>
</head>
<body>
    <canvas id="pendulumCanvas" width="600" height="400"></canvas>
    <canvas id="networkCanvas" width="600" height="400"></canvas> <!-- Canvas thứ hai cho mạng neural -->
    <button id="saveButton">Save Model</button>
    <button id="loadButton">Load Model</button>
    <script src="ai.js"></script>
    <script src="main.js"></script>
</body>
</html>

```

# ../main.js

```
// Lấy tham chiếu đến canvas và các nút
const canvas = document.getElementById("pendulumCanvas");
const ctx = canvas.getContext("2d");

const networkCanvas = document.getElementById("networkCanvas");
const networkCtx = networkCanvas.getContext("2d");

const saveButton = document.getElementById("saveButton");
const loadButton = document.getElementById("loadButton");

let isDragging = false;  // Trạng thái kéo thả
let mouseX = 0;  // Vị trí chuột trên trục X

// Các thông số của con lắc và giỏ
const g = 9.81; // Gia tốc trọng trường
let cartX = canvas.width / 2; // Vị trí của giỏ
let cartVelocity = 0;
let pendulumAngle = Math.PI / 4; // Góc ban đầu của con lắc (radians)
let pendulumAngularVelocity = 0;
const pendulumLength = 150; // Chiều dài con lắc
const cartWidth = 50;
const cartHeight = 30;
const mass = 1; // Khối lượng của con lắc

// Số lần lặp qua dữ liệu để huấn luyện
const epochs = 10000;

// Dữ liệu đầu vào mẫu và đầu ra mong muốn
const trainingData = [
    {
        inputs: [0.1, 300, 0.05, 0.02, 1], // [pendulumAngle, cartX, pendulumAngularVelocity, cartVelocity, mass]
        target: [0.5] // Lực mong muốn
    },
    {
        inputs: [-0.2, 200, -0.03, -0.01, 1],
        target: [-0.5]
    },

    // Tình huống con lắc hơi lệch phải, giỏ ở giữa, vận tốc góc nhỏ
    {
        inputs: [0.1, 300, 0.05, 0.02, 1], // [pendulumAngle, cartX, pendulumAngularVelocity, cartVelocity, mass]
        target: [0.5] // Lực mong muốn
    },
    // Tình huống con lắc lệch trái, giỏ lệch trái, vận tốc góc lớn hơn
    {
        inputs: [-0.2, 200, -0.03, -0.01, 1],
        target: [-0.5]
    },
    // Tình huống con lắc lệch mạnh về bên phải, giỏ lệch về phải, tốc độ giỏ nhanh
    {
        inputs: [0.5, 350, 0.1, 0.3, 1],
        target: [0.8]
    },
    // Con lắc lệch trái, giỏ ở giữa, vận tốc góc rất nhỏ
    {
        inputs: [-0.1, 300, -0.01, 0, 1],
        target: [-0.2]
    },
    // Con lắc ở góc lớn hơn, giỏ ở đầu trái, vận tốc lớn
    {
        inputs: [-0.4, 100, -0.05, 0.05, 1],
        target: [-1.0]
    },
    // Con lắc thẳng đứng, giỏ ở giữa, không có vận tốc
    {
        inputs: [0, 300, 0, 0, 1],
        target: [0]
    },
    // Con lắc lệch phải, giỏ lệch trái, vận tốc góc vừa phải
    {
        inputs: [0.2, 150, 0.03, -0.2, 1],
        target: [0.3]
    },
    // Con lắc lệch trái, giỏ ở giữa, vận tốc góc lớn
    {
        inputs: [-0.5, 300, -0.08, 0.1, 1],
        target: [-0.7]
    },
    // Tình huống giỏ và con lắc đều lệch về bên trái
    {
        inputs: [-0.3, 200, -0.04, -0.15, 1],
        target: [-0.6]
    },
    // Tình huống giỏ lệch về phải, con lắc lệch bên phải
    {
        inputs: [0.4, 400, 0.06, 0.1, 1],
        target: [0.9]
    },
    // Tình huống con lắc và giỏ ở giữa với khối lượng khác
    {
        inputs: [0, 300, 0, 0, 1.5], // Thay đổi khối lượng
        target: [0]
    },
    // Con lắc lệch trái mạnh với khối lượng khác
    {
        inputs: [-0.3, 250, -0.07, -0.05, 1.2],
        target: [-0.4]
    },
    // Con lắc lệch phải nhẹ, khối lượng lớn hơn
    {
        inputs: [0.15, 330, 0.02, 0.03, 2],
        target: [0.2]
    },
    // Tình huống giỏ đang di chuyển nhanh sang phải và con lắc hơi lệch phải
    {
        inputs: [0.2, 350, 0.05, 0.5, 1],
        target: [0.6]
    },
    // Giỏ di chuyển nhanh sang trái, con lắc lệch trái
    {
        inputs: [-0.3, 250, -0.06, -0.5, 1],
        target: [-0.6]
    },
    // Giỏ đứng yên, con lắc lệch trái nhẹ
    {
        inputs: [-0.1, 300, -0.02, 0, 1],
        target: [-0.2]
    },
    // Thêm nhiều mẫu dữ liệu vào đây để mô phỏng các tình huống khác nhau
];

// Tạo neural network để điều khiển hệ thống
const network = new BackpropNetwork({
    inputNodes: 5, // Góc của con lắc, vị trí giỏ, tốc độ góc, tốc độ giỏ, khối lượng
    hiddenNodes: 6,
    outputNodes: 1, // Lực áp dụng lên giỏ
    createAllConnections: true
});

// Hàm huấn luyện
function trainNetwork() {
    for (let epoch = 0; epoch < epochs; epoch++) {
        let totalError = 0;
        for (const data of trainingData) {
            // Đặt đầu vào
            network.setInputs(data.inputs);
            network.calculate();

            // Lan truyền ngược để cập nhật trọng số
            network.setTargetData([data.target]);
            network.backpropagate();

            // Tính sai số
            const error = Math.abs(data.target[0] - network.getNode("OUTPUT", 0).value);
            totalError += error;
        }

        if (epoch % 100 === 0) {
            console.log(`Epoch: ${epoch}, Total Error: ${totalError}`);
        }
    }
}

// Hàm lưu trọng số vào file JSON
function saveNetworkWeights() {
    const networkData = {
        nodes: {},
        connections: {}
    };

    // Lưu các giá trị của nodes
    for (const nodeID in network.nodes) {
        networkData.nodes[nodeID] = {
            value: network.nodes[nodeID].value,
            bias: network.nodes[nodeID].bias
        };
    }

    // Lưu các trọng số của connections
    for (const connectionID in network.connections) {
        networkData.connections[connectionID] = {
            in: network.connections[connectionID].in,
            out: network.connections[connectionID].out,
            weight: network.connections[connectionID].weight
        };
    }

    // Chuyển dữ liệu thành chuỗi JSON
    const networkJSON = JSON.stringify(networkData);

    // Tạo blob và lưu file
    const blob = new Blob([networkJSON], { type: 'application/json' });
    const link = document.createElement('a');
    link.href = URL.createObjectURL(blob);
    link.download = 'network_weights.json';
    link.click();
}

// Hàm nạp trọng số mạng từ JSON
function loadNetworkWeights(networkJSON) {
    const data = JSON.parse(networkJSON);

    // Nạp giá trị của nodes
    for (const nodeID in data.nodes) {
        network.nodes[nodeID].value = data.nodes[nodeID].value;
        network.nodes[nodeID].bias = data.nodes[nodeID].bias;
    }

    // Nạp trọng số của connections
    for (const connectionID in data.connections) {
        network.connections[connectionID].weight = data.connections[connectionID].weight;
    }
}

// Sử dụng Fetch API để tải tệp JSON từ server
function fetchAndLoadWeights() {
    fetch('network_weights.json')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            console.log('Weights loaded:', data);
            loadNetworkWeights(JSON.stringify(data));
        })
        .catch(error => console.error('Error loading JSON:', error));
}

// Hàm tính toán các lực tác động và cập nhật vị trí
function update() {
    // Lấy dữ liệu đầu vào cho neural network
    network.setInputs([pendulumAngle, cartX, pendulumAngularVelocity, cartVelocity, mass]);
    network.calculate();

    // Neural network đưa ra lực áp dụng lên giỏ
    const force = network.getNode("OUTPUT", 0).value * 10 - 5;

    // Cập nhật các giá trị vật lý dựa trên lực
    const angularAcceleration = (g * Math.sin(pendulumAngle)) / pendulumLength;
    pendulumAngularVelocity += angularAcceleration;
    pendulumAngle += pendulumAngularVelocity;

    // Cập nhật vị trí của giỏ
    cartVelocity += force;
    cartX += cartVelocity;

    // Giới hạn giỏ trong biên của canvas
    if (cartX < 0) cartX = 0;
    if (cartX > canvas.width - cartWidth) cartX = canvas.width - cartWidth;

    // Vẽ lại mọi thứ
    draw();
}

// Hàm vẽ giỏ và con lắc lên canvas
function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Vẽ giỏ
    ctx.fillStyle = "#0000ff";
    ctx.fillRect(cartX, canvas.height - cartHeight, cartWidth, cartHeight);

    // Vẽ con lắc
    const pendulumX = cartX + cartWidth / 2 + pendulumLength * Math.sin(pendulumAngle);
    const pendulumY = canvas.height - cartHeight - pendulumLength * Math.cos(pendulumAngle);

    ctx.beginPath();
    ctx.moveTo(cartX + cartWidth / 2, canvas.height - cartHeight);
    ctx.lineTo(pendulumX, pendulumY);
    ctx.stroke();

    ctx.beginPath();
    ctx.arc(pendulumX, pendulumY, 10, 0, 2 * Math.PI);
    ctx.fillStyle = "#ff0000";
    ctx.fill();
}

// Sự kiện chuột: bắt đầu kéo giỏ
canvas.addEventListener('mousedown', function (event) {
    const rect = canvas.getBoundingClientRect();
    mouseX = event.clientX - rect.left;

    // Kiểm tra nếu chuột đang ở trên giỏ
    if (mouseX > cartX && mouseX < cartX + cartWidth) {
        isDragging = true;
    }
});

// Sự kiện chuột: kéo giỏ
canvas.addEventListener('mousemove', function (event) {
    if (isDragging) {
        const rect = canvas.getBoundingClientRect();
        mouseX = event.clientX - rect.left;

        // Cập nhật vị trí của giỏ theo chuột
        cartX = mouseX - cartWidth / 2;

        // Giới hạn giỏ trong biên của canvas
        if (cartX < 0) cartX = 0;
        if (cartX > canvas.width - cartWidth) cartX = canvas.width - cartWidth;

        draw();  // Vẽ lại khi đang kéo giỏ
    }
});

// Sự kiện chuột: thả giỏ
canvas.addEventListener('mouseup', function () {
    if (isDragging) {
        isDragging = false;
        cartVelocity = 0;  // Đặt lại tốc độ giỏ khi thả
    }
});

// Tạo một NetworkVisualizer để vẽ nodes và connections
const visualizer = new NetworkVisualizer({
    canvas: "networkCanvas",
    nodeRadius: 20,
    nodeColor: "blue",
    positiveConnectionColor: "green",
    negativeConnectionColor: "red",
    connectionStrokeModifier: 2
});

// Hàm để vẽ mạng neural lên canvas
function drawNetwork() {
    visualizer.drawNetwork(network);
}

// Chạy vòng lặp game và vẽ cả mạng neural lên canvas thứ hai
function gameLoop() {
    update();
    drawNetwork(); // Vẽ mạng neural
    requestAnimationFrame(gameLoop);
}

// Hàm cập nhật vẽ lại các tham số của các node lên canvas
function drawNodeParameters() {
    const fontSize = 12;
    networkCtx.font = `${fontSize}px Arial`;
    networkCtx.textAlign = "center";
    networkCtx.textBaseline = "middle";

    // Duyệt qua từng node và vẽ các tham số lên
    for (const nodeID in network.nodes) {
        const node = network.getNodeByID(nodeID);
        const location = visualizer.nodeLocations[nodeID]; // Lấy vị trí của node

        // Hiển thị giá trị của node (value) bên trong node
        if (location) {
            networkCtx.fillText(`Value: ${node.value.toFixed(2)}`, location.x, location.y);
            networkCtx.fillText(`Bias: ${node.bias.toFixed(2)}`, location.x, location.y + fontSize);
        }
    }
}

// Chỉnh sửa vòng lặp để vẽ các tham số bên trong các node
function gameLoop() {
    update();
    drawNetwork();
    drawNodeParameters(); // Vẽ tham số bên trong các node
    requestAnimationFrame(gameLoop);
}

// Gán sự kiện cho nút Save
saveButton.addEventListener('click', function () {
    saveNetworkWeights();  // Lưu trọng số mạng sau khi huấn luyện
});

// Gán sự kiện cho nút Load
loadButton.addEventListener('click', function () {
    fetchAndLoadWeights();  // Tải và nạp trọng số từ tệp JSON
});

// Bắt đầu vòng lặp
gameLoop();

```

