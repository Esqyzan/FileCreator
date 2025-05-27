# Document Management System

A simple console-based document management system with status tracking and automatic data persistence.

## Features

- ✅ Create and manage documents
- ✅ Track document statuses (Draft → Under Review → Approved/Rejected)
- ✅ Automatic JSON file persistence
- ✅ Filter documents by status and author
- ✅ Edit document content
- ✅ Delete documents
- ✅ Search documents by title and content
- ✅ Document statistics
- ✅ Export documents to text file
- ✅ UTF-8 support for international characters

## Requirements

- Python 3.6 or higher
- Standard Python libraries (datetime, json, os)

## Installation and Usage

1. Download the `document_manager.py` file
2. Open terminal in the file directory
3. Run the program:

```bash
python document_manager.py
```

## Usage Guide

### Main Menu

After launching the program, you'll see the main menu with these options:

```
=============================================
1.  Add Document
2.  View All Documents
3.  Filter Documents
4.  Advance to Next Status
5.  Revert to Previous Status
6.  Edit Document
7.  Delete Document
8.  Search Documents
9.  Statistics
10. Export Documents
11. Exit
=============================================
```

### Document Statuses

Documents progress through the following statuses:

1. **Draft** - Initial status for new documents
2. **Under Review** - Document submitted for review
3. **Approved** - Document has been approved
4. **Rejected** - Document has been rejected

### Core Functions

#### 1. Add Document

- Enter document title
- Add content
- Specify author
- Document automatically gets "Draft" status

#### 2. View All Documents

Displays all documents with information:
- Document ID
- Title
- Author
- Current status
- Creation and last update timestamps

#### 3. Filter Documents

Filter documents by:
- **Status** - Choose from available statuses
- **Author** - Enter author name (case-insensitive search)

#### 4. Status Management

- **Advance Status**: Move document to next approval level
- **Revert Status**: Return document to previous status

#### 5. Edit Document

- Select document by ID
- View current content
- Enter new content

#### 6. Delete Document

- Select document by ID
- Confirm deletion

#### 7. Search Documents

- Search by title or content
- Case-insensitive search
- Displays all matching documents

#### 8. Statistics

Shows:
- Total number of documents
- Distribution by status
- Distribution by author

#### 9. Export Documents

- Export all documents to a text file
- Choose custom filename or use auto-generated name
- Includes all document metadata and content

## Data Storage

All data is automatically saved to `documents.json` in the same directory as the program. Data is automatically loaded on next startup.

### Data Format

```json
[
  {
    "id": 1,
    "title": "Document Title",
    "content": "Document content",
    "author": "Author Name",
    "status": 0,
    "created_at": "2025-05-27T09:01:05.123456",
    "updated_at": "2025-05-27T09:01:05.123456"
  }
]
```

## Usage Examples

### Creating a Document

```
Choose action (1-11): 1

=== Add New Document ===
Enter document title: Technical Specification
Enter document content: System requirements and architecture
Enter author name: John Doe

Document successfully added.
```

### Viewing Documents

```
=== Document List ===
[ID: 1] Technical Specification | Author: John Doe | Status: Draft | 
Created: 2025-05-27 09:01 | Updated: 2025-05-27 09:01
```

### Status Progression

```
Enter document ID to advance to next status: 1
Status updated to: Under Review
```

### Search Example

```
Enter search term: technical
=== Search Results for 'technical' ===
[ID: 1] Technical Specification | Author: John Doe | Status: Under Review |
Created: 2025-05-27 09:01 | Updated: 2025-05-27 09:05
```

## Troubleshooting

### Save/Load Errors

- Ensure the program has write permissions in the current directory
- Check that `documents.json` is not open in another program

### Encoding Issues

- The program uses UTF-8 for proper international character support
- Ensure your terminal supports UTF-8 encoding

### Common Issues

1. **"Document not found"** - Check that you're entering the correct document ID
2. **"Invalid input"** - Ensure you're entering numbers when prompted for IDs
3. **Empty title/author** - These fields cannot be empty

## Development

### Code Structure

- `Document` - Class representing a document
- `save_documents()` / `load_documents()` - Data persistence functions
- Individual functions for each menu option
- `main()` - Main program loop

### Possible Enhancements

- Document categories/tags
- Comment system
- User roles and permissions
- Web interface
- Database integration
- Version history
- Document templates
- Notification system
- Multi-language support

## File Structure

```
project_directory/
├── document_manager.py    # Main program file
├── documents.json        # Data storage (auto-created)
├── README.md            # This file
└── exported_files/      # Directory for exports (auto-created)
```

## API Reference

### Document Class Methods

- `next_status()` - Advance to next status
- `prev_status()` - Revert to previous status
- `edit_content(new_content)` - Update document content
- `to_dict()` - Convert to dictionary for JSON serialization
- `from_dict(data)` - Create instance from dictionary

### Main Functions

- `add_document()` - Create new document
- `list_documents()` - Display all documents
- `filter_documents()` - Filter by status/author
- `search_documents()` - Search by title/content
- `show_statistics()` - Display statistics
- `export_documents()` - Export to text file

## Version History

### v1.0.0 (2025-05-27)
- Initial release
- Basic document management
- Status tracking
- JSON persistence
- Search and filter functionality
- Export capability

## License

This software is provided free of charge for any purpose.

## Contributing

Feel free to submit issues, feature requests, or pull requests to improve this document management system.

## Author

Created as a demonstration of Python programming and document workflow management.
