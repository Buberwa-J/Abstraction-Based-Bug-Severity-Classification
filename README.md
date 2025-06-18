# Abstraction-Based Bug Severity Classification

## Project Overview

**Abstraction-Based Bug Severity Classification** is a research-oriented machine learning project designed to predict the severity of software bugs from textual bug reports. The project’s distinguishing feature is its use of *abstraction*—systematic replacement of domain-specific terms and patterns with generalized tokens—enabling the model to focus on structural and semantic patterns rather than overfitting to project-specific vocabulary. This approach aims to improve generalizability and facilitate cross-domain research in software engineering.

## Technical Highlights

- **Data Abstraction Pipeline**: Implements a multi-stage pipeline for data preparation, including:
  - **Trimming**: Selects relevant columns and removes incomplete entries from multiple open-source bug datasets.
  - **Preliminary Encoding**: Encodes categorical variables (e.g., bug type, priority) into numerical representations for ML compatibility.
  - **Merging**: Combines datasets from different projects to create a unified corpus.
  - **Text Abstraction**: Uses custom regex-based pattern classes to replace project-specific entities (e.g., class names, file paths, version numbers, error types) with abstract tokens (e.g., `CLASS`, `SOURCE FILE`, `ERROR`).
    
    ```python
    # Example: Abstracting class names and error types in bug summaries
    from Classes.AbstractDetail import AbstractDetail
    from Classes.Pattern import Pattern
    from Classes.AbstractionMapping import AbstractionMapping
    
    abstractor = AbstractDetail(pattern=Pattern(), abstraction_mapping=AbstractionMapping())
    abstractor.abstract_text(df, 'summary')  # df is your DataFrame
    ```
    This replaces project-specific entities (like class names, file paths, error types) with general tokens (e.g., `CLASS`, `ERROR`).
  - **Cleaning**: Further processes text to remove noise, contractions, and special characters.
  - **Feature Engineering**: Extracts word frequencies and sentiment scores; supports extensible feature addition.
  - **Vectorization**: Provides both TF-IDF and spaCy-based vector representations for textual features.

- **Modeling**: Utilizes a Random Forest classifier, with support for imbalanced data handling (SMOTE), and modular code for easy experimentation with other algorithms.

- **Reproducibility**: Each pipeline stage is encapsulated in a dedicated, well-documented script, allowing researchers to reproduce, modify, or extend any part of the workflow.

- **Extensibility**: The abstraction and feature engineering modules are designed for easy adaptation to new domains or additional abstraction patterns.

## Intended Audience & Research Usage

This project is primarily intended for researchers and practitioners in software engineering, natural language processing, and applied machine learning. It is ideal for:
- Experimenting with abstraction techniques in text-based classification tasks
- Benchmarking the impact of abstraction on model generalizability
- Prototyping new feature engineering or vectorization strategies
- Educational purposes in advanced data science or software analytics courses

**Note:** Due to the limited size and scope of the included datasets, this project is not intended for production deployment. Results should be interpreted as exploratory and hypothesis-generating.

## File Structure

- `source/`: Modular Python scripts for each pipeline stage, named with numeric prefixes for sequential execution.
  - `Classes/`: Core abstraction, pattern, and mapping classes
  - `Feature Engineering/`: Scripts for extracting word frequencies and sentiment scores
  - `Models/`: Machine learning model training and evaluation
  - `Vectorizing Text/`: Scripts for text vectorization
- `datasets/`: Organized subfolders for each stage of data processing (original, trimmed, encoded, merged, abstracted, cleaned, feature engineered, vectorized)

## Usage

1. **Data Preprocessing**: Run the scripts in `source/` sequentially to trim, encode, merge, abstract, and clean the datasets.
2. **Feature Engineering**: Use scripts in `Feature Engineering/` to generate additional features.
3. **Vectorization**: Apply vectorization scripts to prepare data for modeling.
4. **Model Training & Evaluation**: Train and evaluate models using scripts in `Models/`.
5. **Experimentation**: Modify abstraction patterns, feature engineering, or modeling scripts to explore new research questions.

## Requirements
- Python 3.x
- numpy
- pandas
- scikit-learn
- imbalanced-learn
- matplotlib
- spaCy
- Ray (optional, for parallel processing)

## Limitations
- **Dataset Size**: The included datasets are small and may not support robust generalization.
- **Research Focus**: The pipeline is optimized for experimentation and demonstration, not for production use.

## Contributors
- Buberwa Jesse

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Future Work
- **Larger Datasets**: Integrate more diverse and extensive datasets to improve model robustness.
- **Advanced Modeling**: Explore deep learning and transfer learning approaches.
- **Automated Pattern Discovery**: Research methods for automatic abstraction pattern generation.

