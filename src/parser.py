def ignore_comment(op_str):
    parts = op_str.split('#')
    return parts[0]


def parse(content):
    lines = content.split('\n')
    operations = []
    for line in lines:
        line = line.strip()
        line = ignore_comment(line)
        ops = line.split(';')
        for op in ops:
            op = op.strip()
            if op != '':
                operations.append(op)
    return operations


