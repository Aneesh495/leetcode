var removeLeafNodes = function(root, target) {
    const postorder = [];
    const stack = root ? [root] : [];
    while (stack.length) {
        const node = stack.pop();
        postorder.push(node);
        if (node.left) stack.push(node.left);
        if (node.right) stack.push(node.right);
    }
    for (let i = postorder.length - 1; i >= 0; --i) {
        const node = postorder[i];
        if (node.left && node.left.val === target && !node.left.left && !node.left.right) node.left = null;
        if (node.right && node.right.val === target && !node.right.left && !node.right.right) node.right = null;
    }
    return root.val === target && !root.left && !root.right ? null : root;
};