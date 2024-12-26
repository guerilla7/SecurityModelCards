# 🪪 SecurityModelCards
“Security Model Cards” for Reporting the Security Posture of Internally Developed Machine Learning Models or Systems

👨🏻‍💻 Author: Ron F. Del Rosario  
📧 E-mail: ronsurf23@gmail.com    
🛜 LinkedIn: www.linkedin.com/in/ronaldfloresdelrosario

🚀 This concept was initially published as public comment via Request for Information (RFI) Related to NIST’s Assignments Under
Sections 4.1, 4.5, and 11 of the Executive Order Concerning Artificial Intelligence (Sections 4.1, 4.5, and 11):
https://www.regulations.gov/comment/NIST-2023-0009-0105

📖 The Security Model Cards concept is also featured in the recently published book (July 26, 2024) "Adversarial AI Attacks, Mitigations, and Defense Strategies: A Cybersecurity Professional's Guide to AI Attacks, Threat Modeling, and Securing AI with MLSecOps" By John Sotiropoulos.  Book is available for purchase in Amazon: https://a.co/d/2LVNvXC

🐍 Proof-of-Concept (POC) Python implementation added.  It's always a great idea to express your vision, and strategy into Pythonic code that others can build on and expand.  

**SecModelCardBuilder.py** - An interactive Python script for uploading a PDF file or manually generating each section of the Model Card via manual inputs.  This can be improved and automated.  
<img width="951" alt="Screenshot 2024-12-26 at 11 23 57 AM" src="https://github.com/user-attachments/assets/4e73358e-a6a5-48e8-8eb5-b0432c1fa3df" />

**SecModelCardPreDefined.py** - A Python script that you can edit and provide the inputs manually for each section of the Model Card, and run to generate in JSON format.  A good quick and dirty approach if you want to copy+paste Model Card data and simply generate the Model Card report as part of a build.  This can be improved and automated.  
<img width="1030" alt="Screenshot 2024-12-26 at 11 24 40 AM" src="https://github.com/user-attachments/assets/67a5e54b-fdc9-4fc4-bc97-e066dd62ab6b" />  

**Sample Report**
```
{
    "model_details": {
        "developer": "Acme AI Inc.",
        "date": "2023-12-26",
        "version": "1.0.0",
        "type": "Image Classification",
        "information": "Trained using a ResNet50 architecture with cross-entropy loss and data augmentation.",
        "resource": "https://www.acmeai.com/image-classifier-paper",
        "citation": "Acme AI Inc. (2023). Image Classification with ResNet50. Journal of AI Research.",
        "license": "MIT License",
        "contact": "research@acmeai.com"
    },
    "intended_use": {
        "primary_uses": "Classifying images into predefined categories.",
        "primary_users": "AI developers, researchers, and image processing applications.",
        "out_of_scope_uses": "Medical diagnosis, facial recognition, or any security-sensitive applications."
    },
    "factors": {
        "relevant_factors": "Image quality, object size, lighting conditions.",
        "evaluation_factors": "Accuracy, precision, recall, F1-score."
    },
    "metrics": {
        "performance_measures": "Accuracy: 95%, Precision: 92%, Recall: 90%, F1-score: 91%",
        "decision_thresholds": "Confidence score > 0.8 for classification.",
        "variation_approaches": "Tested with different image resolutions and noise levels."
    },
    "evaluation_data": {
        "datasets": "ImageNet, CIFAR-10",
        "motivation": "Standard benchmark datasets for image classification.",
        "preprocessing": "Resizing, normalization, and data augmentation."
    },
    "training_data": "Proprietary dataset of 1 million images with balanced class distribution.",
    "quantitative_analyses": {
        "unitary_results": "Detailed breakdown of performance metrics per class.",
        "intersectional_results": "Analysis of performance across different image characteristics."
    },
    "ethical_considerations": "Potential biases in the training data have been mitigated through careful dataset selection and augmentation.",
    "caveats_and_recommendations": "The model may not generalize well to unseen image categories. Further testing is recommended for specific use cases.",
    "security_considerations": {
        "threat_modeling": "Potential adversarial attacks have been considered and mitigated through input validation and adversarial training.",
        "security_testing": "Penetration testing and vulnerability scanning have been performed to ensure the model's security."
    }
}
```

 

> [!NOTE]
> I am using a customized and more advanced version of this Security Model Cards concept at my current work where I serve as the Chief Security Architect, focusing on AI/ML Systems.
> The use of Security Model Cards in large organizations helps promote visibility, transparency, and understanding of ML Models and AI Systems in general within product security organizations.    

> [!TIP]
> Product security teams often struggle when it comes to conducting security reviews and threat modeling of ML Models or AI Systems due to a lack of foundational knowledge about the system that
> they need to review.  This is where Model Cards shine, and can easily be repurposed to include a security considerations section that will benefit both AI/ML developers and security teams.
