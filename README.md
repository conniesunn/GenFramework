# ChatGPT Coding Ability Test Framework

This framework is designed to test and benchmark the coding abilities of ChatGPT across various dimensions such as readability, efficiency, modularity, functionality, accuracy, and reusability. The framework is extendable to support new coding solution generators and measures of coding. The results of the testing are output in a structured JSON format.

## Table of Contents
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Adding New Benchmarks](#adding-new-benchmarks)
- [Output Format](#output-format)

## Getting Started

### Prerequisites
- Python 3.x installed on your machine.

### Installation
1. Clone the repository or download the project files to your local machine.
2. Navigate to the project directory in your terminal.
3. Run `python main.py` to execute the testing framework.

## Usage
1. Add problem sets in supported formats (JSON, Python files, Text files) to the designated directory.
2. Update the `problem_sets` list in `main.py` with the paths to the new problem sets.
3. Execute `main.py` to run the tests and generate the report.

## Adding New Benchmarks
1. Define new test cases and add them to the respective problem set.
2. If a new measure of coding is introduced, extend the `ScoreCalculator` class to incorporate the calculation of the new metric.
3. If a new coding solution generator is introduced, implement the necessary logic in the `TestRunner` class to execute the code accordingly.

## Output Format
The results are output in a structured JSON format in a file named `test_report.json`. This file contains detailed test results, including expected output, actual output, pass/fail status for each test case, and a summary with scores for each category and an overall score.

Feel free to extend the framework and add additional features or metrics as needed. Contributions to improve the framework are welcome.
