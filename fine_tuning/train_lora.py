import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments, Trainer
from peft import LoraConfig, get_peft_model, TaskType
from datasets import load_dataset

MODEL_NAME = "meta-llama/Llama-2-7b-chat-hf"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, torch_dtype=torch.float16, device_map="auto")

# LoRA Configuration
lora_config = LoraConfig(
    task_type=TaskType.CAUSAL_LM,
    r=16, lora_alpha=32, lora_dropout=0.1,
    target_modules=["q_proj", "v_proj"]
)
model = get_peft_model(model, lora_config)

# Load Custom Dataset
dataset = load_dataset("json", data_files={"train": "data/train.json", "test": "data/test.json"})

# Training Arguments
training_args = TrainingArguments(
    output_dir="./results",
    per_device_train_batch_size=4,
    evaluation_strategy="epoch",
    save_strategy="epoch",
    learning_rate=2e-5,
    num_train_epochs=3
)

# Train Model
trainer = Trainer(model=model, args=training_args, train_dataset=dataset["train"])
trainer.train()
model.save_pretrained("fine_tuned_lora_model")