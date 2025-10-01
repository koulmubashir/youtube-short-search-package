"""
Basic usage example for YouTube Short Search library.

This example demonstrates how to use the YouTubeShortSearcher class
to search for YouTube shorts and retrieve metadata.
"""

import os
from youtube_short_search import YouTubeShortSearcher, YouTubeSearchError


def main():
    """Main example function."""
    print("YouTube Short Search - Basic Usage Example")
    print("=" * 50)
    
    # Option 1: With API Key (Recommended)
    api_key = os.getenv('YOUTUBE_API_KEY')  # Set this environment variable
    
    if api_key:
        print("\n🔑 Using YouTube Data API (with API key)")
        searcher = YouTubeShortSearcher(api_key=api_key)
    else:
        print("\n🌐 Using web scraping (no API key)")
        searcher = YouTubeShortSearcher()
    
    # Search for shorts
    search_queries = [
        "funny cats",
        "cooking tips",
        "python programming",
        "travel vlogs"
    ]
    
    for query in search_queries:
        print(f"\n📱 Searching for: '{query}'")
        print("-" * 30)
        
        try:
            results = searcher.search_shorts(query, max_results=3)
            
            if results:
                for i, video in enumerate(results, 1):
                    print(f"{i}. {video['title']}")
                    print(f"   👀 Views: {video['views']}")
                    print(f"   📺 Channel: {video['channel']}")
                    print(f"   🔗 URL: {video['url']}")
                    print()
            else:
                print("   No results found.")
                
        except YouTubeSearchError as e:
            print(f"   ❌ Error: {e}")
        
        print()
    
    # Example: Get details for a specific video
    if api_key:
        print("\n🔍 Getting details for a specific video:")
        print("-" * 40)
        
        # Example YouTube short URL (replace with actual URL)
        example_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        
        try:
            details = searcher.get_video_details(example_url)
            print(f"Title: {details['title']}")
            print(f"Views: {details['views']}")
            print(f"Channel: {details['channel']}")
            print(f"Published: {details['published']}")
            print(f"Likes: {details['likes']}")
            print(f"Comments: {details['comments']}")
            
        except YouTubeSearchError as e:
            print(f"❌ Error getting video details: {e}")
    
    print("\n✅ Example completed!")


if __name__ == "__main__":
    main()
