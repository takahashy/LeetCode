compare_all:
	@python3 runtests.py all

test_user_all:
	@python3 runtests.py all user all 

test_solution_all:
	@python3 runtests.py all solution all

compare_sudoku:
	@python3 runtests.py sudoku

test_sudoku_solution:
	@python3 runtests.py sudoku solution all

test_sudoku_user:
	@python3 runtests.py sudoku user all

compare_longest_common_subsequence:
	@python3 runtests.py longest_common_subsequence

test_longest_common_subsequence_solution:
	@python3 runtests.py longest_common_subsequence solution all

test_longest_common_subsequence_user:
	@python3 runtests.py longest_common_subsequence user all

compare_k_smallest_sum_pairs:
	@python3 runtests.py k_smallest_sum_pairs

test_k_smallest_sum_pairs_solution:
	@python3 runtests.py k_smallest_sum_pairs solution all

test_k_smallest_sum_pairs_user:
	@python3 runtests.py k_smallest_sum_pairs user all
