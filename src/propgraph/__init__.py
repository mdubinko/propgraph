"""
PropGraph - A general-purpose property graph database library.

PropGraph provides a complete graph database implementation built on SQLite with:
- Nodes and edges with arbitrary properties
- CRUD operations with bulk mutations
- Transaction support with automatic rollback
- Lazy query evaluation with method chaining
- Type-safe operations with comprehensive testing

Example usage:
    from propgraph import PropertyGraph

    with PropertyGraph("my_graph.db") as graph:
        # Create nodes and edges
        user = graph.add_node("User", name="Alice", active=True)
        project = graph.add_node("Project", name="Web App")
        works_on = graph.add_edge(user, "WORKS_ON", project, role="Lead")

        # Query and filter
        active_users = list(graph.nodes("User", active=True))

        # Bulk operations
        deleted_count = graph.nodes("TempUser").delete().execute()
"""

from .core import EdgeProxy, Graph, NodeProxy, PropertyGraph
from .exceptions import (
    DatabaseError,
    EntityNotFoundError,
    IntegrityError,
    InvalidQueryError,
    PropertyNotFoundError,
    PropertyValueError,
    PropGraphError,
    QueryExecutionError,
    TransactionError,
    ValidationError,
)
from .query import EdgeIterator, NodeIterator, QuerySpec, QueryStep
from .logging_utils import SUMMARY, configure_for_tests, get_logger, set_log_level

__version__ = "0.1.0"
__all__ = [
    "PropertyGraph",
    "NodeProxy",
    "EdgeProxy",
    "Graph",
    "QuerySpec",
    "QueryStep",
    "NodeIterator",
    "EdgeIterator",
    "PropGraphError",
    "PropertyNotFoundError",
    "PropertyValueError",
    "EntityNotFoundError",
    "InvalidQueryError",
    "QueryExecutionError",
    "DatabaseError",
    "IntegrityError",
    "TransactionError",
    "ValidationError",
    # Logging utilities
    "SUMMARY",
    "configure_for_tests",
    "get_logger",
    "set_log_level",
]
