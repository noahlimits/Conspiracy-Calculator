import numpy as np
import matplotlib.pyplot as plt

# Constants
p = 4e-3  # Intrinsic probability of failure per person per year
paper_title = "On the Viability of Conspiratorial Beliefs"
paper_authors = "David Robert Grimes"
formula = "L(t) = 1 - e^(-p * N * t)"

def calculate_time_to_exposure(num_conspirators, p, threshold=0.99):
    """
    Calculate the time to almost certain exposure of a conspiracy.
    
    :param num_conspirators: Number of people involved in the conspiracy
    :param p: Intrinsic probability of failure per person per year
    :param threshold: Probability threshold for exposure
    :return: Time to exposure in years
    """
    phi = num_conspirators * p
    time_to_exposure = -np.log(1 - threshold) / phi
    return time_to_exposure

def plot_time_to_exposure(num_conspirators, p):
    """
    Plot the time to almost certain exposure over a range of years.
    
    :param num_conspirators: Number of people involved in the conspiracy
    :param p: Intrinsic probability of failure per person per year
    """
    years = np.arange(1, 150, 1)
    probabilities = 1 - np.exp(-p * num_conspirators * years)
    crossover_point = calculate_time_to_exposure(num_conspirators, p)
    plt.figure(figsize=(10, 6))
    plt.plot(years, probabilities, label=f'{num_conspirators} Conspirators')
    plt.axhline(y=0.99, color='r', linestyle='--', label='99% Exposure Threshold')
    plt.axvline(x=crossover_point, color='g', linestyle='--', label='Crossover Point')
    plt.annotate(f'{crossover_point:.2f} years', xy=(crossover_point, 0.99), xytext=(crossover_point+10, 0.8),
                 arrowprops=dict(facecolor='black', shrink=0.05), fontsize=9)
    plt.title('Time to Almost Certain Exposure of a Conspiracy')
    plt.xlabel('Time (years)')
    plt.ylabel('Probability of Exposure')
    plt.figtext(0.5, 0.01, f"Paper: {paper_title} by {paper_authors}", ha="center", fontsize=8)
    plt.figtext(0.5, 0.95, f"Formula: {formula}", ha="center", fontsize=8)
    plt.legend()
    plt.grid(True)
    plt.show()

# Example usage:
num_conspirators = int(input("Enter the number of conspirators: "))
time_to_exposure = calculate_time_to_exposure(num_conspirators, p)
print(f"Time to almost certain exposure: {time_to_exposure:.2f} years")

plot_time_to_exposure(num_conspirators, p)
