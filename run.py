from train import Trainer

trainer = Trainer(
    model_name="bkai-foundation-models/vietnamese-llama2-7b-40GB",
    dataset_name="NTCong/medical_qa_vn",
    num_epochs=10,
    batch_size=1,
    use_4bit=True,
    use_peft=True,
)

trainer.train()