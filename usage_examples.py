#!/usr/bin/env python3
"""
T5 Legal Narrative Generation - Usage Examples
"""

from transformers import T5ForConditionalGeneration, T5Tokenizer
import torch
import json

def load_model():
    """Load the T5 legal narrative model"""
    model_name = "LemkinAI/t5-legal-narrative"

    tokenizer = T5Tokenizer.from_pretrained(model_name)
    model = T5ForConditionalGeneration.from_pretrained(model_name)

    return tokenizer, model

def generate_legal_narrative(prompt, tokenizer, model, max_length=512):
    """Generate legal narrative from structured prompt"""
    # Prepare input with task prefix
    input_text = f"legal_narrative: {prompt}"

    # Tokenize
    input_ids = tokenizer.encode(input_text, return_tensors="pt", max_length=512, truncation=True)

    # Generate
    with torch.no_grad():
        outputs = model.generate(
            input_ids,
            max_length=max_length,
            num_beams=4,
            temperature=0.7,
            do_sample=True,
            early_stopping=True,
            no_repeat_ngram_size=3
        )

    # Decode
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return generated_text

def case_summary_example():
    """Example: Generate case summary"""
    case_data = {
        "case_type": "war_crimes",
        "defendant": "Colonel Ahmed Hassan",
        "charges": ["targeting civilians", "destruction of hospitals"],
        "location": "Syria",
        "dates": "2015-2017",
        "evidence": ["satellite imagery", "witness testimonies", "medical records"],
        "status": "pending trial"
    }

    # Convert to prompt format
    prompt = f"case_type={case_data['case_type']}, defendant={case_data['defendant']}, charges={', '.join(case_data['charges'])}, location={case_data['location']}, evidence={', '.join(case_data['evidence'])}"

    return prompt, case_data

def incident_report_example():
    """Example: Generate incident report"""
    incident_data = {
        "incident_type": "forced_displacement",
        "location": "Myanmar (Rakhine State)",
        "timeframe": "August-September 2017",
        "victims": "Rohingya civilians",
        "perpetrators": "Military forces and local militia",
        "violations": ["deportation", "persecution", "murder", "rape"],
        "displacement_count": "700,000+"
    }

    prompt = f"incident_type={incident_data['incident_type']}, location={incident_data['location']}, victims={incident_data['victims']}, perpetrators={incident_data['perpetrators']}, violations={', '.join(incident_data['violations'])}"

    return prompt, incident_data

def legal_brief_example():
    """Example: Generate legal brief section"""
    brief_data = {
        "document_type": "legal_brief",
        "case": "Prosecutor v. Bemba",
        "legal_issue": "command_responsibility",
        "arguments": [
            "superior knew of crimes",
            "failed to prevent crimes",
            "failed to punish subordinates"
        ],
        "precedents": ["Čelebići case", "Delalić judgment"],
        "legal_framework": "Article 28 Rome Statute"
    }

    prompt = f"document_type={brief_data['document_type']}, legal_issue={brief_data['legal_issue']}, arguments={', '.join(brief_data['arguments'])}, legal_framework={brief_data['legal_framework']}"

    return prompt, brief_data

def investigation_summary_example():
    """Example: Generate investigation summary"""
    investigation_data = {
        "investigation_type": "human_rights_violation",
        "subject": "attacks on healthcare facilities",
        "location": "Yemen",
        "timeframe": "2015-2020",
        "methodology": ["satellite analysis", "witness interviews", "medical records review"],
        "findings": [
            "systematic targeting of hospitals",
            "deliberate destruction of medical infrastructure",
            "pattern of attacks across multiple governorates"
        ],
        "legal_analysis": "violations of Geneva Conventions"
    }

    prompt = f"investigation_type={investigation_data['investigation_type']}, subject={investigation_data['subject']}, location={investigation_data['location']}, methodology={', '.join(investigation_data['methodology'])}, findings={', '.join(investigation_data['findings'])}"

    return prompt, investigation_data

def batch_generation_example(tokenizer, model):
    """Example: Batch process multiple legal documents"""

    # Collect all examples
    examples = [
        case_summary_example(),
        incident_report_example(),
        legal_brief_example(),
        investigation_summary_example()
    ]

    results = []

    for prompt, data in examples:
        print(f"\nGenerating narrative for: {data.get('case_type', data.get('incident_type', data.get('document_type', data.get('investigation_type'))))}")
        print(f"Input prompt: {prompt[:100]}...")

        narrative = generate_legal_narrative(prompt, tokenizer, model)

        results.append({
            'input_data': data,
            'prompt': prompt,
            'generated_narrative': narrative
        })

        print(f"Generated narrative: {narrative[:200]}...")

    return results

def template_based_generation():
    """Example: Using predefined templates"""
    templates = {
        "case_summary": "Generate a case summary for {defendant} charged with {charges} in {location} during {timeframe}",
        "incident_report": "Create an incident report for {incident_type} affecting {victims} in {location} during {timeframe}",
        "legal_analysis": "Analyze the legal implications of {event} under {legal_framework}",
        "investigation_findings": "Summarize investigation findings regarding {subject} in {location} using {methodology}"
    }

    # Example data for templates
    template_data = {
        "case_summary": {
            "defendant": "General Smith",
            "charges": "crimes against humanity",
            "location": "Country X",
            "timeframe": "2018-2020"
        },
        "incident_report": {
            "incident_type": "mass detention",
            "victims": "ethnic minorities",
            "location": "Region Y",
            "timeframe": "March 2021"
        }
    }

    return templates, template_data

def main():
    """Main example demonstration"""
    print("T5 Legal Narrative Generation - Examples")
    print("=" * 50)

    # Load model
    print("Loading model...")
    tokenizer, model = load_model()
    print("Model loaded successfully!")

    # Run batch examples
    print("\n" + "=" * 50)
    print("BATCH GENERATION EXAMPLES")
    print("=" * 50)

    results = batch_generation_example(tokenizer, model)

    # Display detailed results
    print("\n" + "=" * 50)
    print("DETAILED RESULTS")
    print("=" * 50)

    for i, result in enumerate(results, 1):
        print(f"\nExample {i}:")
        print(f"Type: {list(result['input_data'].keys())[0]}")
        print(f"Generated Narrative:")
        print("-" * 30)
        print(result['generated_narrative'])
        print("-" * 30)

    # Template examples
    print("\n" + "=" * 50)
    print("TEMPLATE-BASED GENERATION")
    print("=" * 50)

    templates, template_data = template_based_generation()

    for template_name, template in templates.items():
        if template_name in template_data:
            formatted_template = template.format(**template_data[template_name])
            print(f"\nTemplate: {template_name}")
            print(f"Formatted: {formatted_template}")

if __name__ == "__main__":
    main()