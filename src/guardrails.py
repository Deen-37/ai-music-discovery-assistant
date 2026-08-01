import re


class Guardrails:
    """
    Validates AI responses to ensure recommendations
    are supported by the retrieved dataset.
    """

    def validate(self, response: str, valid_titles: list) -> tuple[bool, list]:
        """
        Checks whether every recommended song exists in the dataset.

        Args:
            response (str): AI-generated response.
            valid_titles (list): Song titles retrieved from the dataset.

        Returns:
            tuple:
                bool  -> True if response is valid.
                list  -> Invalid song titles.
        """

        # Store any hallucinated song titles.
        invalid_titles = []

        # Search for quoted song titles.
        matches = re.findall(r'"([^"]+)"', response)

        # Compare each extracted title against the retrieved songs.
        for title in matches:
            if title not in valid_titles:
                invalid_titles.append(title)

        # The response is valid only if no invalid titles exist.
        return len(invalid_titles) == 0, invalid_titles