## Related Work
- **Paper**: *A Dataset of High Impact Bugs: Manually-Classified Issue Reports*  
  Masao Ohira, Yutaro Kashiwa, Yosuke Yamatani, Hayato Yoshiyuki, Yoshiya Maeda, Nachai Limsettho, Keisuke Fujino, Hideaki Hata, Akinori Ihara, Kenichi Matsumoto (2015)

---

## Motivation and Thought Process

### Why Abstraction?
The core motivation for this project was to address a common challenge in software analytics: models that perform well on one project often fail to generalize to others. This is largely due to the presence of project-specific vocabulary, identifiers, and patterns in bug reports. My goal was to design a pipeline that could "see through" these specifics and focus on the underlying structure and semantics of bug descriptions. By abstracting away details like class names, file paths, and version numbers, the model is encouraged to learn patterns that are more likely to transfer across projects and domains.

### Inspiration
The abstraction approach was inspired by the way experienced developers and triagers mentally filter out irrelevant details to focus on the essence of a bug. I wanted to encode this intuition into a reproducible, systematic process that could be studied, benchmarked, and improved upon by the research community.

## Pipeline Walkthrough & Design Insights

- **Trimming and Encoding**: Early pipeline stages are simple and transparent, ensuring that only relevant, high-quality data is passed downstream. Encoding categorical variables at this stage also makes the pipeline modular and extensible.

- **Abstraction Engine**: The abstraction logic is implemented using custom classes (`Pattern`, `AbstractionMapping`, `AbstractDetail`). Patterns are defined using regular expressions, and mappings are easily extensible. The abstraction is performed in two passes: before and after special character removal, ensuring maximum coverage. Both case-sensitive and case-insensitive matching are supported for flexibility.

- **Cleaning**: Making use of spaCy and a custom stop word list, the cleaning step standardizes text and removes noise, further improving the quality of downstream features.

- **Feature Engineering**: Word frequency and sentiment features are engineered to capture both the content and the emotional tone of bug reports. The design allows for easy addition of new features, supporting further research.

    ```python
    def calculate_word_frequencies(summary):
        words = summary.lower().split()
        return words.count('error') / len(words)  # Example: frequency of 'error'
    
    # Apply to DataFrame
    word_freq = df['summary'].apply(calculate_word_frequencies)
    ```
    This demonstrates how the pipeline quantifies the presence of abstracted tokens in each bug report.

- **Vectorization**: Both TF-IDF and spaCy vectorizations are provided, for comparing traditional and neural embedding approaches. The code is modular, so new vectorization methods can be plugged in with minimal changes.

- **Modeling**: Random Forest was used for its interpretability and robustness on small datasets. The pipeline, however, is agnostic to the model and can be extended to deep learning or other advanced methods.

    ```python
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.model_selection import train_test_split
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    accuracy = model.score(X_test, y_test)
    print(f"Test Accuracy: {accuracy:.2f}")
    ```
    This is a simplified version of the modeling step, showing the use of a Random Forest for classification.

## Design Philosophy & Research Vision

- **Transparency**: Every step is explicit and documented, making the pipeline easy to audit, reproduce, and extend.
- **Modularity**: Each stage is encapsulated in its own script or class, allowing researchers to swap components in and out.
- **Extensibility**: New abstraction patterns, features, or models can be added with minimal disruption to the workflow.
- **Research-First**: The project is designed as a sandbox for experimentation, not as a black-box solution.

## Technical Notes & Tips for Researchers

- **Custom Patterns**: To add new abstraction patterns, simply extend the `Pattern` and `AbstractionMapping` classes.
- **Feature Engineering**: The feature engineering scripts are templates—feel free to add linguistic, structural, or metadata-based features.
- **Vectorization**: Try combining multiple vectorization strategies for richer representations.
- **Modeling**: The pipeline is compatible with any scikit-learn compatible model. For deep learning, export features and use in PyTorch or TensorFlow.
- **Reproducibility**: All scripts are designed to be run independently or as part of a larger workflow. Intermediate datasets are saved at each stage for inspection.

## Challenges and Lessons Learned

- **Data Scarcity**: Working with small datasets highlighted the importance of robust preprocessing and the limitations of complex models in low-data regimes.
- **Pattern Coverage**: Designing abstraction patterns that are both general and effective required iterative refinement and manual inspection of the data.
- **Balancing Generalization and Specificity**: Too much abstraction can remove useful signal; too little can lead to overfitting. The current design reflects a balance, but further research is encouraged.

## Acknowledgements

This project builds on the work of the software analytics and NLP research communities. Special thanks to the authors of the referenced dataset and to the maintainers of the open-source tools used throughout the pipeline.

---

