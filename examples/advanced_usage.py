"""
Advanced usage example for YouTube Short Search library.

This example demonstrates error handling, batch processing,
and advanced features of the library.
"""

import os
import json
import time
from typing import List, Dict
from youtube_short_search import (
    YouTubeShortSearcher,
    YouTubeSearchError,
    InvalidSearchQueryError,
    APIKeyError,
    NetworkError,
    NoResultsFoundError
)


class AdvancedSearchManager:
    """Advanced search manager with error handling and batch processing."""
    
    def __init__(self, api_key: str = None):
        """Initialize the search manager."""
        self.searcher = YouTubeShortSearcher(api_key=api_key)
        self.search_history = []
    
    def batch_search(self, queries: List[str], max_results: int = 5) -> Dict[str, List[Dict]]:
        """
        Perform batch search for multiple queries.
        
        Args:
            queries: List of search queries
            max_results: Maximum results per query
            
        Returns:
            Dictionary with query as key and results as value
        """
        results = {}
        
        for query in queries:
            print(f"🔍 Searching for: '{query}'")
            
            try:
                search_results = self.searcher.search_shorts(query, max_results=max_results)
                results[query] = search_results
                self.search_history.append({
                    'query': query,
                    'timestamp': time.time(),
                    'results_count': len(search_results),
                    'status': 'success'
                })
                
                print(f"   ✅ Found {len(search_results)} results")
                
                # Add delay to respect rate limits
                time.sleep(1)
                
            except InvalidSearchQueryError as e:
                print(f"   ❌ Invalid query: {e}")
                results[query] = []
                self.search_history.append({
                    'query': query,
                    'timestamp': time.time(),
                    'status': 'invalid_query',
                    'error': str(e)
                })
                
            except APIKeyError as e:
                print(f"   ❌ API key error: {e}")
                results[query] = []
                self.search_history.append({
                    'query': query,
                    'timestamp': time.time(),
                    'status': 'api_error',
                    'error': str(e)
                })
                
            except NetworkError as e:
                print(f"   ❌ Network error: {e}")
                results[query] = []
                self.search_history.append({
                    'query': query,
                    'timestamp': time.time(),
                    'status': 'network_error',
                    'error': str(e)
                })
                
            except NoResultsFoundError as e:
                print(f"   ⚠️  No results found: {e}")
                results[query] = []
                self.search_history.append({
                    'query': query,
                    'timestamp': time.time(),
                    'status': 'no_results',
                    'error': str(e)
                })
                
            except YouTubeSearchError as e:
                print(f"   ❌ General error: {e}")
                results[query] = []
                self.search_history.append({
                    'query': query,
                    'timestamp': time.time(),
                    'status': 'general_error',
                    'error': str(e)
                })
        
        return results
    
    def filter_results(self, results: List[Dict], min_views: int = 1000) -> List[Dict]:
        """
        Filter results based on minimum view count.
        
        Args:
            results: List of video results
            min_views: Minimum view count threshold
            
        Returns:
            Filtered list of results
        """
        filtered = []
        
        for video in results:
            view_text = video.get('views', '0 views')
            
            # Extract numeric value from view count
            try:
                if 'M' in view_text:
                    view_count = float(view_text.split('M')[0]) * 1_000_000
                elif 'K' in view_text:
                    view_count = float(view_text.split('K')[0]) * 1_000
                else:
                    view_count = float(view_text.split(' ')[0])
                
                if view_count >= min_views:
                    filtered.append(video)
                    
            except (ValueError, IndexError):
                # If we can't parse the view count, include the video
                filtered.append(video)
        
        return filtered
    
    def save_results(self, results: Dict[str, List[Dict]], filename: str = "search_results.json"):
        """Save search results to a JSON file."""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(results, f, indent=2, ensure_ascii=False)
            print(f"💾 Results saved to {filename}")
        except Exception as e:
            print(f"❌ Error saving results: {e}")
    
    def get_search_statistics(self) -> Dict:
        """Get statistics about search history."""
        if not self.search_history:
            return {}
        
        total_searches = len(self.search_history)
        successful_searches = len([s for s in self.search_history if s['status'] == 'success'])
        total_results = sum(s.get('results_count', 0) for s in self.search_history if s['status'] == 'success')
        
        status_counts = {}
        for search in self.search_history:
            status = search['status']
            status_counts[status] = status_counts.get(status, 0) + 1
        
        return {
            'total_searches': total_searches,
            'successful_searches': successful_searches,
            'success_rate': (successful_searches / total_searches) * 100 if total_searches > 0 else 0,
            'total_results_found': total_results,
            'average_results_per_search': total_results / successful_searches if successful_searches > 0 else 0,
            'status_breakdown': status_counts
        }


def main():
    """Main advanced example function."""
    print("YouTube Short Search - Advanced Usage Example")
    print("=" * 55)
    
    # Initialize the advanced search manager
    api_key = os.getenv('YOUTUBE_API_KEY')
    manager = AdvancedSearchManager(api_key=api_key)
    
    # Define search queries
    search_queries = [
        "python tutorial",
        "cooking recipes",
        "travel destinations",
        "fitness workout",
        "invalid query with special chars !@#$%",
        "music covers",
        "art tutorials"
    ]
    
    print(f"\n🚀 Starting batch search for {len(search_queries)} queries...")
    print("=" * 55)
    
    # Perform batch search
    all_results = manager.batch_search(search_queries, max_results=3)
    
    # Display results summary
    print("\n📊 Search Results Summary:")
    print("-" * 30)
    
    for query, results in all_results.items():
        if results:
            print(f"✅ '{query}': {len(results)} results")
            
            # Show top result
            top_result = results[0]
            print(f"   🏆 Top result: {top_result['title'][:50]}...")
            print(f"   👀 Views: {top_result['views']}")
        else:
            print(f"❌ '{query}': No results")
    
    # Filter results by view count
    print("\n🔽 Filtering results (min 10K views):")
    print("-" * 40)
    
    for query, results in all_results.items():
        if results:
            filtered = manager.filter_results(results, min_views=10000)
            if filtered:
                print(f"✅ '{query}': {len(filtered)}/{len(results)} videos meet criteria")
                for video in filtered:
                    print(f"   📱 {video['title'][:40]}... ({video['views']})")
            else:
                print(f"⚠️  '{query}': No videos meet view criteria")
    
    # Save results to file
    print("\n💾 Saving results...")
    manager.save_results(all_results, "youtube_shorts_results.json")
    
    # Display search statistics
    print("\n📈 Search Statistics:")
    print("-" * 25)
    
    stats = manager.get_search_statistics()
    if stats:
        print(f"Total searches: {stats['total_searches']}")
        print(f"Successful searches: {stats['successful_searches']}")
        print(f"Success rate: {stats['success_rate']:.1f}%")
        print(f"Total results found: {stats['total_results_found']}")
        print(f"Average results per search: {stats['average_results_per_search']:.1f}")
        
        print("\nStatus breakdown:")
        for status, count in stats['status_breakdown'].items():
            print(f"  {status}: {count}")
    
    print("\n✅ Advanced example completed!")


if __name__ == "__main__":
    main()
