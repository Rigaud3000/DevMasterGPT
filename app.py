import gradio as gr
from gpt_tools import (
    handle_chat, handle_code,
    handle_explain, handle_translate, handle_debug
)
from project_builder import generate_project
import json

chat_state = gr.State([])

def save_history(history):
    with open("chat_history.json", "w") as f:
        json.dump(history, f)
    return "chat_history.json"

with gr.Blocks() as app:
    gr.Markdown("# 🤖 DevMasterGPT: Full-Stack Coding Genius")

    model_selector = gr.Radio(
        ["tiiuae/falcon-rw-1b", "mistralai/Mistral-7B-Instruct-v0.1"],
        label="Choose AI Model",
        value="tiiuae/falcon-rw-1b"
    )

    with gr.Tab("💬 Chat Assistant"):
        chatbot = gr.Chatbot(label="🧠 Dev Chat")
        chat_input = gr.Textbox(placeholder="Ask anything coding-related...", lines=1)
        send_btn = gr.Button("Send")
        save_btn = gr.Button("💾 Save Chat History")
        chat_file = gr.File(label="Chat History JSON")

        send_btn.click(fn=handle_chat, inputs=[chat_input, chat_state, model_selector], outputs=[chatbot, chat_state])
        save_btn.click(fn=save_history, inputs=chat_state, outputs=chat_file)

    with gr.Tab("💻 Code Lab"):
        code_input = gr.Code(label="Editor", language="python")
        code_output = gr.Code(label="Response", language="python")
        run_btn = gr.Button("Run / Fix")
        run_btn.click(fn=handle_code, inputs=[code_input, model_selector], outputs=code_output)

    with gr.Tab("🛠️ Code Tools"):
        code_explain = gr.Button("Explain Code")
        code_translate = gr.Button("Translate to English")
        code_debug = gr.Button("Debug Code")
        tool_output = gr.Textbox(label="Tool Output")

        code_explain.click(fn=handle_explain, inputs=[code_input, model_selector], outputs=tool_output)
        code_translate.click(fn=handle_translate, inputs=[code_input, model_selector], outputs=tool_output)
        code_debug.click(fn=handle_debug, inputs=[code_input, model_selector], outputs=tool_output)

    with gr.Tab("🚀 Project Generator"):
        gen_project_btn = gr.Button("Generate Full Project")
        scaffold_output = gr.Textbox(label="Project Structure", lines=10)
        gen_project_btn.click(fn=generate_project, outputs=scaffold_output)

    with gr.Tab("📂 File Tools"):
        file_upload = gr.File(label="Upload Code File", type="text")
        file_view = gr.Code(label="Uploaded File Content", language="python")
        export_btn = gr.Button("Export as .py File")
        file_download = gr.File(label="Download File")

        def load_file(f):
            return open(f.name, 'r').read()

        def export_code(code):
            filename = "dev_output.py"
            with open(filename, "w") as f:
                f.write(code)
            return filename

        file_upload.change(fn=load_file, inputs=file_upload, outputs=file_view)
        export_btn.click(fn=export_code, inputs=file_view, outputs=file_download)

    with gr.Tab("📘 Markdown Preview"):
        md_input = gr.Textbox(label="Paste Markdown (README.md)", lines=12)
        md_output = gr.Markdown()
        md_preview_btn = gr.Button("Preview")
        md_preview_btn.click(fn=lambda x: x, inputs=md_input, outputs=md_output)

app.launch()
