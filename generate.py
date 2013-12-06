import argparse

from astgen.ast_gen import ASTCodeGenerator

def generate_ast(input_file, output_file):
    """ Generates the ast for a given config file.

    Arguments:
        input_path:  Path to the config file
        output_path: Path where the generated AST will be stored
    """
    gen = ASTCodeGenerator(input_file)
    gen.generate(output_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generates the ast for a given config file.')
    parser.add_argument('input_file',
                        metavar='I',
                        help='Path to config file.')
    parser.add_argument('output_file',
                        metavar='O',
                        type=argparse.FileType('w'),
                        help='Path to where the generated AST will be stored.')
    args = parser.parse_args()
    generate_ast(args.input_file, args.output_file)
    

    