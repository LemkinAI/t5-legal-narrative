# Model Card for T5 Legal Narrative Generation

## Model Details

### Model Description
- **Developed by:** Lemkin AI Research Team
- **Model type:** T5-large fine-tuned for legal narrative generation
- **Language(s) (NLP):** Primarily English, with limited multilingual support
- **License:** MIT
- **Finetuned from model:** google/t5-large

### Model Sources
- **Repository:** https://github.com/LemkinAI/t5-legal-narrative
- **Hugging Face Hub:** https://huggingface.co/lemkin-ai/t5-legal-narrative
- **Paper:** [Coming Soon]

## Uses

### Direct Use
The model can be used directly for:
- Generating legal case summaries from structured data
- Creating investigation reports from evidence
- Drafting legal briefs from key points
- Producing human rights documentation narratives
- Synthesizing complex legal information

### Downstream Use
The model can be fine-tuned for:
- Specific legal jurisdictions
- Custom document templates
- Domain-specific terminology
- Additional languages

### Out-of-Scope Use
- Medical report generation
- Creative writing
- Real-time transcription
- Legal advice generation without human oversight

## Bias, Risks, and Limitations

### Bias
- Training data primarily from international criminal law
- May reflect Western legal perspectives
- Better performance on common legal scenarios

### Risks
- Generated text requires human review for accuracy
- Should not be used for automated legal decisions
- May hallucinate facts not present in input

### Limitations
- Maximum input length: 512 tokens
- Maximum output length: 1024 tokens
- Best performance with structured inputs
- Requires fact-checking for critical applications

## Training Details

### Training Data
- **Size:** 500k+ legal documents
- **Sources:**
  - International court decisions (35%)
  - Human rights reports (25%)
  - Legal briefs and memoranda (20%)
  - Investigation reports (10%)
  - Academic legal papers (10%)

### Training Procedure

#### Preprocessing
- Text cleaning: Legal citation standardization
- Format conversion: Structured data to narrative pairs
- Data augmentation: Template variation

#### Training Hyperparameters
- **Training regime:** fp16 mixed precision
- **Batch size:** 16
- **Learning rate:** 1e-4
- **Epochs:** 5
- **Warmup steps:** 500
- **Weight decay:** 0.01
- **Optimizer:** AdamW

## Evaluation

### Testing Data
- Hold-out test set: 10% of total data
- Expert-annotated evaluation set: 1,000 examples

### Metrics

#### Automatic Metrics
| Metric | Score | Description |
|--------|-------|-------------|
| ROUGE-1 | 0.847 | Unigram overlap |
| ROUGE-2 | 0.723 | Bigram overlap |
| ROUGE-L | 0.789 | Longest common subsequence |
| BLEU-4 | 0.741 | 4-gram precision |
| BERTScore | 0.892 | Semantic similarity |

#### Human Evaluation (Legal Experts)
| Aspect | Score (1-10) | Agreement |
|--------|--------------|-----------|
| Factual Accuracy | 9.1 | 0.87 |
| Legal Coherence | 8.9 | 0.85 |
| Completeness | 8.7 | 0.82 |
| Professional Style | 9.3 | 0.90 |
| Overall Quality | 9.0 | 0.88 |

### Results Summary
- **ROUGE-L:** 0.789
- **Expert Rating:** 9.0/10
- **Factual Consistency:** 91%

## Environmental Impact

- **Hardware Type:** 4x NVIDIA V100 GPUs
- **Hours used:** 96 hours
- **Cloud Provider:** Google Cloud
- **Carbon Emitted:** ~35 kg CO2eq

## Technical Specifications

### Model Architecture
- **Base model:** T5-large
- **Parameters:** 770M
- **Hidden size:** 1024
- **Layers:** 24 encoder, 24 decoder
- **Attention heads:** 16
- **Vocabulary size:** 35,000

### Generation Parameters
```json
{
  "max_length": 512,
  "min_length": 50,
  "temperature": 0.7,
  "top_p": 0.9,
  "num_beams": 4,
  "no_repeat_ngram_size": 3,
  "early_stopping": true
}
```

### Compute Infrastructure
- **Hardware:** NVIDIA V100 GPUs
- **Software:** TensorFlow 2.11, Transformers 4.30

## Example Outputs

### Case Summary Generation
**Input:** `case_type=war_crimes, defendant=General X, location=Syria, evidence=satellite_imagery`

**Output:** "The case concerns war crimes allegedly committed by General X in Syria. Evidence includes satellite imagery showing targeted attacks on civilian infrastructure, which violates international humanitarian law under the Geneva Conventions."

### Investigation Report
**Input:** `incident=mass_displacement, location=Myanmar, victims=Rohingya, timeframe=2017`

**Output:** "Investigation findings reveal systematic mass displacement of Rohingya civilians in Myanmar during 2017. The forced displacement affected thousands of individuals and appears to constitute crimes against humanity under international law."

## Citation

```bibtex
@model{t5_legal_narrative_2024,
  title={T5 Legal Narrative Generation Model},
  author={Lemkin AI Research Team},
  year={2024},
  publisher={GitHub},
  url={https://github.com/LemkinAI/t5-legal-narrative}
}
```

## Model Card Contact
models@lemkinai.org

## Updates
- v1.0 (2024-01): Initial release