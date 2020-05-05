import Globals


# for SARD style dataset
def find_vulnerable_statements(filename):
    flaw_status = False
    flaw = []
    flaw_description = []
    potential_flaw_status = False
    potential_flaw = []
    fix_status = False
    fix = []
    line_numbers = []
    try:
        with open(filename) as fp:
            count = 0
            for line in fp:
                count += 1
                if flaw_status:
                    flaw.append(line)
                    line_numbers.append(count)
                    flaw_status = False
                elif potential_flaw_status:
                    potential_flaw.append(line)
                    potential_flaw_status = False
                elif fix_status:
                    fix.append(line)
                    fix_status = False
                if "/* POTENTIAL FLAW" in line:
                    potential_flaw_status = True
                elif "/* FLAW" in line:
                    flaw_description.append(line)
                    flaw_status = True
                elif "/* FIX" in line:
                    fix_status = True
    except IOError as e:
        print("CANNOT read this file: ", e)

    return flaw, line_numbers, flaw_description



