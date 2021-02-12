def scan_letter(word: str, letters: str = 'aeiou') -> set:
    """returns a set of letters found in a phrase"""
    return set(letters).intersection(set(word))


def log_request(req: 'flask_request', res: str) -> None:
    with open('vsearch.log', 'a') as log:
        print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')
