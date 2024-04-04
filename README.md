# IP Address Range Excel Generator

This Python script generates an Excel file containing IP addresses within a specified range of IP addresses.

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/marcosfermin/ip_address_excel_generator.git
   ```

2. Navigate to the project directory:

   ```bash
   cd ip_address_excel_generator
   ```

3. Install the required dependencies:

   ```bash
   pip install openpyxl
   ```

4. Run the script:

   ```bash
   python ip_address_excel_generator.py
   ```

## Description

The script generates IP addresses within a given range (specified by a starting and ending IP address) and saves them to an Excel file. The range should be within the same Class B network (i.e., /16 subnet) to ensure valid IP addresses.

## Requirements

- Python 3.x
- `openpyxl` library

## Installation

You can install the required dependencies using pip:

```bash
pip install openpyxl
```

## Usage Example

```python
start_ip = '192.168.0.0'
end_ip = '192.168.255.255'

ips = generate_ips(start_ip, end_ip)
generate_excel_file(ips)
```

This will generate an Excel file named "IP_addresses.xlsx" containing IP addresses from 192.168.0.0 to 192.168.255.255.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request for any improvements or additional features.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This script utilizes the `openpyxl` library for handling Excel files.