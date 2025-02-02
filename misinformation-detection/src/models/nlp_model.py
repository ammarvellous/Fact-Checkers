from transformers import BertTokenizer, BertForSequenceClassification
import torch

class NLPModel:
    def __init__(self, model_name='bert-base-uncased', num_labels=2):
        self.tokenizer = BertTokenizer.from_pretrained(model_name)
        self.model = BertForSequenceClassification.from_pretrained(model_name, num_labels=num_labels)

    def encode(self, texts):
        return self.tokenizer(texts, padding=True, truncation=True, return_tensors='pt')

    def predict(self, texts):
        inputs = self.encode(texts)
        with torch.no_grad():
            outputs = self.model(**inputs)
        logits = outputs.logits
        predictions = torch.argmax(logits, dim=-1)
        return predictions

    def train(self, train_dataloader, optimizer, device):
        self.model.train()
        for batch in train_dataloader:
            optimizer.zero_grad()
            inputs = self.encode(batch['texts']).to(device)
            labels = batch['labels'].to(device)
            outputs = self.model(**inputs, labels=labels)
            loss = outputs.loss
            loss.backward()
            optimizer.step()

    def evaluate(self, eval_dataloader, device):
        self.model.eval()
        total_loss = 0
        correct_predictions = 0
        with torch.no_grad():
            for batch in eval_dataloader:
                inputs = self.encode(batch['texts']).to(device)
                labels = batch['labels'].to(device)
                outputs = self.model(**inputs, labels=labels)
                total_loss += outputs.loss.item()
                predictions = torch.argmax(outputs.logits, dim=-1)
                correct_predictions += (predictions == labels).sum().item()
        accuracy = correct_predictions / len(eval_dataloader.dataset)
        return total_loss, accuracy