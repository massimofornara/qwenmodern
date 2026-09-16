import gradio as gr
from demo.chatbot.app import demo

# Esporta l'app FastAPI nativa per il runtime serverless
app = gr.mount_gradio_app(demo.app, demo, path="/")
