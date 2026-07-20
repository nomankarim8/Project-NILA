import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from nila import detect_language, get_reply


def test_get_reply_without_api_key_returns_fallback_message():
    os.environ.pop("OPENAI_API_KEY", None)
    reply = get_reply("Hello")
    assert "api key is not set" in reply.lower() or "couldn't reach the ai service" in reply.lower()


def test_detect_language_recognizes_bengali_text():
    assert detect_language("তুমি কেমন আছো") == "bn"
    assert detect_language("How are you") == "en"
