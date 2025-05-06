def deserialize(s):
    s = s.strip()
    idx = 0

    def parse():
        nonlocal idx

        def skip_whitespace():
            while idx < len(s) and s[idx].isspace():
                idx += 1

        def parse_null():
            nonlocal idx
            if s[idx:idx+4] == "null":
                idx += 4
                return None

        def parse_bool():
            nonlocal idx
            if s[idx:idx+4] == "true":
                idx += 4
                return True
            elif s[idx:idx+5] == "false":
                idx += 5
                return False

        def parse_number():
            nonlocal idx
            start = idx
            while idx < len(s) and (s[idx].isdigit() or s[idx] in '-+.eE'):
                idx += 1
            return int(s[start:idx]) if '.' not in s[start:idx] else float(s[start:idx])

        def parse_string():
            nonlocal idx
            assert s[idx] == '"'
            idx += 1
            start = idx
            while idx < len(s) and s[idx] != '"':
                idx += 1
            result = s[start:idx]
            idx += 1  # skip ending quote
            return result

        def parse_list():
            nonlocal idx
            idx += 1  # skip '['
            result = []
            while True:
                skip_whitespace()
                if s[idx] == ']':
                    idx += 1
                    break
                item = parse()
                result.append(item)
                skip_whitespace()
                if s[idx] == ',':
                    idx += 1
                elif s[idx] == ']':
                    idx += 1
                    break
            return result

        def parse_dict():
            nonlocal idx
            idx += 1  # skip '{'
            result = {}
            while True:
                skip_whitespace()
                if s[idx] == '}':
                    idx += 1
                    break
                key = parse()
                skip_whitespace()
                assert s[idx] == ':'
                idx += 1
                skip_whitespace()
                value = parse()
                result[key] = value
                skip_whitespace()
                if s[idx] == ',':
                    idx += 1
                elif s[idx] == '}':
                    idx += 1
                    break
            return result

        skip_whitespace()
        if idx >= len(s):
            return None
        if s[idx] == '"':
            return parse_string()
        elif s[idx].isdigit() or s[idx] == '-':
            return parse_number()
        elif s[idx] == 'n':
            return parse_null()
        elif s[idx] == 't' or s[idx] == 'f':
            return parse_bool()
        elif s[idx] == '[':
            return parse_list()
        elif s[idx] == '{':
            return parse_dict()
        else:
            raise ValueError(f"Unexpected char: {s[idx]} at pos {idx}")

    return parse()
