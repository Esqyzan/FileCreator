import datetime
import json
import os

# Predefined statuses
STATUSES = ["Draft", "Under Review", "Approved", "Rejected"]

# Data file name
DATA_FILE = "documents.json"

# Document storage
documents = []

class Document:
    def __init__(self, title, content, author, doc_id=None):
        self.id = doc_id if doc_id else len(documents) + 1
        self.title = title
        self.content = content
        self.author = author
        self.status = 0  # status index
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

    def next_status(self):
        """Advances document to the next status"""
        if self.status < len(STATUSES) - 1:
            self.status += 1
            self.updated_at = datetime.datetime.now()
            return True
        return False

    def prev_status(self):
        """Reverts document to the previous status"""
        if self.status > 0:
            self.status -= 1
            self.updated_at = datetime.datetime.now()
            return True
        return False

    def edit_content(self, new_content):
        """Edits document content"""
        self.content = new_content
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """Converts object to dictionary for saving"""
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'author': self.author,
            'status': self.status,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

    @classmethod
    def from_dict(cls, data):
        """Creates object from dictionary"""
        doc = cls(data['title'], data['content'], data['author'], data['id'])
        doc.status = data['status']
        doc.created_at = datetime.datetime.fromisoformat(data['created_at'])
        doc.updated_at = datetime.datetime.fromisoformat(data['updated_at'])
        return doc

    def __str__(self):
        return (f"[ID: {self.id}] {self.title} | Author: {self.author} | "
                f"Status: {STATUSES[self.status]} | "
                f"Created: {self.created_at.strftime('%Y-%m-%d %H:%M')} | "
                f"Updated: {self.updated_at.strftime('%Y-%m-%d %H:%M')}")

