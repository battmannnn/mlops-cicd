
from src.model import train_model

if __name__ == "__main__":
    accuracy = train_model()
    print("ML Application Started Successfully")
    print(f"Model Accuracy: {accuracy:.4f}")
