# Changelog

All notable changes to the Mars Rover Photo Fetcher project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Comprehensive exception handling with custom exception classes
- Centralized API request function with timeout and error handling
- Retry logic for failed API requests
- User-friendly error messages and proper exit codes
- MIT License file
- Requirements.txt with dependencies
- Enhanced documentation with tables and NASA URLs

### Changed
- Improved code documentation with detailed docstrings
- Better variable naming consistency (snake_case)
- Enhanced error handling throughout the codebase
- Updated README.md with comprehensive documentation

### Fixed
- Proper handling of empty API responses
- Network timeout issues
- JSON parsing errors
- Rate limiting error handling

## [1.0.0] - 2024-12-19

### Added
- Initial release of Mars Rover Photo Fetcher
- Support for three Mars rovers: Curiosity, Opportunity, and Spirit
- Random rover selection for each execution
- Earth date and sol-based photo queries
- Fallback mechanism for when no photos are found
- Multiple camera type support
- Simple command-line interface
- NASA Mars Rover API integration

### Features
- **Random Rover Selection**: Automatically selects one of three Mars rovers
- **Smart Date Strategy**: Uses appropriate date ranges for each rover's operational period
- **Fallback Mechanism**: Switches to sol-based queries if earth_date queries return no results
- **Multiple Camera Support**: Supports various camera types used by the rovers
- **Simple Output**: Prints direct image URLs to stdout for easy integration

### Technical Details
- Python 3.7+ compatibility
- Requests library for HTTP API calls
- Random date generation within rover operational periods
- JSON response parsing from NASA API
- Error handling for network and API issues

### Rover Support
- **Curiosity**: Active rover (2012-present), uses recent earth_date queries
- **Opportunity**: Completed mission (2004-2019), uses historical date ranges
- **Spirit**: Completed mission (2004-2010), uses historical date ranges

### API Integration
- NASA Mars Rover API integration
- Support for earth_date and sol-based queries
- Rate limiting awareness
- JSON response handling

## [0.1.0] - 2024-12-19

### Added
- Basic script functionality
- NASA API integration
- Random photo selection
- Support for Curiosity, Opportunity, and Spirit rovers

---

## Version History

### Version 1.0.0 (Current)
- **Major Features**: Complete Mars Rover Photo Fetcher with all three rovers
- **Documentation**: Comprehensive README with NASA resources and tables
- **Error Handling**: Robust exception handling and user-friendly error messages
- **Licensing**: MIT License for open source distribution

### Version 0.1.0 (Initial)
- **Basic Functionality**: Core script with NASA API integration
- **Rover Support**: Support for all three Mars rovers
- **Random Selection**: Random rover and photo selection

---

## Contributing

When contributing to this project, please update the CHANGELOG.md file with your changes following the format above.

### Changelog Format Guidelines

- **Added**: for new features
- **Changed**: for changes in existing functionality
- **Deprecated**: for soon-to-be removed features
- **Removed**: for now removed features
- **Fixed**: for any bug fixes
- **Security**: in case of vulnerabilities

### Version Numbering

This project follows [Semantic Versioning](https://semver.org/):

- **MAJOR** version for incompatible API changes
- **MINOR** version for added functionality in a backwards compatible manner
- **PATCH** version for backwards compatible bug fixes

---

## Future Roadmap

### Planned Features
- [ ] Support for Perseverance rover (when API becomes available)
- [ ] Image download functionality
- [ ] Batch photo retrieval
- [ ] Camera-specific photo filtering
- [ ] GUI interface
- [ ] Photo metadata extraction
- [ ] Local caching of API responses
- [ ] Command-line arguments for rover selection
- [ ] Photo quality/size filtering options

### Potential Improvements
- [ ] Async/await for better performance
- [ ] More comprehensive error recovery
- [ ] Logging system for debugging
- [ ] Configuration file support
- [ ] Unit tests and integration tests
- [ ] Docker containerization
- [ ] CI/CD pipeline setup

---

## Release Notes

### Release 1.0.0
This is the first stable release of the Mars Rover Photo Fetcher. It includes:

- Complete functionality for fetching Mars rover photos
- Support for all three major Mars rovers
- Comprehensive error handling
- Professional documentation
- Open source licensing

The project is now ready for production use and community contributions.

---

*This changelog is maintained by the project maintainers and updated with each release.* 
