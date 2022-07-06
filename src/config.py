import transformers

DEVICE = "cuda"
MAX_LEN = 64
TRAIN_BATCH_SIZE = 8
VALID_BATCH_SIZE = 4
EPOCHS = 10
BERT_PATH = "/home/nikunj18/workspace/bert_base_multilingual_uncased/"
MODEL_PATH = "model.bin"
TOKENIZER = transformers.BertTokenizer.from_pretrained(BERT_PATH, do_lower_case=True)