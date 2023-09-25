from ProblemSetLoader import ProblemSetLoader
from TestRunner import TestRunner
from ScoreCalculator import ScoreCalculator
from ScoreKeeper import ScoreKeeper
from Logger import Logger

# Instantiate classes
problem_set_loader = ProblemSetLoader()
test_runner = TestRunner()
score_calculator = ScoreCalculator()
score_keeper = ScoreKeeper()
logger = Logger()

# Load problem sets and execute tests
# problem_sets should be a list of file paths to different problem sets
problem_sets = ["path/to/problem_set_1", "path/to/problem_set_2"]
for problem_set_path in problem_sets:
    problem_set = problem_set_loader.load_problem_set(problem_set_path)
    test_results = test_runner.run_tests(problem_set)
    scores = score_calculator.calculate_scores(test_results)
    score_keeper.update_scores(scores)
    # Log the results using logger

# Generate report and output to file
report = logger.generate_report()
logger.output_to_file(report, "test_report.json")

# Print the total scores
print(score_keeper.get_total_scores())
