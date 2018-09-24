import logging
import os
import re
import sys

ERR_NOT_ENOUGH_ARGUMENTS = 0x1
ERR_WRONG_BASE_DIR = ERR_NOT_ENOUGH_ARGUMENTS << 1

INCLUDE_PATTERN = re.compile(r"^#<INCLUDE\s+(.+)\s*$")
FROM_PATTERN = re.compile(r'^FROM\s+<PARENT>')


def usage():
    return '''
    USAGE: python {program} Dockerfile.source [base_dir]
    
    Compiles a Dockerfile.source file to a regular Dockerfile.
    Dockerfile.source features an include command to source other files,
    e.g. 'something.docker':

    #<INCLUDE include/something.docker

    [base_dir] Specifies the root directory containing all scripts and includes.
               (default: '..' -> {base_dir})
    '''.format(program=os.path.basename(__file__), base_dir=os.path.abspath('..'))


def insert_content(include_path, output_file):
    with open(include_path, 'r') as f:
        for line in f:
            output_file.write(line)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger('Docker:Compile')

    if len(sys.argv) < 2:
        logger.error(usage())
        sys.exit(ERR_NOT_ENOUGH_ARGUMENTS)

    source_file = sys.argv[1]

    if len(sys.argv) >= 3:
        base_dir = sys.argv[2]
    else:
        base_dir = '..'

    base_dir = os.path.abspath(base_dir)

    if not os.path.isdir('{}/include'.format(base_dir)):
        logger.error("Could not find 'include' directory in {}.".format(base_dir))
        logger.error(usage())
        sys.exit(ERR_WRONG_BASE_DIR)

    target_file = '{}/Dockerfile'.format(os.path.dirname(os.path.abspath(source_file)))

    with open(target_file, 'w') as fout:
        with open(source_file, 'r') as fin:
            for line in fin:
                match = INCLUDE_PATTERN.match(line)
                if match:
                    include_path = match.group(1)
                    source_file = '{}/{}.docker'.format(base_dir, include_path)
                    if os.path.isfile(source_file):
                        logger.info('Embedding {}'.format(source_file))
                        with open(source_file, 'r') as f:
                            for line2 in f:
                                if FROM_PATTERN.match(line2):
                                    continue
                                fout.write(line2)
                    else:
                        logger.warn('Could not find {}. Skipping.'.format(source_file))
                else:
                    fout.write(line)

    logger.info('Done.')
