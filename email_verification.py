"""
Email Verification Agent

Stealth email validation without triggering alerts.
"""

import re
import socket
import smtplib
from typing import Dict, Optional


class EmailVerificationAgent:
    """Agent for validating email addresses without detection."""
    
    def __init__(self):
        self.timeout = 10
    
    def validate_format(self, email: str) -> bool:
        """
        Validate email format using regex.
        
        Args:
            email: Email address to validate
        
        Returns:
            bool: True if format is valid
        """
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    def check_mx_records(self, domain: str) -> Optional[list]:
        """
        Check MX records for domain.
        
        Args:
            domain: Domain to check
        
        Returns:
            list: MX records if found, None otherwise
        """
        try:
            import dns.resolver
            mx_records = dns.resolver.resolve(domain, 'MX')
            return [str(record.exchange) for record in mx_records]
        except Exception as e:
            print(f"MX lookup failed: {e}")
            return None
    
    def verify_smtp(self, email: str) -> Dict[str, any]:
        """
        Verify email via SMTP without sending.
        
        Args:
            email: Email address to verify
        
        Returns:
            dict: Verification results
        """
        domain = email.split('@')[1]
        mx_records = self.check_mx_records(domain)
        
        if not mx_records:
            return {
                "valid": False,
                "reason": "No MX records found"
            }
        
        try:
            # Connect to SMTP server
            server = smtplib.SMTP(timeout=self.timeout)
            server.set_debuglevel(0)
            server.connect(mx_records[0])
            server.helo(server.local_hostname)
            server.mail('test@example.com')
            code, message = server.rcpt(email)
            server.quit()
            
            if code == 250:
                return {
                    "valid": True,
                    "mailbox_exists": True,
                    "mx_server": mx_records[0]
                }
            else:
                return {
                    "valid": False,
                    "reason": f"SMTP code {code}: {message.decode()}"
                }
        
        except Exception as e:
            return {
                "valid": False,
                "reason": f"SMTP verification failed: {str(e)}"
            }
    
    def full_verification(self, email: str) -> Dict[str, any]:
        """
        Perform complete email verification.
        
        Args:
            email: Email address to verify
        
        Returns:
            dict: Complete verification results
        """
        results = {
            "email": email,
            "format_valid": False,
            "domain_active": False,
            "mx_records": None,
            "mailbox_exists": None,
            "provider": None
        }
        
        # Step 1: Format validation
        results["format_valid"] = self.validate_format(email)
        if not results["format_valid"]:
            return results
        
        # Step 2: Extract domain and provider
        domain = email.split('@')[1]
        results["provider"] = self._detect_provider(domain)
        
        # Step 3: MX records
        mx_records = self.check_mx_records(domain)
        if mx_records:
            results["domain_active"] = True
            results["mx_records"] = mx_records
        
        # Step 4: SMTP verification (optional, can trigger alerts)
        # Uncomment if needed:
        # smtp_result = self.verify_smtp(email)
        # results["mailbox_exists"] = smtp_result.get("mailbox_exists")
        
        return results
    
    def _detect_provider(self, domain: str) -> str:
        """Detect email provider from domain."""
        providers = {
            "gmail.com": "Google Gmail",
            "yahoo.com": "Yahoo Mail",
            "hotmail.com": "Microsoft Hotmail",
            "outlook.com": "Microsoft Outlook",
            "hotmail.co.uk": "Microsoft Hotmail UK",
            "icloud.com": "Apple iCloud",
            "protonmail.com": "ProtonMail"
        }
        return providers.get(domain, f"Unknown ({domain})")


def main():
    """Example usage."""
    agent = EmailVerificationAgent()
    
    # Test email
    email = "nickbrown05@hotmail.co.uk"
    
    print(f"🔍 Verifying email: {email}\n")
    
    results = agent.full_verification(email)
    
    print("📊 Verification Results:")
    print(f"  Email: {results['email']}")
    print(f"  Format Valid: {'✅' if results['format_valid'] else '❌'}")
    print(f"  Domain Active: {'✅' if results['domain_active'] else '❌'}")
    print(f"  Provider: {results['provider']}")
    print(f"  MX Records: {results['mx_records']}")
    print(f"  Mailbox Exists: {results['mailbox_exists'] or 'Not checked (stealth mode)'}")


if __name__ == "__main__":
    main()
