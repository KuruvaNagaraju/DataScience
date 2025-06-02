# 🔐 Prompt Guardrails Classifier: Fine-Tuning DistilBERT on Toxic Comments

## 📘 Overview

This project demonstrates how to **fine-tune a Transformer-based model** (DistilBERT) to classify user prompts as **"safe"** or **"unsafe"**, supporting prompt guardrails for generative AI systems deployed in sensitive environments such as customer support.

The classifier is trained using the **Jigsaw Toxic Comment Classification** dataset and can help screen out harmful or toxic content before the prompt is passed to a generative model.

---

## 🚀 Use Case

The goal is to **enhance safety** in AI systems by:
- Detecting harmful prompts such as hate speech or harassment.
- Flagging them before they reach the language model.
- Classifying text as either:
  - ✅ **Safe**
  - 🚫 **Unsafe**

---

## 🧠 Model Details

| Feature         | Description                          |
|----------------|--------------------------------------|
| Base Model      | `distilbert-base-uncased` (Hugging Face Transformers) |
| Dataset         | [Jigsaw Toxic Comment Classification](https://huggingface.co/datasets/jigsaw_toxicity_pred) |
| Task            | Binary classification: Safe vs Unsafe |
| Fine-tuning Tool | Hugging Face `Trainer` API |
| Hardware        | Compatible with free-tier GPUs (e.g., Google Colab) |

---

## 🧰 Setup Instructions

1. **Clone the repository or open the notebook:**
   ```
   git clone https://github.com/KuruvaNagaraju/DataScience.git
   cd GenAI/toxic_comment_classifier
   ```
   Or upload the provided notebook to [Google Colab](https://colab.research.google.com/).

2. **Install Required Libraries**
   ```bash
   pip install transformers datasets evaluate scikit-learn
   ```

3. **Run the Notebook**
   - Follow the code cells in `finetuning_distilbert_toxic_comment_classification.ipynb`.
   - The notebook handles:
     - Dataset loading and label binarization
     - Tokenization and preprocessing
     - Model fine-tuning using Hugging Face `Trainer`
     - Evaluation and sample predictions

---

## 📊 Evaluation Metrics

The model is evaluated using:
- **Accuracy**
- **Precision**
- **Recall**
- **F1-Score**
- **Confusion Matrix**
- **ROC-AUC**
- **Precision-Recall Curves**

These metrics are visualized for both train and test sets to validate model performance.

---

## 📎 Sample Inference Results

| Prompt | Predicted Label |
|--------|------------------|
| “Thank you for the support.” | ✅ Safe |
| “You're the dumbest person ever.” | 🚫 Unsafe |
| “Let’s work on this issue together.” | ✅ Safe |

---

## 🛠️ Potential Extensions

- ⚙️ **Real-time Screening**: Integrate this classifier into a chatbot pipeline to flag harmful prompts before generation.
- 🧩 **Multi-label Classification**: Extend model to detect types of toxicity (e.g., threat, insult, identity hate).
- 🧪 **Active Learning**: Continually improve performance by retraining on real-world edge cases.

---

## 📌 Key Design Decisions & Trade-offs

- Chose `distilbert-base-uncased` for lightweight performance on Colab GPUs.
- Binary label mapping: Texts with any toxic label were marked as **unsafe**.
- Limited epochs and batch size to avoid GPU memory overflow.

---

## 📖 References

- [Jigsaw Dataset on HuggingFace](https://huggingface.co/datasets/jigsaw_toxicity_pred)
- [Transformers Library by Hugging Face](https://huggingface.co/transformers/)
- [Hugging Face Trainer API Documentation](https://huggingface.co/docs/transformers/main_classes/trainer)

---

## 🧾 Summary

This project demonstrates how to:
- Transform multi-label toxicity data into binary safe/unsafe classification.
- Fine-tune and evaluate a transformer model with minimal resources.
- Build a guardrail to protect LLMs from processing harmful prompts.

---

## 📎 File Structure

```bash
.
├── README.md                                                  # Project overview
├── multilabel_approach                                        # Multilabel classification files
│   ├── finetuning_distilbert_toxic_comment_classification.ipynb  # Main notebook
│   ├── toxic_model.pt                                             # Trained model
│   ├── submission.csv                                             # Test data predictions
├── binary_approach                                            # Binary classification files
│   ├── finetuning_distilbert_toxic_comment_classification.ipynb  # Main notebook
│   ├── fine_tuned_prompt_guardrails_model.pt                     # Fine-tuned model
│   ├── test_predictions.csv                                      # Test data predictions

```

---

## ✍️ Author

- **Nagaraju Kuruva**
- For technical evaluations or use in enterprise safety layers for generative AI systems.
