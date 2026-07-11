from openai import OpenAI

MODEL = "gpt-4o-mini"


def get_reply(api_key: str, system_prompt: str, messages: list[dict]) -> str:
    """messages: [{"role": "user"|"assistant", "content": str}, ...]
    Returns assistant text, or the LOCKED error string on any exception."""
    try:
        client = OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model=MODEL,
            max_completion_tokens=400,
            temperature=0.2,
            messages=[{"role": "system", "content": system_prompt}] + messages,
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"[llm_client] {type(e).__name__}: {e}")
        return "Something went wrong on my end — please try that question again in a moment."


def get_reply_stream(api_key: str, system_prompt: str, messages: list[dict]):
    """Same contract as get_reply, but yields text chunks for st.write_stream.
    On any exception, yields the LOCKED error string once and stops."""
    try:
        client = OpenAI(api_key=api_key)
        stream = client.chat.completions.create(
            model=MODEL,
            max_completion_tokens=400,
            temperature=0.2,
            messages=[{"role": "system", "content": system_prompt}] + messages,
            stream=True,
        )
        for chunk in stream:
            if not chunk.choices:
                continue
            delta = chunk.choices[0].delta.content
            if delta:
                yield delta
    except Exception as e:
        print(f"[llm_client] {type(e).__name__}: {e}")
        yield "Something went wrong on my end — please try that question again in a moment."
