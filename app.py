# %%
import pandas as pd
from transformers import pipeline
from transformers.pipelines import SUPPORTED_TASKS


# %%
print(SUPPORTED_TASKS.keys())

# %%
model_qa = pipeline("question-answering", model = "deepset/roberta-base-squad2")

# %%
df_questions = pd.read_csv("dados/games_faq.csv")
df_questions

# %%
def question_answer(question):
    context = df_questions[df_questions["question"] == question]
    result = model_qa(question=question, context=context["answer"].values[0])
    return result["answer"]

# %%
question_answer("How can I improve my rank?")

# %%
question_answer("Why is my game crashing?")

# %%
question_answer("How do I unlock a new character?")

# %%
question_answer("How can I get rare items?")

# %%
question_answer("How do I contact game support?")

# %%
question_answer("How do I create a clan?")

# %%
import gradio as gd

# %%
app = gd.Interface(
    fn = question_answer,
    inputs=gd.Dropdown(choices=list(df_questions["question"]), label="Qual a sua dúvida?"),
    outputs="text",
    title = "FAQ Games",
    description="Selecione uma pergunta do FAQ"
)

# %%
app.launch(share=True)


