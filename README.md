# html2fb
Convert HTML to Facebook post format


# Algorithm

- Start from root node
- Traverse all current node. If there are formatter, push to the format-stack
- For each node, traverse all it child nodes
- If this is leaf node, write output
    - Combine all the formatters when writing the output
    - Supported formatter: list (ordered, unordered), bold, itatic, indent (?)

