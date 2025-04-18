import os
from transformers import pipeline

def load_model(model_name):
    return pipeline(
        "text-generation",
        model=model_name,
        token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
    )

def handle_chat(message, history=[], model_name="tiiuae/falcon-rw-1b"):
    chat_model = load_model(model_name)
    prompt = f"[INST] {message} [/INST]"
    try:
        response = chat_model(prompt, max_new_tokens=300, temperature=0.7)[0]['generated_text']
        reply = response.replace(prompt, "").strip()
    except Exception as e:
        reply = f"⚠️ Error: {str(e)}"
    history.append((message, reply))
    return history, history

def handle_code(code, model_name="tiiuae/falcon-rw-1b"):
    chat_model = load_model(model_name)
    prompt = f"[INST] Fix, optimize, and explain this code:\n{code} [/INST]"
    try:
        response = chat_model(prompt, max_new_tokens=300, temperature=0.7)[0]['generated_text']
        return response.replace(prompt, "").strip()
    except Exception as e:
        return f"⚠️ Error: {str(e)}"

def handle_explain(code, model_name="tiiuae/falcon-rw-1b"):
    return handle_code(f"Explain this code: {code}", model_name)

def handle_translate(code, model_name="tiiuae/falcon-rw-1b"):
    return handle_code(f"Translate this code into plain English: {code}", model_name)

def handle_debug(code, model_name="tiiuae/falcon-rw-1b"):
    return handle_code(f"Find and fix any bugs in this code: {code}", model_name)
