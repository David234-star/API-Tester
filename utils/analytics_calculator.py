# Neon-API-Tester/utils/analytics_calculator.py

from collections import Counter


class AnalyticsCalculator:
    """Processes raw analytics data to compute statistics."""

    def __init__(self, analytics_data):
        self.data = analytics_data

    def get_endpoints(self):
        """Returns a list of all unique endpoints."""
        return list(self.data.keys())

    def get_summary_stats(self):
        """Calculates statistics across all requests to all endpoints."""
        all_requests = [req for endpoint_data in self.data.values()
                        for req in endpoint_data]
        if not all_requests:
            return self._get_empty_stats()
        return self._calculate_stats_for_requests(all_requests)

    def get_stats_for_endpoint(self, endpoint_key):
        """Calculates statistics for a specific endpoint."""
        requests = self.data.get(endpoint_key, [])
        if not requests:
            return self._get_empty_stats()
        return self._calculate_stats_for_requests(requests)

    def _calculate_stats_for_requests(self, requests):
        """Helper function to run calculations on a list of request data."""
        response_times = [r['response_time_ms'] for r in requests]
        response_sizes = [r['response_size_bytes'] for r in requests]
        status_codes = [r['status_code'] for r in requests]

        stats = {
            "total_requests": len(requests),
            "avg_time": sum(response_times) / len(response_times) if response_times else 0,
            "min_time": min(response_times) if response_times else 0,
            "max_time": max(response_times) if response_times else 0,
            "avg_size": sum(response_sizes) / len(response_sizes) if response_sizes else 0,
            "status_code_distribution": dict(Counter(status_codes)),
        }
        return stats

    def _get_empty_stats(self):
        """Returns a default dictionary for when there is no data."""
        return {
            "total_requests": 0, "avg_time": 0, "min_time": 0, "max_time": 0,
            "avg_size": 0, "status_code_distribution": {}
        }
