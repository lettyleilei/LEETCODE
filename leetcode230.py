class Solution:
    def kthSmallest(self, root, k):
        List = []
        def dfs(r):
            if r.left:
                dfs(r.left)
            if len(List)>=k:
                return
            List.append(r.val)
            if r.right:
                dfs(r.right)
        dfs(root)
        return List[k-1]
