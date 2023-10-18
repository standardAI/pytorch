import pathlib
import sys

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
sys.path.append(str(REPO_ROOT))
from tools.stats.import_test_stats import (
    get_td_heuristic_historial_edited_files_json,
    get_td_heuristic_profiling_json,
    get_test_class_ratings,
    get_test_file_ratings,
    get_test_times,
)

TEST_TIMES_FILE = ".pytorch-test-times.json"
TEST_FILE_RATINGS_FILE = ".pytorch-test-file-ratings.json"
TEST_CLASS_RATINGS_FILE = ".pytorch-test-class-ratings.json"
TD_HEURISTIC_PROFILING_FILE = ".pytorch-td-heuristic-profiling.json"
TD_HEURISTIC_HISTORICAL_EDITED_FILES = ".pytorch-td-heuristic-historical-edited-files.json"


def main() -> None:
    print(f"Exporting test times from test-infra to {TEST_TIMES_FILE}")
    get_test_times(str(REPO_ROOT), filename=TEST_TIMES_FILE)
    get_test_file_ratings(str(REPO_ROOT), filename=TEST_FILE_RATINGS_FILE)
    get_test_class_ratings(str(REPO_ROOT), filename=TEST_CLASS_RATINGS_FILE)
    get_td_heuristic_historial_edited_files_json(str(REPO_ROOT), filename=TD_HEURISTIC_HISTORICAL_EDITED_FILES)
    get_td_heuristic_profiling_json(str(REPO_ROOT), filename=TD_HEURISTIC_PROFILING_FILE)


if __name__ == "__main__":
    main()
