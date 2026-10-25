import unittest
from score import rank


def sample():
    return [{"id":"test", "name":"Test", "buyer":"Businesses", "problem":"Too much manual research", "scores":{
        "pain_urgency":3,"willingness_to_pay":4,"buyer_access":2,"reuse_feasibility":4,"distribution":2,"execution_safety":4
        },"evidence":[
            {"url":"https://example.com/price", "date":"2026-10-24", "type":"pricing","note":"competitor list price"},
            {"url":"https://jobs.example.com/123", "date":"2026-10-24", "type":"buyer_signal","note":"real request"},
            {"url":"https://another.example.com/offer", "date":"2026-10-24", "type":"competitor","note":"existing offer"}]}]


class ScoreTest(unittest.TestCase):
    def test_ranks_not_validated(self):
        result = rank(sample())[0]
        self.assertEqual(result["score"], 62.0)
        self.assertEqual(result["status"], "RANKABLE_UNVALIDATED")
        self.assertEqual(result["buyer_validation"], "NOT_RUN")
        self.assertIsNone(result["verified_revenue_usd"])

    def test_no_buyer_signal_requires_more_research(self):
        c = sample(); c[0]["evidence"][1]["type"] = "anecdote"
        self.assertEqual(rank(c)[0]["status"], "MORE_RESEARCH_REQUIRED")

    def test_rejects_duplicate(self):
        c = sample()
        with self.assertRaisesRegex(ValueError, "Duplicate"):
            rank(c+c)

    def test_rejects_bool_score(self):
        c = sample(); c[0]["scores"]["distribution"] = True
        with self.assertRaisesRegex(ValueError, "scores"):
            rank(c)

    def test_rejects_untrusted_url(self):
        c = sample(); c[0]["evidence"][0]["url"] = "file:///etc/passwd"
        with self.assertRaisesRegex(ValueError, "HTTPS"):
            rank(c)

    def test_rejects_missing_dimension(self):
        c = sample(); del c[0]["scores"]["execution_safety"]
        with self.assertRaisesRegex(ValueError, "dimensions"):
            rank(c)


if __name__ == "__main__":
    unittest.main()
