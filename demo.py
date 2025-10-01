"""
Demo script for YouTube Short Search library.

This script demonstrates the basic functionality of the library.
"""

from youtube_short_search import YouTubeShortSearcher, YouTubeSearchError


def main():
    """Demo the library functionality."""
    print("🎬 YouTube Short Search Library Demo")
    print("=" * 40)
    
    # Initialize searcher (using web scraping since no API key)
    searcher = YouTubeShortSearcher()
    
    # Demo search
    try:
        print("\n🔍 Searching for 'cooking tips' shorts...")
        results = searcher.search_shorts("cooking tips", max_results=3)
        
        print(f"\n✅ Found {len(results)} results:")
        for i, video in enumerate(results, 1):
            print(f"\n{i}. {video['title']}")
            print(f"   👀 Views: {video['views']}")
            print(f"   🔗 URL: {video['url']}")
            
    except YouTubeSearchError as e:
        print(f"❌ Error: {e}")
    
    print("\n✅ Demo completed!")
    print("\nTo use with YouTube API key:")
    print("searcher = YouTubeShortSearcher(api_key='YOUR_API_KEY')")


if __name__ == "__main__":
    main()
