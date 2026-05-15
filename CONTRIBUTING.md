# Contributing to Mimo AI Agent Project

Thank you for your interest in contributing! This document provides guidelines for contributing to the project.

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Git
- Hermes Agent framework
- API keys for data sources (Stockbit, news sites)

### Setup Development Environment

```bash
# Fork and clone the repository
git clone https://github.com/yourusername/mimo-ai-agent-project.git
cd mimo-ai-agent-project

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Install pre-commit hooks
pre-commit install

# Copy environment variables
cp .env.example .env
# Edit .env with your API keys
```

## 📝 Development Workflow

### 1. Create a Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

### 2. Make Changes

- Write clean, readable code
- Follow PEP 8 style guide
- Add docstrings to functions and classes
- Write tests for new features

### 3. Test Your Changes

```bash
# Run tests
pytest tests/

# Run linting
flake8 .
black --check .
mypy .

# Run specific test
pytest tests/test_email_verification.py -v
```

### 4. Commit Changes

```bash
# Stage changes
git add .

# Commit with descriptive message
git commit -m "feat: add email verification agent"
# or
git commit -m "fix: resolve SMTP timeout issue"
```

**Commit Message Format:**
- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation changes
- `test:` Test additions or changes
- `refactor:` Code refactoring
- `style:` Code style changes
- `chore:` Maintenance tasks

### 5. Push and Create Pull Request

```bash
# Push to your fork
git push origin feature/your-feature-name

# Create pull request on GitHub
```

## 🧪 Testing Guidelines

### Writing Tests

```python
# tests/test_email_verification.py
import pytest
from email_verification import EmailVerificationAgent

def test_validate_format():
    agent = EmailVerificationAgent()
    
    # Valid email
    assert agent.validate_format("test@example.com") == True
    
    # Invalid email
    assert agent.validate_format("invalid-email") == False

def test_check_mx_records():
    agent = EmailVerificationAgent()
    
    # Valid domain
    mx_records = agent.check_mx_records("gmail.com")
    assert mx_records is not None
    assert len(mx_records) > 0
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=. --cov-report=html

# Run specific test file
pytest tests/test_email_verification.py

# Run with verbose output
pytest -v
```

## 📚 Code Style

### Python Style Guide

- Follow PEP 8
- Use type hints
- Maximum line length: 88 characters (Black default)
- Use descriptive variable names

**Example:**

```python
from typing import Dict, List, Optional

def analyze_stock(
    ticker: str,
    timeframe: str = "1 week",
    include_news: bool = True
) -> Dict[str, any]:
    """
    Analyze a stock and generate trading setup.
    
    Args:
        ticker: Stock ticker symbol (e.g., "PGAS")
        timeframe: Analysis timeframe (default: "1 week")
        include_news: Whether to include news analysis
    
    Returns:
        dict: Analysis results with trading setup
    
    Raises:
        ValueError: If ticker is invalid
    """
    if not ticker:
        raise ValueError("Ticker cannot be empty")
    
    # Implementation
    pass
```

### Documentation

- Add docstrings to all public functions and classes
- Use Google-style docstrings
- Include examples in docstrings when helpful

## 🐛 Reporting Bugs

### Before Reporting

1. Check existing issues
2. Verify it's reproducible
3. Collect relevant information

### Bug Report Template

```markdown
**Describe the bug**
A clear description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:
1. Run command '...'
2. See error

**Expected behavior**
What you expected to happen.

**Actual behavior**
What actually happened.

**Environment:**
- OS: [e.g., Ubuntu 22.04]
- Python version: [e.g., 3.10.5]
- Hermes Agent version: [e.g., 0.1.0]

**Additional context**
Any other relevant information.
```

## 💡 Feature Requests

### Feature Request Template

```markdown
**Is your feature request related to a problem?**
A clear description of the problem.

**Describe the solution you'd like**
A clear description of what you want to happen.

**Describe alternatives you've considered**
Alternative solutions or features you've considered.

**Additional context**
Any other context or screenshots.
```

## 🔍 Code Review Process

### What We Look For

- ✅ Code quality and readability
- ✅ Test coverage
- ✅ Documentation
- ✅ Performance considerations
- ✅ Security best practices

### Review Timeline

- Initial review: Within 2-3 days
- Follow-up reviews: Within 1-2 days
- Merge: After approval from maintainers

## 📦 Release Process

### Versioning

We use [Semantic Versioning](https://semver.org/):
- MAJOR: Breaking changes
- MINOR: New features (backward compatible)
- PATCH: Bug fixes

### Release Checklist

- [ ] All tests passing
- [ ] Documentation updated
- [ ] CHANGELOG.md updated
- [ ] Version bumped
- [ ] Git tag created

## 🤝 Community Guidelines

### Code of Conduct

- Be respectful and inclusive
- Welcome newcomers
- Provide constructive feedback
- Focus on the code, not the person

### Communication Channels

- GitHub Issues: Bug reports and feature requests
- GitHub Discussions: General questions and ideas
- Pull Requests: Code contributions

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

## 🙏 Thank You!

Your contributions make this project better for everyone. Thank you for taking the time to contribute!

---

**Questions?** Open an issue or start a discussion on GitHub.
