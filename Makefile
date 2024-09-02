# ALL
compare_all:
	@python3 runtests.py all

# sudoku
compare_sudoku:
	@python3 runtests.py sudoku

test_sudoku_solution:
	@python3 runtests.py sudoku solution all

test_sudoku_user:
	@python3 runtests.py sudoku user all

# longest common subsequence
compare_longest_common_subsequence:
	@python3 runtests.py longest_common_subsequence

test_longest_common_subsequence_solution:
	@python3 runtests.py longest_common_subsequence solution all

test_longest_common_subsequence_user:
	@python3 runtests.py longest_common_subsequence user all

# k smallest sum pairs
compare_k_smallest_sum_pairs:
	@python3 runtests.py k_smallest_sum_pairs

test_k_smallest_sum_pairs_solution:
	@python3 runtests.py k_smallest_sum_pairs solution all

test_k_smallest_sum_pairs_user:
	@python3 runtests.py k_smallest_sum_pairs user all

# max frequency stack
compare_max_freq_stack:
	@python3 runtests.py max_freq_stack 

test_max_freq_stack_solution:
	@python3 runtests.py max_freq_stack solution all

test_max_freq_stack_user:
	@python3 runtests.py max_freq_stack user all

# n queens
compare_n_queens:
	@python3 runtests.py n_queens

test_n_queens_solution:
	@python3 runtests.py n_queens solution all

test_n_queens_user:
	@python3 runtests.py n_queens user all

# minimum genetic mutation
compare_minimum_genetic_mutation:
	@python3 runtests.py minimum_genetic_mutation

test_minimum_genetic_mutation_solution:
	@python3 runtests.py minimum_genetic_mutation solution all

test_minimum_genetic_mutation_user:
	@python3 runtests.py minimum_genetic_mutation user all

# kSum
compare_kSum:
	@python3 runtests.py kSum

test_kSum_solution:
	@python3 runtests.py kSum solution all

test_kSum_user:
	@python3 runtests.py kSum user all

# snapshot
compare_snapshot:
	@python3 runtests.py snapshot

test_snapshot_solution:
	@python3 runtests.py snapshot solution all

test_snapshot_user:
	@python3 runtests.py snapshot user all