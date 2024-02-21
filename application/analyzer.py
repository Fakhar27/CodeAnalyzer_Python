import subprocess
import json

def analyze_code(file_path):
    # Create a subprocess to run pyan3 with the Python file
    process = subprocess.Popen(
        ["pyan3", "--dot", file_path],  # Pass the file path as an argument
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    stdout, stderr = process.communicate()

    # Check for any errors
    if process.returncode != 0:
        raise Exception(f"Error analyzing code: {stderr}")

    # Parse the output as JSON
    analysis_data = json.loads(stdout)

    # Process the analysis data
    total_loops = analysis_data['Loops']['total']
    nested_loops = analysis_data['Loops']['nested']
    if_else_statements = analysis_data['Decisions']

    return total_loops, nested_loops, if_else_statements











# import subprocess
# import json

# def analyze_code(file_paths):
#     # Create a subprocess to run pyan3 with the file paths
#     process = subprocess.Popen(
#         ["pyan3"] + file_paths,
#         stdout=subprocess.PIPE,
#         stderr=subprocess.PIPE,
#         text=True
#     )
#     stdout, stderr = process.communicate()

#     # Check for any errors
#     if process.returncode != 0:
#         raise Exception(f"Error analyzing code: {stderr}")

#     # Parse the output as JSON
#     analysis_data = json.loads(stdout)

#     # Process the analysis data
#     total_loops = analysis_data['Loops']['total']
#     nested_loops = analysis_data['Loops']['nested']
#     if_else_statements = analysis_data['Decisions']

#     return total_loops, nested_loops, if_else_statements

# # Provide a list of Python file paths to analyze
# file_paths = ["C:\\Users\\Admin\\AppData\\Roaming\\Python\\Python311\\Scripts\\pyan3.exe"]

# total_loops, nested_loops, if_else_statements = analyze_code(file_paths)
# print("Total Loops:", total_loops)
# print("Nested Loops:", nested_loops)
# print("If/Else Statements:", len(if_else_statements))















# import ast

# class CodeAnalyzer(ast.NodeVisitor):
#     def __init__(self):
#         self.loop_count = 0
#         self.nested_loop_count = 0
#         self.if_else_count = 0
#         self.current_indentation = 0

#     def visit_For(self, node):
#         self.loop_count += 1
#         if self.current_indentation > 0:
#             self.nested_loop_count += 1
#         self.generic_visit(node)

#     def visit_While(self, node):
#         self.loop_count += 1
#         if self.current_indentation > 0:
#             self.nested_loop_count += 1
#         self.generic_visit(node)

#     def visit_If(self, node):
#         self.if_else_count += 1
#         self.generic_visit(node)

#     def visit_FunctionDef(self, node):
#         self.current_indentation += 1
#         self.generic_visit(node)
#         self.current_indentation -= 1

# def analyze_code(code):
#     tree = ast.parse(code)
#     analyzer = CodeAnalyzer()
#     analyzer.visit(tree)

#     return analyzer.loop_count, analyzer.nested_loop_count, analyzer.if_else_count

# code = """

# """

# total_loops, nested_loops, if_else_statements = analyze_code(code)
# print("Total Loops:", total_loops)
# print("Nested Loops:", nested_loops)
# print("If/Else Statements:", if_else_statements)

# import ast

# class CodeAnalyzer:
#     def __init__(self):
#         self.loop_count = 0
#         self.nested_loop_count = 0
#         self.if_else_count = 0

#     def analyze(self, code):
#         tree = ast.parse(code)
#         self.visit(tree)

#     def visit(self, node, depth=0):
#         if isinstance(node, ast.For) or isinstance(node, ast.While):
#             self.loop_count += 1
#             self.nested_loop_count = max(self.nested_loop_count, depth + 1)

#         if isinstance(node, ast.If):
#             self.if_else_count += 1

#         for child_node in ast.iter_child_nodes(node):
#             self.visit(child_node, depth + 1)

            


# code = """

# """

# analyzer = CodeAnalyzer()
# analyzer.analyze(code)

# print("TOTAL LOOPS: ", analyzer.loop_count)
# print("NESTED LOOPS: ", analyzer.nested_loop_count)
# print("IF/ELSE STATEMENTS: ", analyzer.if_else_count)




# import ast

# class CodeAnalyzer(ast.NodeVisitor):
#     def __init__(self):
#         self.loop_count = 0
#         self.nested_loop_count = 0
#         self.if_else_count = 0

#     def visit_For(self, node):
#         self.loop_count += 1
#         self.nested_loop_count += 1  # Increment for every loop encountered
#         self.generic_visit(node)

#     def visit_While(self, node):
#         self.loop_count += 1
#         self.nested_loop_count += 1  # Increment for every loop encountered
#         self.generic_visit(node)

#     def visit_If(self, node):
#         self.if_else_count += 1
#         self.generic_visit(node)

#     def handle_nested_loops(self, nodes, depth=0):
#         for node in nodes:
#             if isinstance(node, (ast.For, ast.While)):
#                 self.handle_nested_loops(node.body, depth + 1)
#             elif isinstance(node, ast.If):
#                 self.handle_nested_loops(node.body, depth)
#                 self.handle_nested_loops(node.orelse, depth)

# code = """
# """

# tree = ast.parse(code)
# analyzer = CodeAnalyzer()
# analyzer.visit(tree)
# analyzer.handle_nested_loops(tree.body, depth=0)

# print("TOTAL LOOPS: ", analyzer.loop_count)
# print("NESTED LOOPS: ", analyzer.nested_loop_count)
# print("IF/ELSE STATEMENTS: ", analyzer.if_else_count)


# import ast

# class CodeAnalyzer(ast.NodeVisitor):
#     def __init__(self):
#         self.loop_count = 0
#         self.nested_loop_count = 0
#         self.if_else_count = 0

#     def visit_For(self, node):
#         self.loop_count += 1
#         self.generic_visit(node)

#     def visit_While(self, node):
#         self.loop_count += 1
#         self.generic_visit(node)

#     def visit_If(self, node):
#         self.if_else_count += 1
#         self.generic_visit(node)
        
#     def handle_nested_loops(self, nodes, current_nested_count=0):
#         for node in nodes:
#             if isinstance(node, (ast.For, ast.While)):
#                 current_nested_count += 1
#                 if current_nested_count > self.nested_loop_count:
#                     self.nested_loop_count = current_nested_count
#                 self.handle_nested_loops(node.body, current_nested_count)
#                 current_nested_count -= 1  # Decrement after processing the inner loop
#             elif isinstance(node, ast.If):
#                 self.handle_nested_loops(node.body, current_nested_count)
#                 self.handle_nested_loops(node.orelse, current_nested_count)


    # def handle_nested_loops(self, nodes, current_nested_count=0):
    #     for node in nodes:
    #         if isinstance(node, (ast.For, ast.While)):
    #             current_nested_count += 1
    #             if current_nested_count > self.nested_loop_count:
    #                 self.nested_loop_count = current_nested_count
    #             self.handle_nested_loops(node.body, current_nested_count)
    #         elif isinstance(node, ast.If):
    #             self.handle_nested_loops(node.body, current_nested_count)
    #             self.handle_nested_loops(node.orelse, current_nested_count)
    

# code = """
# """

# tree = ast.parse(code)
# analyzer = CodeAnalyzer()
# analyzer.visit(tree)
# analyzer.handle_nested_loops(tree.body)

# print("TOTAL LOOPS: ", analyzer.loop_count)
# print("NESTED LOOPS: ", analyzer.nested_loop_count)
# print("IF/ELSE STATEMENTS: ", analyzer.if_else_count)





# import ast

# class CodeAnalyzer(ast.NodeVisitor):
#     def __init__(self):
#         self.loop_count = 0
#         self.nested_loop_count = 0
#         self.if_else_count = 0

#     def visit_For(self, node):
#         self.loop_count += 1
#         self.generic_visit(node)

#     def visit_While(self, node):
#         self.loop_count += 1
#         self.generic_visit(node)

#     def visit_If(self, node):
#         self.if_else_count += 1
#         self.generic_visit(node)

#     def visit_Else(self, node):
#         self.if_else_count += 1
#         self.generic_visit(node)

#     def handle_nested_loops(self, nodes):
#         current_nested_count = 0
#         for node in nodes:
#             if isinstance(node, (ast.For, ast.While)):
#                 current_nested_count += 1
#                 if current_nested_count > self.nested_loop_count:
#                     self.nested_loop_count = current_nested_count
#                 self.handle_nested_loops(node.body)
#             elif isinstance(node, ast.If):
#                 self.handle_nested_loops(node.body)
#                 self.handle_nested_loops(node.orelse)

# code = """ 


# """

# tree = ast.parse(code)
# analyzer = CodeAnalyzer()
# analyzer.visit(tree)
# analyzer.handle_nested_loops(tree.body)

# print("TOTAL LOOPS: ", analyzer.loop_count)
# print("NESTED LOOPS: ", analyzer.nested_loop_count)
# print("IF/ELSE STATEMENTS: ", analyzer.if_else_count)




# muhammad.amman@nlc.com.pk
# filereader pandas

# class CodeAnalyzer(ast.NodeVisitor):
#     def __init__(self):
#         self.loop_count = 0
#         self.current_loop_count = 0
#         self.nested_loop_count = 0
#         self.if_else_count = 0

#     def visit_For(self, node):
#         self.loop_count += 1
#         self.current_loop_count += 1
#         if self.current_loop_count > self.nested_loop_count:
#             self.nested_loop_count = self.current_loop_count
#         self.generic_visit(node)
#         self.current_loop_count -= 1

#     def visit_While(self, node):
#         self.loop_count += 1
#         self.current_loop_count += 1
#         if self.current_loop_count > self.nested_loop_count:
#             self.nested_loop_count = self.current_loop_count
#         self.generic_visit(node)
#         self.current_loop_count -= 1

#     def visit_If(self, node):
#         self.if_else_count += 1
#         self.generic_visit(node)

#     def visit_Else(self, node):
#         self.if_else_count += 1
#         self.generic_visit(node)

# code = """ 
# total_loops = 0
# total_if_else = 0

# for i in range(3):
#     total_loops += 1
#     if i % 2 == 0:
#         total_if_else += 1
#     else:
#         total_if_else += 2
#     for k in range(1):
#         total_loops += 1
#         if k == 0:
#             total_if_else += 1
#         else:
#             total_if_else += 2


# for j in range(2):
#     total_loops += 1
#     if j == 0:
#         total_if_else += 1
#     else:
#         total_if_else += 2

#     for k in range(1):
#         total_loops += 1
#         if k == 0:
#             total_if_else += 1
#         else:
#             total_if_else += 2
  
# """

# tree = ast.parse(code)
# analyzer = CodeAnalyzer()
# analyzer.visit(tree)

# print("TOTAL LOOPS: ", analyzer.loop_count)
# print("NESTED LOOPS: ", analyzer.nested_loop_count)
# print("IF/ELSE STATEMENTS: ", analyzer.if_else_count)


# class CodeAnalyzer(ast.NodeVisitor):
#     def __init__(self):
#         self.loop_count = 0
#         self.nested_loop_count = 0
#         self.if_else_count = 0
#         self.loop_stack = []  # Stack to keep track of nesting levels

#     def visit_For(self, node):
#         self.loop_count += 1
#         self.loop_stack.append('for')  # Push 'for' onto the stack
#         if len(self.loop_stack) > self.nested_loop_count:
#             self.nested_loop_count = len(self.loop_stack)
#         self.generic_visit(node)
#         self.loop_stack.pop()  # Pop 'for' from the stack

#     def visit_While(self, node):
#         self.loop_count += 1
#         self.loop_stack.append('while')  # Push 'while' onto the stack
#         if len(self.loop_stack) > self.nested_loop_count:
#             self.nested_loop_count = len(self.loop_stack)
#         self.generic_visit(node)
#         self.loop_stack.pop()  # Pop 'while' from the stack

#     def visit_If(self, node):
#         self.if_else_count += 1
#         self.generic_visit(node)

#     def visit_Else(self, node):
#         self.if_else_count += 1
#         self.generic_visit(node)

# class CodeAnalyzer(ast.NodeVisitor):
#     def __init__(self):
#         self.loop_count = 0
#         self.max_nesting = 0
#         self.current_nesting = 0 
#         self.if_else_count = 0

#     def visit_For(self, node):
#         self.loop_count += 1
#         self.current_nesting += 1
#         if self.current_nesting > self.max_nesting:
#             self.max_nesting += 1
#         self.generic_visit(node)
#         self.current_nesting -= 1

#     def visit_While(self, node):
#         self.loop_count += 1
#         self.current_nesting += 1
#         if self.current_nesting > self.max_nesting:
#             self.max_nesting = self.current_nesting
#         self.generic_visit(node)
#         self.current_nesting -= 1

#     def visit_If(self, node):
#         self.if_else_count += 1
#         self.generic_visit(node)

#     def visit_Else(self, node):
#         self.if_else_count += 1
#         self.generic_visit(node) 


