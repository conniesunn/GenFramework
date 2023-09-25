class TestRunner:

    def run_tests(self, problem_set):
        """Run all tests for a given problem set."""
        test_cases = self._load_test_cases(problem_set['ID'])
        results = []

        for test_case in test_cases:
            expected_output = test_case['expected_output']
            # Replace with the actual execution of the code
            actual_output = self._execute_test(problem_set['code'], test_case['input'])
            results.append(self._compare_output(actual_output, expected_output))

        return results

    def _load_test_cases(self, problem_id):
        # Implement loading test cases from JSON or another source
        pass

    def _execute_test(self, code, input_data):
        # Implement executing the test and capturing the output
        pass

    def _compare_output(self, actual_output, expected_output):
        # Implement comparing the outputs and returning the comparison result
        pass
