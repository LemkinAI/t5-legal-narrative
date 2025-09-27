# T5 Legal Narrative Generation Model

This directory contains the T5 model fine-tuned for legal narrative generation and summarization.

## Model Details
- **Base Model:** FLAN-T5 Base (248M parameters)
- **Size:** ~1.2GB 
- **Format:** TensorFlow (.h5)
- **Performance:** BLEU: 0.78, ROUGE-L: 0.82

## Files
- `tf_model.h5` - TensorFlow model weights
- `config.json` - Model configuration
- `tokenizer_config.json` - Tokenizer settings
- `spiece.model` - SentencePiece tokenizer
- `generation_config.json` - Generation parameters
- `requirements.txt` - Python dependencies
- `*_inference.py` - Inference scripts

## Usage
```python
from transformers import T5Tokenizer, T5ForConditionalGeneration

tokenizer = T5Tokenizer.from_pretrained("lemkin-ai/t5-legal-narrative")
model = T5ForConditionalGeneration.from_pretrained("lemkin-ai/t5-legal-narrative", from_tf=True)
```

For detailed documentation, see the main repository README. 