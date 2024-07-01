# Neural Networks


# This episode will be just theory in the next one we write the handwritten digits project

# Neural Network Structure:
"""
In a neural network we have multiple layers of neurons

    Image 1: '#7 - neuron layers.ppng'

The first layer is the Input Layer, here we input all the training and testing data
The last layer is the Output Layer, a.k.a. our result. 
i.e. if we try to classify something we input all of our values in the first layer
 and in the end get a classification, if its for example two neurons in the end
 it tells us the probability of how much it's class 1 or class 2, or
 we could also have just 1 output neuron with a regression

In between we have the Hidden Layers that add complexity and sophistication to the model. 
In an ordinary 'feed-forward' Neural Network we connect every neuron with of one layer
 with every neuron of the next layer.
The neuron connections are random in the beginning, if we do supervised learning
 we have some Training Feature Data in the input layer and some Training Labels in the output

For the example of Handwritten digits, the input data would be a 28px \times 28px image
 of a handwritten digit which means 784px with values from 0 to 255 indicating 
 how black or white it is and that many input neurons, 
 and the output training labels would be digits from 0-9
 All these points and connections need to be adjusted and trained so they output the correct
 desired result so that they can be used on untrained data to classify
"""

# Individual neurons:
"""
Every neuron has a certain input, either the input layer of our data, 
 or the input of another neuron / always from another neuron in feed-forward Neural Network
The input is fed into the neuron and this neuron has a certain activation function 
 (in image called 'a'), this activation function determines what happens with this input
 / how it gets proccessed, tells us how "bright"/activated our neuron is
 i.e. input is 1, and activation fuinction let's say outputs 0.9 (think K-C-M matrix)
We could also use the basic perception model (outdated and not used anymore) with a bias, 
 basically taking the input and subtracting the bias to calculate the activation.
 Most primitive form of neuron - perceptron

    Image 2: '#7 - individual neuron.png'   
 
Then this Neuron has outputs (unless in last layer) and this output is an input
 for the next neurons

What's important is that every connection has a certain weight, this weight
 determines how important is the activation of a neuron to the next neuron
 if very important to the neuron with connection \omega_1 then \omega_1 is big
 This is what the Neural Network adjusts to train, we do this with tens of 
 thousands of examples of training data.

We have many different activation functions. 
One example would be the Sigmoid function
 (shown in graph, looks basically like fermi porazdelitev inversed) - it transforms
 every input value to value between 0 to 1
Another example would be RELU function - Rectified Linear Unit
 if value is negative it says 0, and if the value is positive we just return it
 f(x)_{RELU} = max{0, input_value(x)}
"""

# Gradient Descent algorithm:
"""
Algorithm that allows our neural network to be optimized. 
While training the network it needs to adjust weights and biases for better results
The ideal case for the handwritten digits example would be if we input a 2 handwritten
 that the output neuron corresponding to the digit 2 would get activation = 1,
 and all the other neurons would have the activation of 0, 0 probability.

    Image 3: '#7 - gradient descent.png'
  
But in reality each neuron gets a bit of activation. From all of these we 
 compare the values / probabilities of all of the output neurons and we come
 up with the Loss Function - indicates how wrong our function is
 It's not the Error - that would be the % of missclassification, how many were
 not classified correctly
 The loss function tells you how much you're off of the right result
 our goal is to minimize the Loss Function
"""

# Loss Function:
"""
We're trying to minimize it, if it's low our model is performing well
When we input the weights and biases and the desired outcomes, 
 the loss function calculates how wrong we are

    Image 4: '#7 - loss function.png'

What we want to do, is to adjust the weights and biases in such a way that we
 reach the minimum of the loss function (just think variacijski račun),
 a thousand dimensional graph

To roll down we need to go down the steepest slope, aka just gradient function
 and we take a tiny step in that direction  $ - \varepsilon \cdot \nabla Loss  $
 and we rinse and repeat until we're in the local minimum

We can also choose other starting points to find other minimums non locally.
"""