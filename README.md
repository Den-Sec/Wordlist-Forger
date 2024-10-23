# WordListForger

A powerful and customizable wordlist generator designed for cybersecurity professionals, penetration testers, and ethical hackers. This tool helps create tailored wordlists for use in password cracking techniques such as dictionary attacks, as well as for advanced scenarios requiring custom patterns.

## Features

- **Leet Speak Variations**: Generate 1337 substitutions for input words automatically.
- **Special Character Combinations**: Incorporate user-specified special characters into passwords.
- **Custom Number Inclusion**: Add numbers, including specific date ranges and current date components.
- **Pattern-Based Generation**: Use customizable patterns with placeholders to create passwords in specific formats.
- **Optimized Performance**: Efficient memory management and generators to handle large wordlists without overloading your system.
- **Interactive Prompts**: A user-friendly command-line interface to guide you step by step.
- **Ethical Use**: Strictly intended for authorized penetration testing and educational purposes.

## Disclaimer

**This tool is intended for educational purposes and authorized penetration testing only. Unauthorized use of this tool is prohibited. The author is not responsible for any misuse, illegal activity, or damage caused by this tool. Always ensure you have explicit permission to test any system using this tool.**

## Installation

### Prerequisites

- Python 3.6 or higher.

### Installation Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Den-Sec/WordListForger.git
   cd WordListForger
   ```

2. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the script using Python:

```bash
python main.py
```

### Interactive Prompts

The tool will guide you through a series of interactive prompts:

1. **Enter Basic Words**: Input words separated by spaces (e.g., `admin password login`).
2. **Enter Special Characters**: Input special characters separated by spaces (e.g., `! @ # $ %`).
3. **Enter Numbers**: Input numbers separated by spaces (e.g., `1234 2021`).
4. **Generate Numbers from Date Range**: Optionally specify a date range to include all years within that range.
5. **Specify Password Length**: Define the minimum and maximum password lengths.
6. **Custom Character Set**: Optionally specify a custom set of characters to include.
7. **Maximum Pattern Length**: Define the maximum number of placeholders to combine in patterns.

### Placeholders in Patterns

- `{W}`: Words (including leet variations)
- `{N}`: Numbers
- `{S}`: Special Characters
- `{C}`: Custom Character Set

### Example

When prompted:

- **Basic Words**: `admin`
- **Special Characters**: `@ !`
- **Numbers**: `2021`
- **Date Range**: `No`
- **Password Length**: `Min 6, Max 12`
- **Custom Character Set**: `No`
- **Maximum Pattern Length**: `2`

The tool will generate passwords like:

- `Admin2021`
- `adm1n@`
- `@Admin`
- `adm1n2021`
- `@adm1n`

### Output

After generation, you can choose to save the wordlist to a file (default is `wordlist.txt`).

## Best Practices

- **Use Ethically**: Only use this tool on systems you have explicit permission to test.
- **Manage Input Sizes**: Be mindful of the number of words and variations to prevent excessive generation times.
- **Adjust Max Combinations**: Modify the `MAX_COMBINATIONS` parameter in the script if needed, but be cautious of resource usage.

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue to discuss potential changes or improvements.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contact

**Author**: Dennis Sepede (Cybersecurity Specialist)  
**Email**: [dennisepede@proton.me](mailto:dennisepede@proton.me)  
**GitHub**: [Den-Sec](https://github.com/Den-Sec)

---

## Summary

- **Enhanced Interface**: User-friendly CLI interface for effortless wordlist generation.
- **Comprehensive Features**: Includes leet speak, custom characters, and flexible pattern generation.
- **Ethical and Legal Usage**: Emphasizes responsible use in cybersecurity activities.

## Next Steps

1. **Test the Tool**: Run the script and verify that everything works as expected.
2. **Share the Tool**: Consider sharing this tool on GitHub or other platforms to benefit the cybersecurity community.
3. **Promote Ethical Use**: Encourage ethical usage in all communications to reinforce positive practices.
4. **Gather Feedback**: Engage with peers and the cybersecurity community to gather feedback for future enhancements.

---

Feel free to reach out if you have any questions or need further assistance!

