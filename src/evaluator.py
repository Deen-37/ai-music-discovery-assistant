import time

from src.agent import MusicAgent


class Evaluator:
    """
    Runs a collection of predefined test cases
    to evaluate the reliability of the AI system.
    """

    def __init__(self):
        # Initialize the AI system.
        self.agent = MusicAgent()

        # Test prompts.
        self.test_cases = [
            "I need relaxing music while studying.",
            "Play energetic music for the gym.",
            "I want happy pop songs.",
            "I feel sad today.",
            "Play some jazz while drinking coffee.",
            "I want music for sleeping.",
            "Recommend music for coding.",
            "I need party music.",
            "I want peaceful music.",
            "Play confident hip hop."
        ]

    def run(self):
        """
        Execute every test case and print a summary.
        """

        passed = 0
        failed = 0

        total_time = 0

        print("=" * 60)
        print("Running AI Evaluation...")
        print("=" * 60)

        for index, prompt in enumerate(self.test_cases, start=1):

            print(f"\nTest {index}")
            print(f"Prompt: {prompt}")

            start = time.time()

            try:

                result = self.agent.recommend(prompt)

                elapsed = time.time() - start
                total_time += elapsed

                print("PASS")
                print(f"Response Time: {elapsed:.2f} sec")

                print(result)

                passed += 1

            except Exception as error:

                print("FAIL")
                print(error)

                failed += 1

        print("\n" + "=" * 60)
        print("Evaluation Summary")
        print("=" * 60)

        print(f"Tests Run : {len(self.test_cases)}")
        print(f"Passed    : {passed}")
        print(f"Failed    : {failed}")

        if passed + failed > 0:
            print(
                f"Average Response Time: "
                f"{total_time / (passed + failed):.2f} sec"
            )


if __name__ == "__main__":
    evaluator = Evaluator()
    evaluator.run()