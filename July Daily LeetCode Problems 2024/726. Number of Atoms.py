class Solution:
    def countOfAtoms(self, formula: str) -> str:
        import collections
        import re

        # Initialize stack and a dictionary to store counts
        stack = [collections.defaultdict(int)]
        i, n = 0, len(formula)

        while i < n:
            if formula[i] == '(':
                stack.append(collections.defaultdict(int))
                i += 1
            elif formula[i] == ')':
                i += 1
                num_start = i
                while i < n and formula[i].isdigit():
                    i += 1
                multiplier = int(formula[num_start:i] or 1)
                top = stack.pop()
                for atom, count in top.items():
                    stack[-1][atom] += count * multiplier
            else:
                atom_start = i
                i += 1
                while i < n and formula[i].islower():
                    i += 1
                atom = formula[atom_start:i]
                num_start = i
                while i < n and formula[i].isdigit():
                    i += 1
                count = int(formula[num_start:i] or 1)
                stack[-1][atom] += count

        # Process final counts
        final_counts = stack.pop()
        sorted_atoms = sorted(final_counts.items())

        # Build the result string
        result = []
        for atom, count in sorted_atoms:
            result.append(atom)
            if count > 1:
                result.append(str(count))

        return ''.join(result)