def save_documents():
    """Saves documents to file"""
    try:
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump([doc.to_dict() for doc in documents], f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        print(f"Error saving documents: {e}")
        return False

def load_documents():
    """Loads documents from file"""
    global documents
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
                documents = [Document.from_dict(doc_data) for doc_data in data]
            print(f"Loaded {len(documents)} documents.")
        except Exception as e:
            print(f"Error loading documents: {e}")
            documents = []
    else:
        documents = []

def add_document():
    """Adds a new document"""
    print("=== Add New Document ===")
    title = input("Enter document title: ").strip()
    if not title:
        print("Document title cannot be empty.\n")
        return
    
    content = input("Enter document content: ").strip()
    author = input("Enter author name: ").strip()
    if not author:
        print("Author name cannot be empty.\n")
        return
    
    # Generate new ID
    max_id = max([doc.id for doc in documents], default=0)
    doc = Document(title, content, author, max_id + 1)
    documents.append(doc)
    
    if save_documents():
        print("Document successfully added.\n")
    else:
        print("Document added, but failed to save to file.\n")

def list_documents():
    """Displays list of all documents"""
    if not documents:
        print("No documents yet.\n")
        return
    
    print("=== Document List ===")
    for doc in documents:
        print(doc)
    print()

def filter_documents():
    """Filters documents by status or author"""
    if not documents:
        print("No documents yet.\n")
        return
    
    print("Filter by:")
    print("1. Status")
    print("2. Author")
    choice = input("Choose option (1-2): ").strip()
    
    if choice == "1":
        print("Available statuses:")
        for i, status in enumerate(STATUSES):
            print(f"{i + 1}. {status}")
        
        try:
            status_choice = int(input("Select status (number): ")) - 1
            if 0 <= status_choice < len(STATUSES):
                filtered_docs = [doc for doc in documents if doc.status == status_choice]
                if filtered_docs:
                    print(f"\n=== Documents with status '{STATUSES[status_choice]}' ===")
                    for doc in filtered_docs:
                        print(doc)
                else:
                    print(f"No documents with status '{STATUSES[status_choice]}' found.")
            else:
                print("Invalid status number.")
        except ValueError:
            print("Invalid input.")
    
    elif choice == "2":
        author = input("Enter author name: ").strip()
        filtered_docs = [doc for doc in documents if author.lower() in doc.author.lower()]
        if filtered_docs:
            print(f"\n=== Documents by author '{author}' ===")
            for doc in filtered_docs:
                print(doc)
        else:
            print(f"No documents by author '{author}' found.")
    else:
        print("Invalid choice.")
    print()

def advance_status():
    """Advances document to next status"""
    if not documents:
        print("No documents yet.\n")
        return
    
    list_documents()
    try:
        doc_id = int(input("Enter document ID to advance to next status: "))
        doc = next((d for d in documents if d.id == doc_id), None)
        if doc:
            if doc.next_status():
                print(f"Status updated to: {STATUSES[doc.status]}")
                save_documents()
            else:
                print("Document is already at final status.")
        else:
            print("Document not found.")
    except ValueError:
        print("Invalid input.")
    print()

def retreat_status():
    """Reverts document to previous status"""
    if not documents:
        print("No documents yet.\n")
        return
    
    list_documents()
    try:
        doc_id = int(input("Enter document ID to revert to previous status: "))
        doc = next((d for d in documents if d.id == doc_id), None)
        if doc:
            if doc.prev_status():
                print(f"Status changed to: {STATUSES[doc.status]}")
                save_documents()
            else:
                print("Document is already at initial status.")
        else:
            print("Document not found.")
    except ValueError:
        print("Invalid input.")
    print()

def edit_document():
    """Edits document content"""
    if not documents:
        print("No documents yet.\n")
        return
    
    list_documents()
    try:
        doc_id = int(input("Enter document ID to edit: "))
        doc = next((d for d in documents if d.id == doc_id), None)
        if doc:
            print(f"Current content:\n{doc.content}\n")
            new_content = input("Enter new content: ").strip()
            doc.edit_content(new_content)
            print("Document content updated.")
            save_documents()
        else:
            print("Document not found.")
    except ValueError:
        print("Invalid input.")
    print()

def delete_document():
    """Deletes a document"""
    if not documents:
        print("No documents yet.\n")
        return
    
    list_documents()
    try:
        doc_id = int(input("Enter document ID to delete: "))
        doc = next((d for d in documents if d.id == doc_id), None)
        if doc:
            confirm = input(f"Are you sure you want to delete document '{doc.title}'? (yes/no): ").strip().lower()
            if confirm in ['yes', 'y']:
                documents.remove(doc)
                print("Document deleted.")
                save_documents()
            else:
                print("Deletion cancelled.")
        else:
            print("Document not found.")
    except ValueError:
        print("Invalid input.")
    print()

def show_statistics():
    """Shows document statistics"""
    if not documents:
        print("No documents yet.\n")
        return
    
    print("=== Statistics ===")
    print(f"Total documents: {len(documents)}")
    
    # Status statistics
    status_counts = {}
    for doc in documents:
        status = STATUSES[doc.status]
        status_counts[status] = status_counts.get(status, 0) + 1
    
    print("\nDistribution by status:")
    for status, count in status_counts.items():
        print(f"  {status}: {count}")
    
    # Author statistics
    author_counts = {}
    for doc in documents:
        author_counts[doc.author] = author_counts.get(doc.author, 0) + 1
    
    print("\nDistribution by author:")
    for author, count in sorted(author_counts.items()):
        print(f"  {author}: {count}")
    print()

def search_documents():
    """Searches documents by title or content"""
    if not documents:
        print("No documents yet.\n")
        return
    
    search_term = input("Enter search term: ").strip().lower()
    if not search_term:
        print("Search term cannot be empty.\n")
        return
    
    found_docs = []
    for doc in documents:
        if (search_term in doc.title.lower() or 
            search_term in doc.content.lower()):
            found_docs.append(doc)
    
    if found_docs:
        print(f"\n=== Search Results for '{search_term}' ===")
        for doc in found_docs:
            print(doc)
    else:
        print(f"No documents found containing '{search_term}'.")
    print()

def export_documents():
    """Exports documents to a text file"""
    if not documents:
        print("No documents to export.\n")
        return
    
    filename = input("Enter export filename (without extension): ").strip()
    if not filename:
        filename = f"documents_export_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}"
    
    filename += ".txt"
    
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("DOCUMENT EXPORT\n")
            f.write("=" * 50 + "\n\n")
            
            for doc in documents:
                f.write(f"ID: {doc.id}\n")
                f.write(f"Title: {doc.title}\n")
                f.write(f"Author: {doc.author}\n")
                f.write(f"Status: {STATUSES[doc.status]}\n")
                f.write(f"Created: {doc.created_at.strftime('%Y-%m-%d %H:%M')}\n")
                f.write(f"Updated: {doc.updated_at.strftime('%Y-%m-%d %H:%M')}\n")
                f.write(f"Content:\n{doc.content}\n")
                f.write("-" * 50 + "\n\n")
        
        print(f"Documents exported to '{filename}'.")
    except Exception as e:
        print(f"Error exporting documents: {e}")
    print()

def main():
    """Main program function"""
    print("=== Document Management System ===")
    load_documents()
    
    while True:
        print("=" * 45)
        print("1.  Add Document")
        print("2.  View All Documents")
        print("3.  Filter Documents")
        print("4.  Advance to Next Status")
        print("5.  Revert to Previous Status")
        print("6.  Edit Document")
        print("7.  Delete Document")
        print("8.  Search Documents")
        print("9.  Statistics")
        print("10. Export Documents")
        print("11. Exit")
        print("=" * 45)
        
        choice = input("Choose action (1-11): ").strip()
        print()

        if choice == "1":
            add_document()
        elif choice == "2":
            list_documents()
        elif choice == "3":
            filter_documents()
        elif choice == "4":
            advance_status()
        elif choice == "5":
            retreat_status()
        elif choice == "6":
            edit_document()
        elif choice == "7":
            delete_document()
        elif choice == "8":
            search_documents()
        elif choice == "9":
            show_statistics()
        elif choice == "10":
            export_documents()
        elif choice == "11":
            print("Goodbye! Thank you for using Document Management System.")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()