
# ZERO-SHOT CROSS-LINGUAL POS TAGGING FOR FILIPINO

## Abstract

To effectively train models for NLP tasks like POS tagging, substantial amounts of annotated data are necessary, often demanding intensive resources and incurring high costs. This study investigates the feasibility of employing cross-lingual transfer learning, specifically utilizing zero-shot learning, to mitigate data scarcity issues for the Filipino language. The approach involves assessing effective source language selection as a basis for zero-shot POS tagging. The study demonstrates that its zero-shot implementation outperforms previous studies, with top-performing fine-tuned PLMs achieving significantly higher F1-scores, the highest being 79.10%, compared to prior zero-shot Filipino POS tagging methods. The analysis also reveals moderate correlations between cross-lingual transfer performance and certain linguistic distances, particularly featural, inventory, and syntactic. The primary issue lies in tokenizer optimization, as tokenization with a PLM may fail to align with meaningful representations, resulting in decreased POS tagging performance.

### Dependencies
If you're using Conda environments, you can replicate the exact dependency versions used in the experiments:

```bash
conda create -n xpos --file conda-linux-64.lock  # if 64-bit Linux
conda activate xpos
```

### Training
To train the models, execute the following command:

```bash
python src/train.py udpos --learning_rate=5e-5 --eval_steps=1000 --per_device_batch_size=10 --max_steps=1000 --multi
```

### Cross-lingual prediction

Generate predictions for the best trained models for every target language with:

```bash
python src/predict.py udpos
```

**Tip:** append `--language_source={lang_code}` or `--language_target={lang_code}` to generate predictions for specific languages.

**Tip:** append `--digest {digest}` to generate predictions for a specific training configuration. The digest is the random string of 8 characters in the output path of each model.

### Cross-lingual results

Export a CSV file with test accuracies for every source/target combination:

```bash
python src/results.py udpos -a -e results.csv
```

**Tip:** Just like with training and prediction, you can specify specific languages or a specific digest.

### Models

Export trained models with:

```bash
python src/export.py udpos -e models
```

**Tip:** Just like with training and prediction, you can specify specific languages or a specific digest.
