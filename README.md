
# ZERO-SHOT CROSS-LINGUAL POS TAGGING FOR FILIPINO

### Dependencies
If you use Conda environments, you can replicate the exact dependency versions that were used for the experiments:

```bash
conda create -n xpos --file conda-linux-64.lock  # if 64-bit Linux
conda create -n xpos --file conda-osx-arm64.lock  # if Apple Silicon
conda activate xpos
```

### Training
You can then train the models with:

```bash
python src/train.py udpos --learning_rate=5e-5 --eval_steps=1000 --per_device_batch_size=10 --max_steps=1000 --multi
```

### Cross-lingual prediction

Predictions for the best trained models for every target language can be generated with:

```bash
python src/predict.py udpos
```

**Tip:** append `--language_source={lang_code}` or `--language_target={lang_code}` to generate predictions for specific languages.

**Tip:** append `--digest {digest}` to generate predictions for a specific training configuration. The digest is the random string of 8 characters in the output path of each model.

### Cross-lingual results

Export a csv with test accuracies for every source/target combination with:

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
