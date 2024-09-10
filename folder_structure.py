import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

# Add nodes
G.add_node("Document-Structure-Tool")

G.add_node("backend/")
G.add_node("app/")
G.add_node("main.py")
G.add_node("services/")
G.add_node("__init__.py")
G.add_node("extract_text.py")
G.add_node("utils/")

G.add_node("models/")
G.add_node("__init__.py")

G.add_node("tests/")
G.add_node("test_extract.py")
G.add_node("test_detect_sections.py")
G.add_node("test_summarize.py")

G.add_node("requirements.txt")

G.add_node("frontend/")




# Add edges
G.add_edges_from([("Document-Structure-Tool","backend/"),
                    ("backend/","app/"),
                        ("app/","main.py"),
                        ("app/","services/"),
                            ("services/","__init__.py"),
                            ("services/","extract_text.py"),
                            ("services/","utils/"),
                        ("app/","models/"),
                            ("models/","__init__.py"),
                    ("backend/","tests/"),
                        ("tests/","test_extract.py"),
                        ("tests/","test_detect_sections.py"),
                        ("tests/","text_summarize.py"),
                    ("backend/","requirements.txt"),
                ("Document-Structure-Tool","frontend/")])

nx.draw(G,with_labels = True)
plt.show()