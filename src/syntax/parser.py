
# remove comments from code line
def ignore_comment(op_str):
    parts = op_str.split('#')
    return parts[0]

# parse content of the file to the operations list
def parse(content):
    # split the lines
    lines = content.split('\n')
    operations = []
    for line in lines:
        # clean line, remove comments from that
        line = line.strip()
        line = ignore_comment(line)

        # get operations by spliting line by ;
        ops = line.split(';')
        for op in ops:
            op = op.strip()
            if op != '':
                operations.append(op)
    return operations
