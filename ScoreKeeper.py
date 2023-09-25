class ScoreKeeper:

    def __init__(self):
        self.total_scores = {
            "readability_score": 0,
            "efficiency_score": 0,
            "modularity_score": 0,
            "functionality_score": 0,
            "accuracy_score": 0,
            "reusability_score": 0,
            "overall_score": 0,
        }

    def update_scores(self, scores):
        """Update total scores with the new scores."""
        for key in scores:
            self.total_scores[key] += scores[key]

    def get_total_scores(self):
        """Retrieve the total scores."""
        return self.total_scores
