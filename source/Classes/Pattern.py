class Pattern:

    """
    A class to store predefined regex patterns for abstraction.

    Attributes:
        error_patterns (list): List of regex patterns for errors.
        variable_patterns (list): List of regex patterns for variables.
        exception_patterns (list): List of regex patterns for exceptions.
        components_patterns (list): List of strings representing components.
        class_patterns (list): List of regex patterns for classes.
        config_file_patterns (list): List of regex patterns for configuration files.
        source_file_patterns (list): List of regex patterns for source files.
        version_number_patterns (list): List of regex patterns for version numbers.
        digit_patterns (list): List of regex patterns for digits.
        method_patterns (list): List of regex patterns for methods.
        sql_class_patterns (list): List of regex patterns for SQL classes.
        sql_source_file_patterns (list): List of regex patterns for SQL source files.
        java_class_patterns (list): List of regex patterns for Java classes.
    """

    def __init__(self):
        self.error_patterns = [
            r'\w(?:error|Error|ERROR)'
        ]
        self.variable_patterns = [
            r'[a-z]\.[a-z]',
            r'[A-Za-z]_[A-Za-z]',
            r'\.[A-Z]+',
            r'_\w'
        ]
        self.exception_patterns = [
            r'Exception|NPE'
        ]
        self.components_patterns = [
            'ambari',
            'camel',
            'derby',
            'wicket'
        ]

        self.class_patterns = [
            r'^[A-Z]+[a-z]*[A-Z][a-z]+\w+$',
            r'^[A-Z]+[a-z]*[A-Z][a-z]+\.'
        ]
        self.config_file_patterns = [
            '.conf',
            '.cfg',
            '.ini',
            '.yaml',
            '.yml',
            '.json',
            '.xml',
            '.properties',
            '.toml',
            '.cnf',
        ]
        self.source_file_patterns = [
            '.java',
            '.php',
            '.js',
            '.html',
            '.ksh',
            '.sh',
            'htm',  # only one instance of this. So remove during production
            '.py',
            '.jar'
        ]
        self.version_number_patterns = [
            r'\b\d+(?:\.\d+){1,3}(?:-\w+)?(?:\.\d+)?\b',
            r'\d\.[a-z0-9A-Z]+'
        ]
        self.digit_patterns = [
            r'\s\d\s',
            r'\d'
        ]
        self.method_patterns = [
            r'^[a-z]+[A-Z][a-zA-Z]+$',
            r'\w\(.*\)',
            r'^[a-z]+[A-Z]',
            r'\.[a-z]+[A-Z]',
            r'\.[a-z]+\(',
            r'#'
        ]
        self.sql_class_patterns = [
            r'java\.sql'
        ]
        self.sql_source_file_patterns = [
            r'\.sql$'
        ]
        self.java_class_patterns = [
            r'java\.'
        ]
