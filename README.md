# Overview

The Bug Severity Predictor is a machine learning project aimed at predicting the severity of software bugs based on various features extracted from bug reports. The main approach employed in this project is abstraction( during data cleaning), focusing on generalizable patterns rather than specific domain knowledge.

# Intentions

The primary intention behind this model is to demonstrate the effectiveness of an abstraction approach in predicting bug severity. The model architecture and feature engineering techniques are designed to be adaptable to different software domains, making it a versatile tool for bug severity prediction tasks.

# Limitations

It's essential to note that the current results may not be entirely satisfactory due to the limitations of the dataset. The size of the dataset used for training and evaluation is relatively small, which has impacted the model's performance and generalization capabilities. Therefore, while the model provides valuable insights, its predictions should be interpreted with caution.

# File Structure
source: Contains source files organized with prefixed numbers for ease of reproducing results.

datasets: Contains the datasets used for training and evaluation.

# Usage

1. **Data Preprocessing**: Use the provided datasets for preprocessing bug report data and engineering relevant features.

2. **Model Training**: Utilize the source files prefixed with numbers to train the machine learning models and predict bug severity.

3. **Evaluation**: Evaluate the performance of the trained models using appropriate metrics and visualization techniques.

4. **Integration**: Integrate the trained models into your software development workflow for bug severity prediction tasks.

# Requirements
Python 3.x

NumPy

pandas

scikit-learn

imbalanced-learn

matplotlib

Ray (optional for parallel computing)

# Contributors
Buberwa Jesse

# License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

# Future Work
Larger Dataset: Acquire a larger and more diverse dataset to improve the model's performance and generalization capabilities.

Stronger Model: Explore more advanced machine learning algorithms and techniques to build a more robust bug severity prediction model.

# Related Paper
Title: A Dataset of High Impact Bugs: Manually-Classified Issue Reports

Authors: Masao Ohira, Yutaro Kashiwa, Yosuke Yamatani, Hayato Yoshiyuki, Yoshiya Maeda, Nachai Limsettho, Keisuke Fujino, Hideaki Hata, Akinori Ihara, Kenichi Matsumoto

Year: 2015

# Dataset
The source of the datasets used in this project is mentioned in the paper, but the source is no longer accessible. Therefore, it's advisable to utilize the datasets provided within this project, as they are identical to the ones referenced in the paper.

# Additional Notes
Contributions are welcome! If you have any suggestions, feel free to reach out at joramjesse21900@outlook.com

Some code in this project was AI generated to speed up development and optimization
