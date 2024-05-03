class AbstractionMapping:
    """
    A class to define mappings for different abstractions.

    Attributes:
        all_components (str): Mapping for all components.
        all_exceptions (str): Mapping for all exceptions.
        all_classes (str): Mapping for all classes.
        all_methods (str): Mapping for all methods.
        all_config_files (str): Mapping for all configuration files.
        all_source_files (str): Mapping for all source files.
        all_versions (str): Mapping for all version numbers.
        all_variables (str): Mapping for all variables.
        all_digits (str): Mapping for all digits.
        all_sql_classes (str): Mapping for all SQL classes.
        all_sql_source_files (str): Mapping for all SQL source files.
        all_java_classes (str): Mapping for all Java classes.
        all_errors (str): Mapping for all errors.
    """
    def __init__(self):
        self.all_components = 'COMPONENT'
        self.all_exceptions = 'EXCEPTION'
        self.all_classes = 'CLASS'
        self.all_methods = 'METHOD'
        self.all_config_files = 'CONFIGURATION FILE'
        self.all_source_files = 'SOURCE FILE'
        self.all_versions = 'VERSION NUMBER'
        self.all_variables = 'VARIABLE'
        self.all_digits = 'NUMBER'
        self.all_sql_classes = 'CLASS'
        self.all_sql_source_files = 'SOURCE FILE'
        self.all_java_classes = 'CLASS'
        self.all_errors = 'ERROR'
