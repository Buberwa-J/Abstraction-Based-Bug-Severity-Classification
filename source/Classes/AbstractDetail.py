import regex as re
import contractions
from source.configurations import text_column_to_use as column_to_check


def display_rows_with(sample_df, pattern):
    text_column = sample_df[column_to_check]
    regex = re.compile(pattern)
    for string in text_column:
        if regex.search(string):
            print(string)


def display_tokens_with(sample_df, pattern):
    text_column = sample_df[column_to_check]
    regex = re.compile(pattern)
    tokens = text_column.str.split()
    for token_list in tokens:
        for token in token_list:
            if regex.search(token):
                print(token)


class AbstractDetail:
    def __init__(self, pattern, abstraction_mapping):

        """
        Initializes the AbstractDetail object.

        Args:
            pattern (Pattern): An instance of Pattern containing predefined regex patterns.
            abstraction_mapping (AbstractionMapping): An instance of AbstractionMapping containing mappings for abstractions.
        """

        self.pattern = pattern
        self.abstraction_mapping = abstraction_mapping

    def abstract_text(self, dataframe, column_to_abstract):

        """
        Abstracts text in the specified column of the dataframe based on patterns and mappings.

        Args:
            dataframe (DataFrame): The dataframe containing text data.
            column_to_abstract (str): The name of the column to abstract.
        """

        # Remove contractions from the column
        dataframe[column_to_abstract] = self.remove_contractions(dataframe, column_to_abstract)

        abstraction_order = [
            ('components_patterns', 'all_components'),
            ('exception_patterns', 'all_exceptions'),
            ('config_file_patterns', 'all_config_files'),
            ('version_number_patterns', 'all_versions'),
            ('class_patterns', 'all_classes'),
            ('source_file_patterns', 'all_source_files'),
            ('method_patterns', 'all_methods'),
            ('error_patterns', 'all_errors'),
            ('sql_class_patterns', 'all_sql_classes'),
            ('sql_source_file_patterns', 'all_sql_source_files'),
            ('java_class_patterns', 'all_java_classes'),
            ('variable_patterns', 'all_variables'),
            ('digit_patterns', 'all_digits'),
        ]

        # Iterate over the abstraction order
        for pattern_attr, mapping_attr in abstraction_order:
            patterns = getattr(self.pattern, pattern_attr)
            mapping = getattr(self.abstraction_mapping, mapping_attr)
            if pattern_attr == 'components_patterns':
                self.apply_pattern_mapping_case_insensitive(dataframe, column_to_abstract, patterns, mapping)
            else:
                self.apply_pattern_mapping(dataframe, column_to_abstract, patterns, mapping)

        # Remove special characters
        special_char_pattern = r'[^A-Za-z0-9\s]'
        dataframe[column_to_abstract] = dataframe[column_to_abstract].apply(
            lambda x: re.sub(special_char_pattern, '', x))

        """
        Explanation:
        After removing special characters, the text may change and patterns that were not matched previously due to the presence of special characters might now be matched.
        Therefore, we perform abstraction again to ensure that all relevant patterns are applied to the text.
        """

        for pattern_attr, mapping_attr in abstraction_order:
            patterns = getattr(self.pattern, pattern_attr)
            mapping = getattr(self.abstraction_mapping, mapping_attr)
            if pattern_attr == 'components_patterns':
                self.apply_pattern_mapping_case_insensitive(dataframe, column_to_abstract, patterns, mapping)
            else:
                self.apply_pattern_mapping(dataframe, column_to_abstract, patterns, mapping)

    """
    These Methods Abstract text in the specified column of the dataframe based on patterns and mappings.

    Args:
        dataframe (DataFrame): The dataframe containing text data.
        column_to_abstract (str): The name of the column to abstract.
        patterns (list): The list of patterns to consider
        mapping (str): The term that will be used to replace the specific terms

    Explanation:
    The dataset may contain text where the patterns to be matched for abstraction may appear in various cases(lower or upper).
    To ensure that all instances of the patterns are captured for abstraction, we provide two methods for abstraction:
    - The `apply_pattern_mapping` method tokenizes the text column and replaces matched tokens with mappings, considering case sensitivity.
    - The `apply_pattern_mapping_case_insensitive` method tokenizes the text column and replaces matched tokens with mappings in a case-insensitive manner - This is convenient for the component abstraction.
    By providing both methods, we aim to cover all possible cases of pattern appearance for effective abstraction.
    """

    @staticmethod
    def apply_pattern_mapping(dataframe, column_to_abstract, patterns, mapping):
        # Tokenize the column and replace matched tokens with mapping
        for pattern in patterns:
            dataframe[column_to_abstract] = dataframe[column_to_abstract].apply(
                lambda x: ' '.join([mapping if re.search(pattern, token) else token for token in x.split()]))

    @staticmethod
    def apply_pattern_mapping_case_insensitive(dataframe, column_to_abstract, patterns, mapping):

        # Tokenize the column and replace matched tokens case-insensitively with mapping
        for pattern in patterns:
            dataframe[column_to_abstract] = dataframe[column_to_abstract].apply(
                lambda x: ' '.join(
                    [mapping if re.search(pattern, token.lower()) else token for token in
                     x.split()]))

    @staticmethod
    def remove_contractions(dataframe, column_to_abstract):
        # Return the column with contractions removed
        return dataframe[column_to_abstract].apply(contractions.fix)
