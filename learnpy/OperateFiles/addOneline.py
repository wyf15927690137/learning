import os
# with open('pre-check-in-env.txt', 'r') as f:
with open('pre-check-in-env.txt', 'r') as f:
    cases = f.readlines()
for case in cases:
    print(case)
    os.system(f"p4 edit -c 446714 {case}")
    # Open the input file in read mode
    with open(case[:len(case)-1], 'r') as f:
        lines = f.readlines()

    # Insert the new line at the beginning
    new_line = 'export SIGRITY_CONF_FILE_DIR=./qconf\n'
    lines.insert(0, new_line)

    # Open the same file in write mode
    with open(case[:len(case)-1], 'w') as f:
        f.writelines(lines)
