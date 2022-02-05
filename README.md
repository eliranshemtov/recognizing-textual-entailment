# recognizing-textual-entailment

**Master degree's NLP Course Project - Recognizing Textual Entailment (RTE):**
**By:** [Yehuda Yadid](https://www.linkedin.com/in/yehuda-yadid/) and [Eliran Shem Tov](https://www.linkedin.com/in/eliranshemtov/)
### Full project report could be found [Here](https://github.com/eliranshemtov/recognizing-textual-entailment/blob/main/project-report.pdf).
*****
## Abstract
As part of our Master's Natural Language Processing (NLP) course, we were instructed to use the knowledge we’ve gained and create a software that will recognize textual entailment (sometimes referred as Inference) and based on the Stanford Natural Language Inference (SNLI) corpus. <br>
Recognizing Textual Entailment **(RTE)** is a relatively advanced task that aims to classify directional relation between texts.<br>

There are two flavors of the problem: 2-way and 3-way classification.

#### Definitions
- For Text T’ and Hypothesis H’, we’ll say that:<br>
   - 3-way classification:
     - T' entails H' if humans reading of T' will infer that H' is most likely true.
     - T' contradicts if humans reading of T' will infer that H' is most likely false.
     - T' neutral if humans reading of T' will infer that H' is most undetermined. - 
   - 2-way classification:
     - T' entails H' if humans reading of T' will infer that H' is most likely true.
     - T' doesn't entail H' if humans reading of T' will infer that H' is most likely false.

## The Data
Our RTE task is based on the [SNLI corpus](https://nlp.stanford.edu/projects/snli/) (v1.0) which is a large collection of 570K English sentence pairs that were labeled manually with the labels: [entailment, contradiction, neutral].
The best classification results for RTE with the SNLI corpus were achieved by [Pilault et al. ('20)](https://arxiv.org/pdf/2009.09139.pdf) with their CA-MTL model (92.1% accuracy). <br>
Every instance in the corpus is composed of premise (T'), hypothesis (H') and label. In fact, there are some other attributes for every instance, but we’ll use “sentence1”, “sentence2” and “gold_label” solely.


## Our Solution
During our work we went through a lot of ideas. Some better, some less, few got implemented and others were dropped in theory phase.<br>
Eventually the purposed solution we came with is to use the BERT model that we mentioned in class and retrained it on our corpus for fine-tuning and adjustments to excel the RTE task. <br>
We used Facebook’s open source PyTorch framework and hugging-face transformers library and implemented the solution in a JuPyter notebook. We initially played around with the free Kaggle’s NVidia K80 GPU kernel. When we got to the real action part of training the model twice (3-way and 2-way classifications) we switched to a paid Google Cloud N1-Standard-4 instance with NVIDIA Tesla T4x1 GPU. <br><br>
The model was pre-trained ahead and already holds word embedding for language modeling and prediction tasks for which the model was trained for. However, our task is not one of the pre-training tasks and therefore we are required to adjust the model parameters for our needs. To achieve the desired fine-tuning of the model weights and parameters, we need to preprocess the RTE task specific dataset and train the model on it.

## Results
### Accuracy & Timing
Re-training the model on our processed SNLI corpus took 3 hours for each epoch (~9 total) and achieved 0.89% accuracy for the 3-way classification, and 91% accuracy for the 2-way task (with similar timing).

### Error Analysis
Full error analysis could be found [in the project report](https://github.com/eliranshemtov/recognizing-textual-entailment/blob/main/project-report.pdf).



# Execution Instructions
### Online
- The entire project is available in [our GitHub repository](https://github.com/eliranshemtov/recognizing-textual-entailment).
- To view every step’s results, you can explore the [JuPyter notebook here](https://github.com/eliranshemtov/recognizing-textual-entailment/blob/main/notebook.ipynb).
- You may also run and play with the [notebook in Kaggle](https://www.kaggle.com/eliranshemtov/rte-snli-nlp).

### Offline
- You may also clone the repository and run the notebook.
- Note that our re-trained BERT model and the encoding pickles are available for download from the repository’s [releases section](https://github.com/eliranshemtov/recognizing-textual-entailment/releases), so you can download and use them instead of re-encoding and training. All you need to do is to download the data pickles & the models, and place them in `./data` and `./models` respectively.


****
© [Yehuda Yadid](https://www.linkedin.com/in/yehuda-yadid/) and [Eliran Shem Tov](https://www.linkedin.com/in/eliranshemtov/) | MTA | Feb-22 <br>
This is an educational course project, not for production.