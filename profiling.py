import cProfile
import pstats

from pstats import SortKey

from great_expectations import DataContext

target_directory = "/tmp/blarg/great_expectations"
# context = DataContext.create(target_directory)
context = DataContext(target_directory)
# context.add_datasource(
#     name="test2",
#     type_="pandas",
#     base_directory="/ge_data/"
# )

cProfile.run('context.profile_datasource(\
    "test2",\
    dry_run=False\
)', 'profile_stats_auto')
# profiling_results = context.profile_datasource(
#     "test2",
#     dry_run=False
# )
p = pstats.Stats('profile_stats_auto')
p.sort_stats(SortKey.CUMULATIVE).print_stats(100)

