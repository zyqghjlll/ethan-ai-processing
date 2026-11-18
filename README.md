# ethan-ai-processing

## Standalone LiteLLM + Groq example

This example sends a sample message to Groq through LiteLLM and prints the
response. It runs independently of the existing FastAPI `/classify` endpoint.
Integrating the two is reserved for a later issue.

From the project directory, create and activate a virtual environment (or activate
your existing one), then install the example's dependencies:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-example.txt
```

If you do not already have a `.env` file, copy `.env.example` to `.env`. If you
already have one, add any missing settings without overwriting your existing key.
Set `GROQ_API_KEY` to your key from the [Groq console](https://console.groq.com/keys).
Optionally set `GROQ_MODEL` to a Groq model ID; the default is
`openai/gpt-oss-20b`. Do not include the `groq/` prefix: the script adds it.
You can also export these variables in your shell; shell values take precedence.

```sh
python litellm_example.py
```

A successful run prints a short response. This makes a real API request and
requires network access, a valid API key, and access to the selected model.
If the provider rejects the request, check the reported error, your key, model
access, and account limits. Requests use a 30-second timeout.

Keep credentials in `.env` (already ignored by Git) or your shell environment.
Never put real keys in `.env.example` or commit them.

See the [LiteLLM Groq documentation](https://docs.litellm.ai/docs/providers/groq)
for provider configuration. `requirements-example.txt` installs only dependencies
for this standalone example; it does not install the existing FastAPI application.
