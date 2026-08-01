class Guardrails:
    """
    Validates that the AI only recommends retrieved songs.
    """

    def validate(self, recommendations: list, valid_titles: list):
        # Store invalid song titles.
        invalid_titles = []

        # Check each recommendation.
        for song in recommendations:

            # Get the recommended song title.
            title = song["title"]

            # Verify the title exists in the retrieved songs.
            if title not in valid_titles:
                invalid_titles.append(title)

        # Return whether the response is valid.
        return len(invalid_titles) == 0, invalid_titles