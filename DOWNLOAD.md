# 📥 Download T5 Legal Narrative Model

The large model files are hosted on HuggingFace Hub for better performance and reliability.

## 🤗 Direct Download from HuggingFace Hub

### Option 1: Using Transformers Library (Recommended)
```python
from transformers import T5Tokenizer, T5ForConditionalGeneration

# Automatically downloads and caches the model
tokenizer = T5Tokenizer.from_pretrained("lemkin-ai/t5-legal-narrative")
model = T5ForConditionalGeneration.from_pretrained("lemkin-ai/t5-legal-narrative", from_tf=True)
```

### Option 2: Manual Download via CLI
```bash
# Install HuggingFace Hub CLI
pip install huggingface_hub

# Download all model files
huggingface-cli download lemkin-ai/t5-legal-narrative --local-dir ./models/t5-legal-narrative/
```

### Option 3: Git Clone from HuggingFace
```bash
# Clone the model repository
git clone https://huggingface.co/lemkin-ai/t5-legal-narrative
```

## 📊 Model Files Available on HuggingFace Hub

| File | Size | Description |
|------|------|-------------|
| `tf_model.h5` | 1.1GB | TensorFlow model weights |
| `config.json` | 1KB | Model configuration |
| `generation_config.json` | 1KB | Generation parameters |
| `tokenizer_config.json` | 1KB | Tokenizer configuration |
| `spiece.model` | 768KB | SentencePiece tokenizer |
| `special_tokens_map.json` | 1KB | Special tokens mapping |

## 🌐 Model Hub URL
**https://huggingface.co/lemkin-ai/t5-legal-narrative**

## ⚡ Quick Start
```python
from transformers import T5Tokenizer, T5ForConditionalGeneration

# Load model
tokenizer = T5Tokenizer.from_pretrained("lemkin-ai/t5-legal-narrative")
model = T5ForConditionalGeneration.from_pretrained("lemkin-ai/t5-legal-narrative", from_tf=True)

# Example usage - Legal narrative generation
prompt = "Summarize the following legal evidence: The defendant was found at the scene with the murder weapon."
inputs = tokenizer.encode(prompt, return_tensors="pt")

# Generate narrative
outputs = model.generate(
    inputs, 
    max_length=512, 
    temperature=0.7,
    do_sample=True,
    top_p=0.9
)

narrative = tokenizer.decode(outputs[0], skip_special_tokens=True)
print("Generated narrative:", narrative)
```

## 🎯 Supported Narrative Types
- Legal Summaries
- Factual Findings
- Legal Analysis
- Executive Summaries
- Conclusions & Recommendations
- Timeline Narratives
- Evidence Synthesis
- Relationship Descriptions

---
*For complete documentation, see the main repository README and model card on HuggingFace Hub.* 