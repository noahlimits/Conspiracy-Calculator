import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

# Constants
# Assuming an average failure rate (lambda) per person per year
# This value would need to be estimated from historical data or literature
lambda_per_person = 0.01  # This is an example value

def calculate_time_to_exposure(num_conspirators, lambda_per_person, threshold=0.99):
    """
    Calculate the time to almost certain exposure of a conspiracy using Poisson distribution.
    
    :param num_conspirators: Number of people involved in the conspiracy
    :param lambda_per_person: Average failure rate per person per year
    :param threshold: Probability threshold for exposure
    :return: Time to exposure in years
    """
    # Total lambda is the rate per person times the number of conspirators
    total_lambda = lambda_per_person * num_conspirators
    
    # Start at year 0 and increment until we reach the threshold probability
    time_to_exposure = 0
    cumulative_probability = 0
    while cumulative_probability < threshold:
        # Calculate the probability of zero events up to the current time
        cumulative_probability = 1 - poisson.cdf(0, total_lambda * time_to_exposure)
        time_to_exposure += 1
    
    return time_to_exposure - 1  # Subtract 1 because we start at year 0

def plot_time_to_exposure(num_conspirators, lambda_per_person):
    """
    Plot the time to almost certain exposure over a range of years using Poisson distribution.
    
    :param num_conspirators: Number of people involved in the conspiracy
    :param lambda_per_person: Average failure rate per person per year
    """
    years = np.arange(0, 150, 1)
    total_lambda = lambda_per_person * num_conspirators
    probabilities = 1 - poisson.cdf(0, total_lambda * years)
    crossover_point = calculate_time_to_exposure(num_conspirators, lambda_per_person)
    
    plt.figure(figsize=(10, 6))
    plt.plot(years, probabilities, label=f'{num_conspirators} Conspirators')
    plt.axhline(y=0.99, color='r', linestyle='--', label='99% Exposure Threshold')
    plt.axvline(x=crossover_point, color='g', linestyle='--', label='Crossover Point')
    plt.annotate(f'{crossover_point} years', xy=(crossover_point, 0.99), xytext=(crossover_point+5, 0.8),
                 arrowprops=dict(facecolor='black', shrink=0.05), fontsize=9)
    plt.title('Time to Almost Certain Exposure of a Conspiracy')
    plt.xlabel('Time (years)')
    plt.ylabel('Probability of Exposure')
    plt.legend()
    plt.grid(True)
    plt.show()

# Example usage:
num_conspirators = int(input("Enter the number of conspirators: "))
time_to_exposure = calculate_time_to_exposure(num_conspirators, lambda_per_person)
print(f"Time to almost certain exposure: {time_to_exposure} years")

plot_time_to_exposure(num_conspirators, lambda_per_person)
