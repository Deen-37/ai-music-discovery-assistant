import ollama


class LLMClient(model="gemma3:4b"):
    """
    Handles communication with the local Llama model using Ollama.
    """

    def __init__(self, model="llama3.2"):
        # Store the model name so it can be changed easily later.
        self.model = model

    def generate(self, prompt: str) -> str:
        """
        Sends the user's prompt to the LLM and returns the generated response.
        """

        # Send a chat request to the local Llama model.
        response = ollama.chat(
            model=self.model,              # Which Ollama model to use.
            messages=[
                {
                    "role": "user",        # This message is coming from the user.
                    "content": prompt      # The actual question or prompt.
                }
            ]
        )

        # Extract only the generated text from the response object.
        return response["message"]["content"]