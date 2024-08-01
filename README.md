# Password Generator

###### Technologies:
<p align="center">
<img src="https://img.icons8.com/color/75/000000/python.png" width="75" height="75" alt="Python" style="margin: 10px 15px 0 15px;" />
</p>

### Try it!

To run the Password Generator application, follow the instructions in the Setup section below.

## Project Structure

- `password_generator.py`: Contains the implementation of the Password Generator function.

## Setup

### Prerequisites

- Python 3 installed

### Installation Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/creinis/password-generator-fcc-scicomp-py-cert.git
   cd password-generator-fcc-scicomp-py-cert
   ```

2. Run the Password Generator script:
   ```bash
   python3 password_generator.py
   ```

## Password Generator

### Functionality

The Password Generator creates strong, random passwords based on specified criteria, including length, the number of digits, special characters, uppercase letters, and lowercase letters. The function ensures the generated password meets all specified constraints.

### Practical Use Case

The Password Generator is useful for creating secure passwords for online accounts, ensuring they are strong and meet various security requirements. This tool can be used by individuals who want to enhance their password security or by developers needing to generate passwords for user accounts in applications.

### Benefits

- **Security:** Generates strong, random passwords to enhance security.
- **Customization:** Allows specifying the length and composition of the password.
- **Constraint Checking:** Ensures the generated password meets all specified constraints.
- **Python Standard Library:** Utilizes the `secrets` module for secure random generation.

## How to Use

1. Run the `password_generator.py` script:
   ```bash
   python3 password_generator.py
   ```

2. Call the `generate_password` function with the desired parameters.

### Example Usage

```python
from password_generator import generate_password

# Generate a password with default parameters
new_password = generate_password()
print('Generated password:', new_password)

# Generate a password with custom parameters
custom_password = generate_password(length=16, nums=2, special_chars=2, uppercase=2, lowercase=2)
print('Generated custom password:', custom_password)
```

### Example Output

```plaintext
Generated password: lK#9fJ!vTm3ZxQ2vWp
Generated custom password: D!5r@k7Gq2Pm#x4L
```

## Function Parameters

- `length`: The total length of the password (default is 20).
- `nums`: The minimum number of digits (default is 1).
- `special_chars`: The minimum number of special characters (default is 1).
- `uppercase`: The minimum number of uppercase letters (default is 1).
- `lowercase`: The minimum number of lowercase letters (default is 1).

### Constraints

- The generated password must contain at least the specified number of digits, special characters, uppercase letters, and lowercase letters.
- The length of the password must be sufficient to accommodate all specified constraints.

---
#### This is a FreeCodeCamp Challenge for Scientific Computing with Python Projects Certification.
<p align="center">
<img src="https://cdn.freecodecamp.org/platform/universal/fcc_primary.svg" width="250" height="75" alt="freeCodeCamp" style="margin: 0 15px; opacity: 0.6" />
</p>
