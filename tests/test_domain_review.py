import unittest

from src.policyglass.domain_review import DomainReview, review_lane, review_score


class DomainReviewTests(unittest.TestCase):
    def test_review_lane(self) -> None:
        item = DomainReview(68, 47, 19, 52)
        self.assertEqual(review_score(item), 178)
        self.assertEqual(review_lane(item), "ship")


if __name__ == "__main__":
    unittest.main()
