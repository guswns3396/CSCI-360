import numpy as np
# from lab5_utils import log_loss, sigmoid, ArtificialNeuralNetwork
from lab5_utils import relu, mean_squared_error, ArtificialNeuralNetwork

def d_mse(y, y_hat):
    return -1 * (y - y_hat)


def d_relu(x):
    result = x.copy()
    result[result > 0] = 1
    result[result <= 0] = 0
    return result

# consider how you can use ArtificialNeuralNetwork.forward and ArtificialNeuralNetwork.at_layer to help with BP
def train(
    neural_network,
    training_inputs,
    training_labels,
    n_epochs,
    learning_rate=0.001
):
    losses = []

    for epoch in range(n_epochs):
        # feedforward to get a, z, and y_hat for each epoch
        y_hat, a_mem, z_mem = neural_network.forward(training_inputs)
        m = y_hat.shape[1]

        # add loss (mse) for epoch
        loss = mean_squared_error(training_labels, y_hat)
        losses.append(loss)

        dAl = d_mse(training_labels, y_hat)
        for j in range(len(neural_network.layers)):
            l = len(neural_network.layers) - j - 1
            wl = neural_network.layers[l]
            Al_1 = a_mem[-(j+1)]
            dzl = dAl * d_relu(z_mem[-(j+1)])
            dwl = np.dot(dzl, Al_1.T)
            db = (1/m) * np.sum(dzl)
            dAl = np.dot(wl.T, dzl)

            neural_network.layers[l] -= learning_rate * dwl
            neural_network.biases[l] -= learning_rate * db

    return losses


def extra_credit(x_train, y_train, x_test, y_test):
    #populate this dictionary with your extra credit experiments...
    results = {
        "architectures": [],
        "n_epochs": [],
        "learning_rate": [],
        "training_losses": [],
        "evaluation_mean_squared_error": []
    }

    return results