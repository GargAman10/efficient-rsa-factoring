# RSA Factoring

## Overview

The RSA Factoring project is a web application that utilizes Pollard's Rho Algorithm for efficient factorization of RSA numbers, which are the product of two prime numbers. This tool is designed to demonstrate the effectiveness of probabilistic algorithms in number theory and their application in cryptography.

## Table of Contents

- [Features](#features)
- [How It Works](#how-it-works)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- 
## Features

- Efficient factorization of large numbers using Pollard's Rho Algorithm.
- User-friendly web interface to input numbers for factorization.
- Displays the factors in a well-structured table.
- Animated UI for a better user experience.

## How It Works

1. **Input Handling**: Users can input multiple numbers, one per line, in the provided text area.
2. **Pollard's Rho Algorithm**: The application employs the Pollard's Rho Algorithm, a probabilistic method, to find one prime factor of the input number.
3. **Result Display**: Once a factor is found, the application displays the results, showing the original number and its corresponding factors in a neatly formatted table.

## Installation

To run this project locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/rsa-factoring.git
   cd rsa-factoring
Set Up the Environment: Ensure you have Python and Flask installed. If not, you can install Flask using pip:

bash
pip install Flask

Run the Application: Start the Flask development server:

bash
python app.py


**Usage**
Open the web application in your browser.
Enter the numbers you wish to factor, one per line, in the provided text area.
Click the "Factor Numbers" button.
The results will be displayed in a table format below the form, showing the original number and its factors.

**Technologies Used**
Frontend: HTML, CSS
Backend: Python, Flask
Algorithm: Pollard's Rho Algorithm for number factorization
