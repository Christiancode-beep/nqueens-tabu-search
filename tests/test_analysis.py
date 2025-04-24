from ..analysis.performance import PerformanceAnalyzer
from ..analysis.comparison import AlgorithmComparator

class TestAnalysis:
    def test_performance_analysis(self):
        results = PerformanceAnalyzer.analyze([4, 8])
        assert 4 in results
        assert 8 in results
        assert 'avg_time' in results[4]
        assert 'success_rate' in results[8]

    def test_algorithm_comparison(self):
        results = AlgorithmComparator.compare([4, 8])
        assert len(results) == 2
        for n, ts_time, bt_time in results:
            assert ts_time > 0
            if n <= 12:
                assert bt_time > 0