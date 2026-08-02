import json


class Guardrails:
    """
    Validates AI-generated recommendations before they are shown
    to the user.
    """

    def validate(self, recommendations, valid_titles):
        """
        Validate the LLM response.

        Returns:
            (bool, list): Validation result and invalid titles.
        """

        invalid_titles = []

        # Response must be a list.
        if not isinstance(recommendations, list):
            return False, ["Response is not a list"]

        for recommendation in recommendations:

            # Every recommendation must contain these fields.
            required = {"title", "artist", "reason"}

            if not required.issubset(recommendation.keys()):
                return False, ["Missing required fields"]

            # Song title must exist in retrieved songs.
            if recommendation["title"] not in valid_titles:
                invalid_titles.append(recommendation["title"])

        return len(invalid_titles) == 0, invalid_titles