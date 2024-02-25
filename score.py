from utils import SCORES_FILE_NAME


def add_score(difficulty):
    current_score = get_current_score()
    points = (difficulty * 3) + 5
    if current_score:
        points = points + current_score

    with open(SCORES_FILE_NAME, "w") as f:
        f.write(str(points))


def get_current_score():
    try:
        with open(SCORES_FILE_NAME, 'r') as file:
            return int(file.read().strip())
    except (FileNotFoundError, ValueError):
        return None
