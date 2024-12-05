# LLaMA-2 QLoRA experiment
<p align="center">
  <img src="https://github.com/longday1102/VietAI-experiment-LLaMA2/assets/121651344/11695528-b3fb-4ea6-814e-7d2a91843cf7" alt="llama-2">
</p>


## I. Introduction
- This project was made by me to refine the LLaMA-2 model based on instructions, applying some techniques to save memory when training such as QLoRA.                                      
- You can run it on Kaggle notebook or Colab notebook.


## II. Dataset
The dataset I used is [MCQ_medical_QA](https://drive.google.com/drive/folders/1o-IOR2tqmhd9lkIW8EEuhqAEUErCPYqS?usp=drive_link), which includes 3 columns: QUESTION, CONTEXT, ANSWER about different types of diseases. Moreover, We propose the corpus of that disease in the scope of Vietnamese. You can watch it in "Notebook/process.ipynb" and the way we collect data in "Notebook/Tam_Anh_Hospital_QA_Crawler.ipynb".


## III. Model
I use model [LLaMA-2 7B](https://huggingface.co/meta-llama/Llama-2-7b-hf) to experiment. If your device has a larger configuration, you can experiment with larger versions of LLaMA-2 such as [LLaMA-2 13B](https://huggingface.co/meta-llama/Llama-2-13b-hf) and [LLaMA-2 70B](https://huggingface.co/meta-llama/Llama-2-70b-hf).


## IV. How to use
First, `!git clone` this repo, then install the environment with the command `!pip install --upgrade -r requirements.txt`. To do Train, Inference and Demo you can use the script in my [notebook](https://github.com/ThanhCong19/Chatbot_Medical/tree/dev/Notebook). 

## Acknowledgements
Thanks [VietAI-experiment-LLaMA2](https://github.com/longday1102/VietAI-experiment-LLaMA2) for the base codes.



      
