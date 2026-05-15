"""
AI-Driven Stock Trading Analysis Agent

Main entry point for the autonomous agent system.
"""

from hermes_agent import Agent, delegate_task
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class StockAnalysisAgent:
    """Main agent for stock market analysis and content generation."""
    
    def __init__(self):
        self.agent = Agent(
            model=os.getenv("AGENT_MODEL", "claude-sonnet-4"),
            tools=["web_search", "terminal", "file", "browser"]
        )
    
    def analyze_stock(self, ticker: str, timeframe: str = "1 week") -> dict:
        """
        Analyze a stock and generate trading setup.
        
        Args:
            ticker: Stock ticker symbol (e.g., "PGAS")
            timeframe: Analysis timeframe (e.g., "1 week", "1 month")
        
        Returns:
            dict: Analysis results with trading setup
        """
        prompt = f"""
        Analyze {ticker} stock for {timeframe} timeframe:
        
        1. Fetch current price from Stockbit
        2. Scrape latest news from Kompas, CNBC Indonesia, CNN Indonesia
        3. Perform technical analysis (RSI, MACD, support/resistance)
        4. Identify fundamental catalysts
        5. Generate trading setup with:
           - Entry zone (buy price range)
           - Target 1 & 2 (profit targets)
           - Stop loss (risk management)
           - Risk/reward ratio
        6. Save analysis to markdown file
        
        Return comprehensive trading setup.
        """
        
        result = self.agent.run(prompt)
        return result
    
    def generate_content(self, analysis: str, platform: str = "twitter") -> str:
        """
        Generate social media content from analysis.
        
        Args:
            analysis: Trading setup analysis
            platform: Target platform ("twitter", "telegram")
        
        Returns:
            str: Generated content
        """
        prompt = f"""
        Transform this trading analysis into engaging {platform} content:
        
        {analysis}
        
        Requirements:
        - Aggressive/hype tone
        - Use emojis strategically
        - Highlight key catalysts
        - Include clear trading setup
        - Add risk warnings
        - Use Indonesian language
        - Format for {platform} (thread for Twitter, message for Telegram)
        """
        
        content = self.agent.run(prompt)
        return content
    
    def multi_agent_research(self, tickers: list) -> dict:
        """
        Use multiple agents to research stocks in parallel.
        
        Args:
            tickers: List of stock ticker symbols
        
        Returns:
            dict: Aggregated research results
        """
        tasks = [
            {
                "goal": f"Fetch {ticker} price and volume from Stockbit",
                "toolsets": ["web", "terminal"]
            }
            for ticker in tickers
        ]
        
        # Add news research task
        tasks.append({
            "goal": f"Scrape latest news about {', '.join(tickers)} from Indonesian news sites",
            "toolsets": ["web", "browser"]
        })
        
        # Delegate to sub-agents
        results = delegate_task(tasks=tasks)
        
        return results


def main():
    """Main execution function."""
    
    # Initialize agent
    agent = StockAnalysisAgent()
    
    # Example 1: Analyze single stock
    print("🤖 Analyzing PGAS stock...")
    analysis = agent.analyze_stock("PGAS", timeframe="1 week")
    print(f"✅ Analysis complete:\n{analysis}\n")
    
    # Example 2: Generate Twitter content
    print("📱 Generating Twitter thread...")
    twitter_content = agent.generate_content(analysis, platform="twitter")
    print(f"✅ Twitter content:\n{twitter_content}\n")
    
    # Example 3: Multi-agent research
    print("🔍 Running multi-agent research...")
    research = agent.multi_agent_research(["PGAS", "NPGF", "MEDC"])
    print(f"✅ Research complete:\n{research}\n")


if __name__ == "__main__":
    main()
