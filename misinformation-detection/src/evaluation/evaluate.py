def evaluate_model(model, test_data, test_labels):
    predictions = model.predict(test_data)
    accuracy = accuracy_score(test_labels, predictions)
    precision = precision_score(test_labels, predictions, average='weighted')
    recall = recall_score(test_labels, predictions, average='weighted')
    f1 = f1_score(test_labels, predictions, average='weighted')
    
    metrics = {
        'accuracy': accuracy,
        'precision': precision,
        'recall': recall,
        'f1_score': f1
    }
    
    return metrics

def visualize_metrics(metrics):
    import matplotlib.pyplot as plt
    
    labels = list(metrics.keys())
    values = list(metrics.values())
    
    plt.bar(labels, values)
    plt.ylim(0, 1)
    plt.ylabel('Score')
    plt.title('Model Evaluation Metrics')
    plt.show()

def main():
    # Load your model and data here
    # model = load_model('path_to_model')
    # test_data, test_labels = load_test_data('path_to_test_data')
    
    # metrics = evaluate_model(model, test_data, test_labels)
    # visualize_metrics(metrics)

if __name__ == "__main__":
    main()